from numpy import *

class floatx():
    def __init__(self,list):
        self.val=list
        self.len=len(list)
    def new(self,list):
        return floatx(list)
    def __add__(self, other): 
        if type(other) is type(self) and self.len == other.len:
            result = [other.val[i]+self.val[i] for i in range(0,len(other.val))]
            return floatx(result)
        elif type(other) is list and self.len == len(other):
            result = [other[i]+self.val[i] for i in range(0,len(other.val))]
            return floatx(result)
        else:
            raise Exception("Invalid Op type! {type} + {type1}".format(type=type(self),type1=type(other)))
    def __mul__(self, other):   
        if type(other) is type(self):
            result = [other.val[i]*self.val[i] for i in range(0,len(other.val))]
            return sum(result)
        elif type(other) is list and self.len == len(other):
            result = [other[i]*self.val[i] for i in range(0,len(other.val))]
            return floatx(result) 
        elif type(other) is float or type(other) is int :
            result = [other.val[i]*self.val[i] for i in range(0,len(other.val))]
            return floatx(result)       
        else:
            raise Exception("Invalid Op type! {type} * {type1}".format(type=type(self),type1=type(other)))


class vertex():
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
        
if __name__=="__main__":
    v0=vertex([0,1,1])
    v1=vertex([0,0,1])
    v2=vertex([1,0,1])
    tri1=triangle([v0,v1,v2])
