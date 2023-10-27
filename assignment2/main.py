import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
button_val = None

def setup():
    p5.createCanvas(800, 800)

def draw():
    p5.background(0)
    global data_string, data_list
    global sensor_val, button_val

    data_string = document.getElementById("data").innerText
    # split data_string by comma, making a list:
    data_list = data_string.split(',')

    sensor_val = int(data_list[0])
    button_val = int(data_list[1])
    p5.noStroke()
    p5.fill(0)
    p5.text('sensor_val = ' + str(sensor_val), 10, 20)
    p5.text('button_val = ' + str(button_val), 10, 35)

    if(button_val == 0):
        p5.fill(255)  # red fill
    else:
        p5.fill(200,60,60)  # white fill

    p5.push()
    p5.translate(p5.width/2, p5.height/2)
    angle_offset = sensor_val

    scaling_factor = 1.5 if button_val == 1 else 1
    p5.scale(scaling_factor)

    num_petals = 5
    petal_distance = 90
    petal_length = 200
    petal_width = 200

    for i in range(num_petals):
        petal_angle = p5.TWO_PI / num_petals * i + p5.radians(angle_offset)
        x = p5.cos(petal_angle) * petal_distance
        y = p5.sin(petal_angle) * petal_distance
        
        p5.push()
        p5.translate(x, y)
        p5.rotate(petal_angle + p5.HALF_PI)
        
        p5.beginShape()
        p5.vertex(0, -petal_length/2)
        p5.bezierVertex(petal_width/6, -petal_length/3, petal_width/4, -petal_length/4, petal_width/3, 0)
        p5.bezierVertex(petal_width/4, petal_length/4, petal_width/6, petal_length/3, 0, petal_length/2)
        p5.bezierVertex(-petal_width/6, petal_length/3, -petal_width/4, petal_length/4, -petal_width/3, 0)
        p5.bezierVertex(-petal_width/4, -petal_length/4, -petal_width/6, -petal_length/3, 0, -petal_length/2)
        p5.endShape(p5.CLOSE)
        
        p5.pop()

    p5.fill(230)
    p5.ellipse(0, 0, 80, 80)
    p5.fill(100,80,180)
    for i in range(12):
        angle = p5.TWO_PI / 12 * i
        x = p5.cos(angle) * 30
        y = p5.sin(angle) * 30
        p5.ellipse(x, y, 10, 10)

    p5.pop()
