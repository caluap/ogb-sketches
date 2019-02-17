max_x, max_y, max_z = 800, 800, 500
pgs = []
ang = 0.0
max_size = 100
polys = []

save_pdf = False


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

        if True:
            siz = 6
            sphereDetail(siz)
            pushMatrix()
            translate(self.position.x, self.position.y, self.position.z)
            fill(128, 90, 200)
            noStroke()
            sphere(siz)
            popMatrix()
        else:
            curveVertex(self.position.x, self.position.y, self.position.z)

class ParticleGroup:

    def __init__(self, n):
        self.particles = []
        for i in range(n):
            if i == 0:
                pos = PVector(
                    random(max_x), random(max_y), random(max_z) - max_z / 2)
            else:
                x = noise(self.particles[i - 1].position.x) * max_x
                y = noise(self.particles[i - 1].position.y) * max_y
                z = noise(self.particles[i - 1].position.z) * max_z - max_z / 2
                pos = PVector(x, y, z)
            vel = PVector(0, 0, 0)
            acc = PVector(0, 0, 0)
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

def generate_polygons(n, r):
    polys = []
    for _ in range(n):
        poly = []
        for i in range(int(random(r)) + 3):
            if i == 0:
                x = random(width)
                y = random(height)
                poly.append(PVector(x, y, 0))
            else:
                x = poly[i - 1].x
                y = poly[i - 1].y
                d = 0.5
                x += noise(x, y) * random(width / d) * [-1, 1][int(random(2))]
                y += noise(x, y) * random(height / d) * [-1, 1][int(random(2))]
                poly.append(PVector(x, y, 0))
        polys.append(poly)
    return polys

def draw_polygons(polys):

    fill('#FF8E43')
    noStroke()
    pushMatrix()
    scl = 1.3
    scale(scl, scl, scl)
    for poly in polys:
        beginShape()
        for p in poly:
            vertex(p.x, p.y, p.z)
        endShape()
    popMatrix()


def rotate_view(ang):
    translate(width / 2, height / 2)
    rotateX(ang)
    rotateY(-ang)
    translate(-width / 2, -height / 2)

def setup():
    global pgs, max_x, max_y, polys
    add_library('pdf')
    hint(ENABLE_DEPTH_SORT)
    size(297, 410, P3D)
    max_x = width
    max_y = height

    for _ in range(7):
        pgs.append(ParticleGroup(5))
    polys = generate_polygons(5, 0)

def draw():
    global pgs, ang, polys, save_pdf

    if save_pdf:
        beginRaw(PDF, 'output/#######.pdf')

    lights()
    background(0)

    pushMatrix()

    # zoom out?
    translate(0, 0, -100)

    rotate_view(ang)

    draw_polygons(polys)

    for pg in pgs:
        pg.draw_particles()

    popMatrix()

    ang += 0.005

    if save_pdf:
        endRaw()
        exit()

def keyPressed():
    global save_pdf
    if key == ENTER:
        save_pdf = True
    d = True
