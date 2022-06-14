from flask import Flask, jsonify, request
from pytube import YouTube 
from flask_cors import CORS, cross_origin
from sqlalchemy import true


app = Flask(__name__)
CORS(app, resources={r"/app/*": {"origins": "*"}})

save_path='D:/'

@app.route('/app/getVideo',methods=['post'])
@cross_origin()
def downloadVideo():
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
    d_video.download(save_path) #downloading the video to path specified in save_path
    #yt.streams.download()
    return jsonify(['downloaded'])

if __name__ == '__main__':
    app.run(debug=True)
    