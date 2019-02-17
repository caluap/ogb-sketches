SILVER = 2.414
GOLDEN = 1.618

def setup():
    size(594, 480)
    noStroke()

def draw():
    
    background(0)
    
    noiseScale = 0.03
    
    for i in range(9000):
        ang = i * TAU / GOLDEN
        d = 0.04 * i
        x = cos(ang) * d + width / 2        
        y = sin(ang) * d + height / 2

        
        if x > width or y > height:
            continue

        c = 255 * noise(x * noiseScale, y * noiseScale, frameCount * noiseScale)
        if 150 < c < 255:
            p = 1
        else:
            if 0 < c < 100:
                p = 2
            else:
                p = 0
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
