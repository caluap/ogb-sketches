
noiseFactor = 0.006
noiseDetail(2,0.75)

oct = 24
nd = 1.0


def setup():
    size(420, 594)
    
    
def draw():
    global blob, noiseFactor, nd, oct
    background(0)
    
    nd = 1.0 * mouseY/height
    oct = int(24.0 * mouseX/width)
    noiseDetail(oct, nd)
    
    for x in range(width):
        for y in range(height):
            perlin = noise(x * noiseFactor, y * noiseFactor, frameCount / 20.0)
            stroke(255 * perlin)            
            point(x,y)
            
    loadPixels()
    
def mouseWheel(event):
    global noiseFactor
    e = event.getCount()
    noiseFactor += -e * 0.005
    print(noiseFactor)
    
def mouseClicked():
    global nd, oct
    print(nd)
    print(oct)
