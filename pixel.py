from numpy import *

class pixelshader():
    def __init__(self):
        pass
    def run(self,pixelin):
        colorbuf=[]
        depthbuf=[]
        for pix in pixelin:
            colorbuf.append(pix[1])
            depthbuf.append(pix[0][2])
        return colorbuf,depthbuf
