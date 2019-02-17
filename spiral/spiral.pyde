SILVER = 2.414
GOLDEN = 1.618

def setup():
    size(800, 800)
    noStroke()

def draw():
    
    background(0)
    
    for i in range(6000):
        pushMatrix()
        translate(width/2, height/2)
        ang = i * TAU / GOLDEN
        d = 0.1 * i
        y = sin(ang) * d
        x = cos(ang) * d
        
        perlin = noise(x, y, frameCount / 100)
        fill(255)
        s = d/60.0
        ellipse(x, y, s, s)
        popMatrix()
