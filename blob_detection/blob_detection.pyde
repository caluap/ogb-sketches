add_library('blobDetection')

noiseFactor = 0.006
noiseDetail(2,0.75)
blobDetector = None

# blob_factor = 0.8
perlin_threshold = 0.4


def setup():
    global blobDetector, blob_factor
    size(210, 297)
    blobDetector = BlobDetection(width,height)
    
    # blobDetector.setPosDiscrimination(True)
    # blobDetector.setThreshold(blob_factor)
    
    
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

    loadPixels()
    
    blobDetector.computeBlobs(pixels)
    # background(0)
    
    for i in range(blobDetector.getBlobNb()):
        blob = blobDetector.getBlob(i)
        
        stroke(255, 0, 0)
        noFill()
        beginShape()
        for i_vert in range(blob.getEdgeNb()):
            vert = blob.getEdgeVertexA(i_vert)
            x = vert.x * width
            y = vert.y * height
            curveVertex(x,y)
        endShape()
            
    
