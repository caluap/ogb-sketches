SILVER = 2.4142135623730950488
GOLDEN = 1.6180339887498948482

ang = 0.001

def setup():
    # size(600,600, P3D)
    fullScreen(P3D)
    sphereDetail(3)
    # ortho()

def draw():
    global ang
    
    lights()
    background(0)
    
    pushMatrix()    
    
    translate(width/2,height/2)
    scale(0.5,0.5,0.5)
    rotateX(ang)
    rotateY(-ang)
    
    n = 17000
    
    for i in range(n):
        
        pushMatrix()
        
        translate(width/2, height/2)
        
        angX = i * TAU / GOLDEN
        angY = i * TAU / GOLDEN
        
        rotateX(angX)
        rotateY(angY)

        d = 0.05 * i

        translate(-d, d, 0)
        
        noiseScale = 0.02
        perlin = noise(-d * noiseScale, d * noiseScale, frameCount * noiseScale)
        fill(perlin * 255, 0, 0)
        noStroke()
        
        siz = 10.0 * i / n 
        sphere(siz)
                
        popMatrix()
    
    popMatrix()
    ang += 0.01
