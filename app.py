from flask import Flask, render_template, Response
from camera_pi import Camera
import io

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera(),mimetype='multipart/x-mixed-replace; boundary=frame'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=False)