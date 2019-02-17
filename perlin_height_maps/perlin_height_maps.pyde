
noiseScale = 0.03

def setup():
    size(400,400)
    # fullScreen()
    noFill()
    noSmooth()
    noiseSeed(999)

def draw():
    background('#B74C04')
    background(0)
    for x in range(width):
        for y in range(height):
            c = 255 * noise(x*noiseScale, y*noiseScale, frameCount * noiseScale)
            # print(c)
            if c > 255.0 * 2/3:
                if c > 255.0 * 5/6:
                    stroke('#0FFAE4')
                else:
                    stroke('#2DE0D0')
                point(x,y)
            elif c < 255 * 1/3:
                if c < 255.0 * 1/6:
                    stroke('#0641D1')
                else:
                    stroke('#2D5EE0')
                point(x,y)
