from flask import Flask, render_template, Response, request
from camera_pi import Camera
import io
import servo_control as sc

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


### Request to send images
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')

### Controlling motors
@app.route('/move', methods=["POST"])
def move():
    content = request.json
    direction = content['direction']
    if direction == "forward":
        sc.forward()
    if direction == "backward":
        sc.backward()
    if direction == "right":
        sc.right()
    if direction == "left":
        sc.left()
    return "done"

@app.route('/start')
def start():
    motor_control.start()
    return "done"

@app.route('/stop')
def stop():
    motor_control.stop()
    return "done"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=False)