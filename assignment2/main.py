import js as p5
from js import document

data = None

def setup():
    p5.createCanvas(400, 400)
    print('hello p5!')

def draw():
    p5.background(255)

    global data
    data = document.getElementById("data").innerText
    
    # Set the rotation angle based on the data
    angle = int(data)
    p5.push()
    p5.translate(p5.width/2, p5.height/2)
    p5.rotate(p5.radians(angle))
    
    # Draw the center of the flower
    p5.fill(255, 204, 0)  # Yellow color for the center
    p5.ellipse(0, 0, 50, 50)  # Center circle

    # Draw petals around the center
    num_petals = 8  # Number of petals
    petal_length = 100  # Length of the petal
    petal_width = 30  # Width of the petal

    p5.fill(255, 102, 204)  # Pink color for the petals
    for i in range(num_petals):
        petal_angle = p5.TWO_PI / num_petals * i
        x = p5.cos(petal_angle) * (25 + petal_length/2)
        y = p5.sin(petal_angle) * (25 + petal_length/2)
        p5.ellipse(x, y, petal_length, petal_width)
    
    p5.pop()
