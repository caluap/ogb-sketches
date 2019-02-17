SILVER = 2.414
GOLDEN = 1.618
save_pdf = False
noiseScale = 0.03

def setup():
    add_library('pdf')
    size(594, 820)
    noStroke()

def draw():
    global save_pdf

    if save_pdf:
        beginRecord(PDF, 'output/#######.pdf')
                
    background(0)
    
    for i in range(13000):
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
        if p == -1:
            pass
        else:
            noStroke()
            if p == 1:
                fill('#3DE0D0')
            elif p == 2:
                fill('#F57C7C')
            else:
                fill(30)
            s = d/80.0
            ellipse(x, y, s, s)

    if save_pdf:
        endRecord()
        exit()

def keyPressed():
    global save_pdf
    if key == ENTER:
        save_pdf = True
    d = True
