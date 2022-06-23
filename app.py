from flask import Flask, jsonify, request, send_file, send_from_directory
from pytube import YouTube 
from flask_cors import CORS, cross_origin
from sqlalchemy import true
import pathlib

app = Flask(__name__)
CORS(app, resources={r"/app/*": {"origins": "*"}})



@app.route('/app/getVideo',methods=['post'])
@cross_origin()
def downloadVideo():
    save_path=pathlib.Path().resolve()
    save_path=str(save_path)+'\\'
    url=request.data
    url=url.decode()
    print(url)
    yt = YouTube(url) 
    mp4files = yt.streams.filter(file_extension='mp4').get_highest_resolution().itag #getting higher resolution stream itag
    
    # print(mp4files.itag)
    # for i in mp4files:
    #    print(i.itag)
    # print(d_video)
    d_video=yt.streams.get_by_itag(mp4files) #getting stream based on itag
    print(d_video.default_filename)
    d_video.download(save_path) #downloading the video to path specified in save_path
    #yt.streams.download()
    return send_file(save_path+d_video.default_filename,as_attachment=True)

    # return jsonify(['hello'])

if __name__ == '__main__':
    app.run(debug=True)
    