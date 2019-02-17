def setup():
    size(540, 540)

def draw():
    
    background(0)
    
    for i in range(2000):
        pushMatrix()
        translate(width/2, height/2)
        ang = i * TAU / 1.618
        rotate(ang)
        translate(0, i * 0.2)
        fill(255)
        ellipse(0, 0, 3, 3)
        popMatrix()
