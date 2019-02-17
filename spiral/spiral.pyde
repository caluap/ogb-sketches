SILVER = 2.414
GOLDEN = 1.618

def setup():
    size(297, 410)
    noStroke()

def draw():
    
    background(0)
    
    noiseScale = 0.03
    perl = []
    for x in range(width):
        line = []
        for y in range(height):
            c = 255 * noise(x * noiseScale, y * noiseScale, frameCount * noiseScale)
            if 150 < c < 255:
                line.append(1)
            else:
                if 0 < c < 100:
                    line.append(2)
                else:
                    line.append(0)
        perl.append(line)
                # stroke('#3DE0D0')
                # point(x,y) 
    
    for i in range(7000):
        pushMatrix()
        translate(width/2, height/2)
        ang = i * TAU / GOLDEN
        d = 0.04 * i
        y = sin(ang) * d
        x = cos(ang) * d
        p = perl[int(x)][int(y)]
        if p == 0:
            pass
        else:
            noStroke()
            if p == 1:
                fill('#3DE0D0')
            else:
                fill('#F57C7C')
            s = d/80.0
            ellipse(x, y, s, s)
        popMatrix()
