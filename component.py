from numpy import *

class vertex():
    def __init__(self,pos=None,color=None,normal=None,uv=None):
        if type(pos) is list:
            self.pos=array(pos)
        else:
            self.pos=pos
        if type(color) is list:
            self.color=array(color)
        else:
            self.color=color
        if type(normal) is list:
            self.normal=array(normal)
        else:
            self.normal=normal
        if type(uv) is list:
            self.uv=uv
        else:
            self.uv=uv

class pixel():
    def __init__(self,pos=None,color=None,uv=None):
        if type(pos) is list:
            self.pos=array(pos)
        else:
            self.pos=pos
        if type(color) is list:
            self.color=array(color)
        else:
            self.color=color
        if type(uv) is list:
            self.uv=uv
        else:
            self.uv=uv

class triangle():
    def __init__(self,vertexlist):
        if len(vertexlist)==3:
            self.vertexlist = vertexlist

class light():
    def __init__(self,src,direct,clour):
        self.src=array(src)
        self.direct=array(direct)
        self.color=array(clour)
        
if __name__=="__main__":
    v0=vertex([0,1,1])
    v1=vertex([0,0,1])
    v2=vertex([1,0,1])
    tri1=triangle([v0,v1,v2])
