from PIL import Image
from pylab import *
import sys
import getopt
import os
import string
import pdb

#
# Calculates the threshold of an image
#

def readImage(imageName):
    im = array(Image.open(imageName).convert('L'))
    return im


def convolution():
    im = [[1,2,3],[4,5,6],[7,8,9]]
    mask = [[1,1,1],[1,1,1],[1,1,1]]
   
   # im = readImage('empire.jpg')
   # lx,ly = im.shape
    lx = len(im[0])/2
    ly = len (im)/2
    print "[DEBUG] lx = ",lx," ly = ",ly
    newIm = Image.new("RGB",(lx,ly))
    pix = newIm.load()
    total = 0
    
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for x in  [-1,0,1]:
                for y in  [-1,0,1]:
                    total += im[i][j] * mask[1-y][1-x]
                    #if (j == 3):
                   # gpdb.set_trace()            
                    print "Y[",i+1,"][",j+1,"]=im[",y,"][",x,"] * mask[",i-(y-1),"][",j-(x-1),"]"
            #pix[i][j] = total 

def threshold (thre):
    im = readImage('empire.jpg')
    lx,ly = im.shape 
    #print "[DEBUG] Threshold value =  ".thre
    for i in range (0,lx):
        for j in range (0,ly):
            valorPix = im[i][j]
            value = valorPix > thre
        #    pdb.set_trace()
            if value:
               # print "m[%d][%d] =  %d ",i,j,im[i][j]
                im[i][j] = 100
            else:
#                print "m[%d][%d] =  %d ",i,j,im[i][j]
                im[i][j] = 255               
    imshow(im,cmap=gray())
    show()
convolution()
"""
def main(argv):
    try:
        print "iniciando... " 
        #pdb.set_trace()
        opts, args = getopt.getopt(argv,"ht:i",["threshold=","image="])
    except getopt.GetoptError:
        print "-t <threshold>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '-t <threshold>'
            sys.exit()
        elif opt in ("-t","--threshold"):
            thre = arg
            threshold(int(thre))
            sys.exit()
        
            
if __name__ == "__main__":main(sys.argv[1:])# with if

"""

