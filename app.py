from flask import Flask, render_template, Response
import picamera
import io

app = Flask(__name__)
cam = picamera.PiCamera()
img_stream = io.BytesIO()
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        cam.capture(img_stream, 'jpeg')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_stream + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/move/<dire>')
def profile(dire="aaaa"):
    print(dire)
    return ""


if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, threaded=True)