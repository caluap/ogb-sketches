noiseFactor = 0.01
hiTreshold = .54*255
loTreshold = .34*255

hiImg = None


def setup():
    global hiImg
    size(297*2, 410*2)
    hiImg = loadImage("dots.png")
    
def draw(): 
    global hiImg
    background(0)
    for x in range(width):
        for y in range(height):
            c = int(noise(x*noiseFactor,y*noiseFactor, frameCount*noiseFactor) * 255)
            col = color(c)
            set(x,y,col)
    filter(BLUR, 7)
    
    for y in range(height):
        for x in range(width):
            c = get(x,y)
            if brightness(c) > hiTreshold:
                cX = int(1.0 * x/width * hiImg.width)
                cY = int(1.0 * y/height * hiImg.height)
                imgC = hiImg.pixels[cX + cY * hiImg.width]
                set(x,y,imgC)
            elif brightness(c) < loTreshold:
                set(x,y,color(0,255,0))
            else:
                set(x,y,color(0,0,0))
            
