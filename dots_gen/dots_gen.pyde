GOLDEN = 1.6180339887498948482
noiseScale = 0.015
dInc = 0.025
blankRadius = 0
dashSize = 10.0  
margin = 20

savePDF = False

def setup():
    add_library('pdf')
    size(297*2, 410*2)
    
    
def draw(): 
    global savePDF
    
    if savePDF:
        fileName = 'output/' + str(year()) + '-' + str(month()) + '-' + str(day()) + '-' + str(hour()) + '-' + str(minute()) + '-' + str(second()) + '.pdf'
        beginRecord(PDF, fileName)
        
    n = 24000   
    background(0)
    for i in range(n):
        ang = i * TAU / GOLDEN
        blank_radius = 2
        
        d = blankRadius + dInc * i
        x = cos(ang) * d + width / 2        
        y = sin(ang) * d + height / 2
        
        
        if x > -margin and x < width+margin and y > -margin and y < height+margin:
       
            noiz = noise(x*noiseScale, y*noiseScale, frameCount/20.0)
            angle = noiz * TWO_PI          
            noiz = min(1.0, (noiz-0.1) / 0.8) # flatten somewhat the color curve here
            
            stroke(noiz*255,noiz*255,noiz*255)

            
            adjDash = dashSize * (0.1 + 1.0*i/n)
            
            distX = cos(angle) * adjDash
            distY = sin(angle) * adjDash
            
            line(x,y, x+distX,y+distY)
            
    if savePDF:
        endRecord()
        savePDF = False
            
def keyPressed():
    global savePDF
    if key == ENTER:
        savePDF = True
    d = True
