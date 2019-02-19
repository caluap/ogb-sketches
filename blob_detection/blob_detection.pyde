add_library('blobDetection')

noiseFactor = 0.011
noiseDetail(17,0.397)
blobDetector = None

blob_factor = 0.8
perlin_threshold = 0.5


def setup():
    global blobDetector, blob_factor
    size(210*2, 297*2)
    blobDetector = BlobDetection(width,height)
    blobDetector.setPosDiscrimination(True)
    blobDetector.setThreshold(blob_factor)
    
    noiseDetail(18, 0.63)
    noSmooth()
    
def draw():
    global blobDetector, blob_factor
    
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

    filter(BLUR, 6)
    
    loadPixels()
    blobDetector.computeBlobs(pixels)
    
    background(0)
    noFill()
    stroke(255,0,0)         
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
            line(xA,yA, xB,yB)
            
        endShape()
            
    
