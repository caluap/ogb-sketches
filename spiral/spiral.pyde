SILVER = 2.414
GOLDEN = 1.6180339887498948482
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
        blank_radius = 2
        
        d = blank_radius + 0.08 * i
        x = cos(ang) * d + width / 2        
        y = sin(ang) * d + height / 2

        
        if x > width or y > height:
            continue

        c = 255 * noise(x * noiseScale, y * noiseScale, frameCount * noiseScale)
        
        tints_a = ['#FFF9C4','#FFF59D','#FFF176','#FFEE58','#FFEB3B'] #yellow
        tints_b = ['#80D8FF','#40C4FF','#00B0FF','#0091EA'] #blue
        tints_c = ['#F44336','#E53935','#D32F2F','#C62828','#B71C1C'] #red
        tints_d = ['#B9F6CA','#69F0AE','#00E676','#00C853'] #green
        
        min_1 = 155
        max_1 = 255
        min_2 = 0
        max_2 = 100
        
        if min_1 < c < max_1:
            p = 1
            f = tints_c[int((c-min_1)/(max_1-min_1) * len(tints_c))]
        else:
            if min_2 < c < max_2:
                p = 2
                f = tints_c[int((c-min_2)/(max_2-min_2) * len(tints_c))]
            else:
                p = 0
        if p == 0:
            pass
        else:
            noStroke()
            if p == 1:
                fill(f)
            elif p == 2:
                fill(f)
            else:
                fill(30)
                
            s = i / 500.0 + 1.0
            ellipse(x, y, s, s)

    if save_pdf:
        endRecord()
        exit()

def keyPressed():
    global save_pdf
    if key == ENTER:
        save_pdf = True
    d = True
