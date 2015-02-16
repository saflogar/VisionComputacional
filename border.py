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
    mask = [[1,1,1][1,1,1][1,1,1]]
    im = readImage('empire.jpg')
    
    pix = newIm.load()
    lx,ly = im.shape
    newIm = Image.new("RGB",(lx,ly))
    total = 0
    for i in range (lx):
        for j in range (ly):
            for x in range (0,2):
                for y in range (0,2):
                    total += im[i][j] * mask[x-fi][j-i]
            pix[i][j] = total 

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

