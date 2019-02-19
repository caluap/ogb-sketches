add_library('blobDetection')
add_library('pdf')

noiseFactor = 0.011
noiseDetail(17,0.397)
blobDetectors = []

perlin_threshold = 0.5

levels = 5


def setup():
    size(210, 297)
    # blobDetector = BlobDetection(width,height)
    # blobDetector.setPosDiscrimination(True)
    # blobDetector.setThreshold(blob_factor)
    
    noiseDetail(18, 0.63)
    noSmooth()
    
def draw():
    global blobDetectors, levels
    
    background(0)
    
    for x in range(width):
        for y in range(height):
            perlin = noise(x * noiseFactor, y * noiseFactor, frameCount / 20.0)
            if perlin > perlin_threshold:
                stroke(255)
            else:
                stroke(0)
            # stroke(255 * perlin)            
            point(x,y)

    filter(BLUR, 8)
    
    loadPixels()
    background(0)
    
    for _ in range(levels):
        blobDetector = BlobDetection(width,height)
        blobDetector.setThreshold(1.0*_/levels)
        blobDetector.computeBlobs(pixels)
        blobDetectors.append(blobDetector)

    noFill()    
    col = 0
    
    fileName = 'output/' + str(year()) + '-' + str(month()) + '-' + str(day()) + '-' + str(hour()) + '-' + str(minute()) + '-' + str(second()) + '.pdf'
    
    beginRecord(PDF, fileName)
    
    for blobDetector in blobDetectors:    
        stroke(col * 255 / levels)
        noFill()
        col += 1
        for i in range(blobDetector.getBlobNb()):
            blob = blobDetector.getBlob(i)
    
            beginShape()
            init = -1
            for i_vert in range(blob.getEdgeNb()):
                vertA = blob.getEdgeVertexA(i_vert)
                vertB = blob.getEdgeVertexB(i_vert)
                xA = vertA.x * width
                yA = vertA.y * height
                xB = vertB.x * width
                yB = vertB.y * height
                
                # print(str(xA) + ',' + str(yA) + ' - ' + str(xB) + ',' + str(yB))
                vertex(xA,yA)
                vertex(xB,yB)
                # line(xA,yA, xB,yB)
                
            endShape()
            
    endRecord()        
    noLoop()
    
