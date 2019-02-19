noiseFactor = 0.01
hiTreshold = .50*255
# loTreshold = .54*255
loTreshold = hiTreshold

hiImg = None
loImg = None

bg = [0,0,0]

def setup():
    global hiImg, loImg
    size(297*2, 410*2)
    hiImg = loadImage("dots.png")
    loImg = loadImage("lines.png")
    
def draw(): 
    global hiImg, loImg
    background(*bg)
    for x in range(width):
        for y in range(height):
            c = int(noise(x*noiseFactor,y*noiseFactor, frameCount*noiseFactor) * 255)
            col = color(c)
            set(x,y,col)
    filter(BLUR, 7)
    
    for y in range(height):
        for x in range(width):
            c = get(x,y)
            if brightness(c) >= hiTreshold:
                cX = int(1.0 * x/width * hiImg.width)
                cY = int(1.0 * y/height * hiImg.height)
                imgC = hiImg.pixels[cX + cY * hiImg.width]
                set(x,y,imgC)
            elif brightness(c) < loTreshold:
                cX = int(1.0 * x/width * loImg.width)
                cY = int(1.0 * y/height * loImg.height)
                imgC = loImg.pixels[cX + cY * loImg.width]
                set(x,y,imgC)
            else:
                set(x,y,color(*bg))
            
