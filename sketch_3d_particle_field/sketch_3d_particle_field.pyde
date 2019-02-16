max_x, max_y, max_z = 1200, 1200, 4000
pg = None
ang = 0.0
max_size = 100


class Particle:
    def __init__(self, position, velocity, acceleration, siz):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.siz = siz
    
    def update(self):
        pass
    
    def accelerate(self):
        pass
        
    def draw_self(self):

        d = self.siz / max_size * 10 + 3
        sphereDetail(int(d))
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        rotateX(self.siz / max_size * TWO_PI)
        fill(128,90,200)
        noStroke()
        sphere(self.siz)
        popMatrix()

class ParticleGroup:
    def __init__(self, n):
        self.particles = []
        for i in range(n):
            pos = PVector(random(max_x), random(max_y), random(max_z))
            vel = PVector(0,0,0)
            acc = PVector(0,0,0)            
            s = pos.x * pos.y / (max_x * max_y) * max_size
            self.particles.append(Particle(pos, vel, acc, s))
    def update(self):
        pass
    def print_self(self):
        for p in self.particles:
            print(p.position)
    def draw_particles(self):
        for p in self.particles:
            p.draw_self()

    

def setup():
    global pg, max_x, max_y
    size(800,800, P3D)
    pg = ParticleGroup(1000)

def draw():
    global pg, ang
    
    lights()
    background(0)
    
    pushMatrix()
    translate(width/2, height/2)
    rotateX(ang)
    rotateY(-ang)
    translate(-width/2, -height/2)
    
    pg.draw_particles()
    
    popMatrix()
    
    ang += 0.01
