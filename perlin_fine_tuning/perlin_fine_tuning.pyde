
noiseFactor = 0.006
noiseDetail(2,0.75)


def setup():
    size(594, 820)
    
    
def draw():
    global blob
    for x in range(width):
        for y in range(height):
            perlin = noise(x * noiseFactor, y * noiseFactor)
            stroke(255 * perlin)            
            point(x,y)
            
    loadPixels()
