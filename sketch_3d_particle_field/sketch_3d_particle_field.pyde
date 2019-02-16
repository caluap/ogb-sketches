max_x, max_y, max_z = 300, 300, 20 


class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    
    def update():
        pass
    
    def accelerate():
        pass


class ParticleGroup:
    def __init__(self, n):
        self.particles = []
        for i in range(n):
            pos = PVector(random(max_x), random(max_y), random(max_z))
            vel = PVector(0,0,0)
            acc = PVector(0,0,0)
            self.particles.append(Particle(pos, vel, acc))
    def update():
        pass
    def print_self(self):
        for i in range(len(self.particles)):
            print(self.particles[i].acceleration)

    

def setup():
  size(800,800)

def draw():
    p = ParticleGroup(10)
    p.print_self()
    exit()
