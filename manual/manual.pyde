noiseFactor = 0.01
hiTreshold = .60*255
loTreshold = .40*255

saveImg = False

hiImg = None
loImg = None

bg = [255,0,255]
pg = None

def setup():
    global hiImg, loImg, pg
    size(297, 410)
    hiImg = loadImage("dots.png")
    loImg = loadImage("lines.png")
    
    # pg = createGraphics(2475, 3417)
    pg = createGraphics(297, 410)
    
def draw(): 
    global hiImg, loImg, saveImg, pg
    
    background(*bg)
    for x in range(width):
        for y in range(height):
            c = int(noise(x*noiseFactor,y*noiseFactor, frameCount*noiseFactor) * 255)
            col = color(c)
            set(x,y,col)
    filter(BLUR, 7)
    
    w = width
    h = height
    
    if saveImg:
        pg.beginDraw()
    
    for x in range(w):
        for y in range(h):
            c = get(x,y)
            if brightness(c) >= hiTreshold:
                cX = int(1.0 * x/w * hiImg.width)
                cY = int(1.0 * y/h * hiImg.height)
                imgC = hiImg.pixels[cX + cY * hiImg.width]
                if not saveImg:
                    set(x,y,imgC)
                else:
                    pg.set(x,y,imgC)
            elif brightness(c) < loTreshold:
                cX = int(1.0 * x/w * loImg.width)
                cY = int(1.0 * y/h * loImg.height)
                imgC = loImg.pixels[cX + cY * loImg.width]                
                if not saveImg:
                    set(x,y,imgC)
                else:
                    pg.set(x,y,imgC)
            else:
                if not saveImg:
                    set(x,y,color(*bg))
    
    
    if saveImg:
        pg.endDraw()
        fileName = 'output/' + str(year()) + '-' + str(month()) + '-' + str(day()) + '-' + str(hour()) + '-' + str(minute()) + '-' + str(second()) + '.png'
        pg.save(fileName)
        saveImg = False
                

            
def keyPressed():
    global saveImg
    if key == ENTER:
        saveImg = True
            
