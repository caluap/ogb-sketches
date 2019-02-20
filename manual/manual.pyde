noiseFactor = 0.05
hiTreshold = .50*255
loTreshold = .45*255

saveImg = False

hiImg = None
loImg = None

bg = [255,0,255]
pg = None

def setup():
    global hiImg, loImg, pg
    size(297, 410)
    hiImg = loadImage("dots.jpg")
    loImg = loadImage("lines.png")
    
    pg = createGraphics(2475, 3417) # 300dpi
    # pg = createGraphics(1754, 2480) #150dpi
    
def draw(): 
    global hiImg, loImg, saveImg, pg
    
    if saveImg:
        pCorrection = 1.0 * width / pg.width
        pg.beginDraw()
        w = pg.width
        h = pg.height
        print('began saving...')
    else:
        pCorrection = 1
        background(*bg)
        w = width
        h = height
        
    for x in range(w):
        for y in range(h):
            c = int(noise(x*noiseFactor*pCorrection,y*noiseFactor*pCorrection, frameCount*noiseFactor) * 255)
            col = color(c)
            if not saveImg:
                set(x,y,col)
            else:
                pg.set(x,y,col)
                
    if saveImg:        
        print('perlin done')    
        pg.filter(BLUR, 7)
        print('blur done')
    else:
        filter(BLUR, 7)
    
    for x in range(w):
        for y in range(h):
            if saveImg:
                c = pg.get(x,y)
            else:
                c = get(x,y)
            if brightness(c) > hiTreshold:
                cX = int(1.0 * x/w * hiImg.width)
                cY = int(1.0 * y/h * hiImg.height)
                imgC = hiImg.pixels[cX + cY * hiImg.width]
                if saveImg:
                    pg.set(x,y,imgC)
                else:
                    set(x,y,imgC)
            elif brightness(c) <= loTreshold:
                cX = int(1.0 * x/w * loImg.width)
                cY = int(1.0 * y/h * loImg.height)
                imgC = loImg.pixels[cX + cY * loImg.width]                
                if saveImg:
                    pg.set(x,y,imgC)
                else:
                    set(x,y,imgC)
            else:
                if saveImg:
                    pg.set(x,y,color(*bg))
                else:
                    set(x,y,color(*bg))
    
    
    if saveImg:
        print('img placement done')
        pg.endDraw()
        fileName = 'output/' + str(year()) + '-' + str(month()) + '-' + str(day()) + '-' + str(hour()) + '-' + str(minute()) + '-' + str(second()) + '.png'
        pg.save(fileName)
        print('saved as ' + fileName)
        saveImg = False
                

            
def keyPressed():
    global saveImg
    if key == ENTER:
        saveImg = True
    if key == TAB:
        noiseSeed(int(random(32767)))
            
