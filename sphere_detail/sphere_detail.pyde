lon = 3
lan = 3
ang = 0.0

def setup():
    size(400,400, P3D)

def draw():
    global lon, lan, ang
    
    lon = int(1.0 * mouseX / width * 30 + 3)
    lan = int(1.0 * mouseY / height * 30 + 3)
    
    
    background(128)
    lights()
    
    pushMatrix()
    
    translate(width/2,height/2)
    rotateY(ang)
    rotateX(-ang)

    sphereDetail(lon, lan)
    fill(0,0,255)
    stroke(0,255,0)
    sphere(40)
    
    popMatrix()
    
    ang += 0.01
