def setup():
    size(540, 540)

def draw():
    
    background(0)
    
    for i in range(2000):
        pushMatrix()
        translate(width/2, height/2)
        ang = i * TAU / 1.618
        d = 0.2 * i
        y = sin(ang) * d
        x = cos(ang) * d
        stroke(255)
        noFill()
        point(x, y)
        popMatrix()
