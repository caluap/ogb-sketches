SILVER = 2.414
GOLDEN = 1.6180339887498948482
savePDF = False
noiseScale = 0.015

min_1 = 135
max_1 = 255
min_2 = 0
max_2 = 100

perlinDots = True

def setup():
    add_library('pdf')
    size(594, 820)
    noStroke()

def draw():
    global savePDF

    if savePDF:
        beginRecord(PDF, 'output/#######.pdf')
                
    # background('#621727')
    background(0)
    
    for i in range(13000):
        ang = i * TAU / GOLDEN
        blank_radius = 2
        
        d = blank_radius + 0.08 * i
        x = cos(ang) * d + width / 2        
        y = sin(ang) * d + height / 2

        
        if x > width or x < 0 or y > height or y < 0:
            continue
        else:
    
            c = 255 * noise(x * noiseScale, y * noiseScale, frameCount * noiseScale)
            
            tints_a = ['#FFF9C4','#FFF59D','#FFF176','#FFEE58','#FFEB3B'] #yellow
            tints_b = ['#80D8FF','#40C4FF','#00B0FF','#0091EA'] #blue
            tints_c = ['#F44336','#E53935','#D32F2F','#C62828','#B71C1C'] #red
            tints_d = ['#B9F6CA','#69F0AE','#00E676','#00C853'] #green
            

            
            if min_1 < c < max_1:
                p = 1
                f = '#000091'
                # f = tints_c[int((c-min_1)/(max_1-min_1) * len(tints_c))]
            else:
                if min_2 < c < max_2:
                    p = 2
                    f = '#ff0000'
                    # f = tints_c[int((c-min_2)/(max_2-min_2) * len(tints_c))]
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
    
    if perlinDots:
        for x in range(width):
            for y in range(height):
                c = 255 * noise(x * noiseScale, y * noiseScale, frameCount * noiseScale)
                if c >= max_2 and c <= min_1:
                    f = '#211006'
                    stroke(f)
                    point(x,y)

    if savePDF:
        endRecord()
        exit()

def keyPressed():
    global savePDF
    if key == ENTER:
        savePDF = True
    d = True
