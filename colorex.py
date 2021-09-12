import cv2 as cv
import numpy as np 
import functools
import math

WIDTH = 512 * 3 
HEIGHT = 178 

def getcounts(res) -> dict: 
    
    count = {}
    for color in res: 
        count[color] = 1 if color not in count else count[color] + 1 
    return count 


def getColors(impath: str, K= 8): 
    im = cv.imread(impath)

    Z = im.reshape((-1,3))

    Z = np.float32(Z)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 50, 1.0)
    ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    tupped = list(map(lambda x: (x[0],x[1],x[2]), center))

    res = center[label.flatten()]
    tuppedres = list(map(lambda x: (x[0],x[1],x[2]), res))
    
    count = getcounts(tuppedres)
    
    tupped2 = list(map(lambda x: (x[0],x[1],x[2],count[x]), tupped))
    tupped2 = sorted(tupped2,key= lambda x: x[3],reverse=True)
    
    
    pixsum = 0
    for color in tupped2: 
        pixsum += color[3]
        
    return tupped2, pixsum




def genColorRect(name: str, impath: str, K= 8, colors = None, pixsum= None ) -> None : 
    if not colors: 
        colors, pixsum = getColors(impath, K)
    img = np.zeros((HEIGHT,WIDTH,3), np.uint8) 
    offset = 0
    for color in colors: 
        ratio = color[3] / pixsum
        cwidth = math.ceil (ratio * WIDTH)
 
        cent = (int(color[0]),int(color[1]),int(color[2]))
    #cv.rectangle(img, (0,i * incr), (512,(i + 1) * incr) , cent, -1) 
        start = (offset, 0)
        end = (offset + cwidth,512 )
        offset += cwidth 
        cv.rectangle(img, start, end , cent, -1) 
    cv.imwrite("paletteref/" + name, img)
    #cv.imshow("color", img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

def writeColors(name: str, colors) -> None: 
    f = open("palettes.txt", "a")
    f.write(name)
    f.write("\n")
    for color in colors: 
        f.write(str(color[0:3]) + " " + str(color[3]) + "\n")
def consumeImage(name: str, K= 8): 
    impath = "refpics/" + name
    print("Starting...")
    colors, pixsum = getColors(impath, K)
    print("Got colors..." )
    genColorRect(name,impath,colors=colors,pixsum=pixsum)
    print("Generated Reference image..." )
    writeColors(name,colors)
    print("Done!")
    return

#consumeImage("WilhelminaGardenPal.jpg", "WilhelminaGarden.jpg")