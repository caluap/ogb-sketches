max_x, max_y, max_z = 800, 800, 500
pgs = []
ang = 0.0
max_size = 100


class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    
    def update(self):
        pass
    
    def accelerate(self):
        pass
        
    def draw_self(self):

        if False:
            d = self.siz / max_size * 10 + 3
            sphereDetail(int(d))
            pushMatrix()
            translate(self.position.x, self.position.y, self.position.z)
            rotateX(self.siz / max_size * TWO_PI)
            fill(128,90,200)
            noStroke()
            sphere(self.siz)
            popMatrix()
        else:
            curveVertex(self.position.x, self.position.y, self.position.z)

class ParticleGroup:
    def __init__(self, n):
        self.particles = []
        for i in range(n):
            pos = PVector(random(max_x), random(max_y), random(max_z) - max_z/2)
            vel = PVector(0,0,0)
            acc = PVector(0,0,0)
            self.particles.append(Particle(pos, vel, acc))
    def update(self):
        pass
    def print_self(self):
        for p in self.particles:
            print(p.position)
    def draw_particles(self):
        beginShape()
        strokeWeight(2)
        noFill()
        for p in self.particles:
            stroke('#72FA97')
            p.draw_self()
        endShape()
        
def draw_polygons():
    polys = [[
          ( width*.80, height*.10, 0),
          ( width*.85, height*.23, 0),
          ( width*.78, height*.17, 0),
          ( width*.56, height*.45, 0),
          ( width*.14, height*.56, 0),
          ( width*.78, height*.23, 0)]]
    polys.append([( width*.56, height*.77, 0),
          ( width*.76, height*.55, 0),
          ( width*.33, height*.66, 0),
          ( width*.78, height*.99, 0),
          ( width*.99, height*.88, 0),
          ( width*.78, height*.55, 0)])
    
    fill('#FF8E43')
    noStroke()
    pushMatrix()
    scl = 1.3
    scale(scl,scl,0)
    for poly in polys:
        beginShape()
        for p in poly:
            vertex(p[0], p[1], p[2])
        endShape()
    popMatrix()
    

def rotate_view(ang):
    translate(width/2, height/2)
    rotateX(ang)
    rotateY(-ang)
    translate(-width/2, -height/2)

def setup():
    global pgs, max_x, max_y
    size(297,410, P3D)
    max_x = width
    max_y = height
    
    for _ in range(10):
        pgs.append(ParticleGroup(5))

def draw():
    global pgs, ang
    
    lights()
    background('#FFDEDE')
    background(0)
        
    pushMatrix()
    
    # zoom out?
    translate(0,0,-400)
    
    rotate_view(ang)
    
    draw_polygons()
    
    for pg in pgs:
        pg.draw_particles()
    
    popMatrix()
    
    ang += 0.005
