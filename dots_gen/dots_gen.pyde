GOLDEN = 1.6180339887498948482
noiseScale = 0.015
dInc = 0.03
blankRadius = 10
jitDist = 5.0

def setup():
    size(297*2, 410*2)
    
    
def draw():
    
    n = 15000
    
    background(0)
    for i in range(n):
        ang = i * TAU / GOLDEN
        blank_radius = 2
        
        d = blankRadius + dInc * i
        x = cos(ang) * d + width / 2        
        y = sin(ang) * d + height / 2
        
        jitX = float(i)/n * random(jitDist)
        jitY = float(i)/n * random(jitDist)
        
        x += jitX
        y += jitY
        
        set(x,y, color(255,0,0))
        
    noLoop()
