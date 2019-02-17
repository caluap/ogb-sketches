SILVER = 2.414
GOLDEN = 1.618

def setup():
    size(400, 400)
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
        noStroke()
        fill(255)
        s = d/60.0
        ellipse(x, y, s, s)
        popMatrix()
    
    noiseScale = 0.03
    for x in range(width):
        for y in range(height):
            c = 255 * noise(x * noiseScale, y * noiseScale, frameCount * noiseScale)
            if 120 < c < 140:
                stroke('#3DE0D0')
                point(x,y) 
