from numpy import *

class pixelshader():
    def __init__(self):
        self.lightlist=None
    def lightfunction(self):
        for light in self.lightlist[0:1]:
            direct=self.pos - light.src
            r=linalg.norm(direct,axis =1)
            dmask=self.depthbuf<100
            args=(-self.normalbuf*direct).sum(1)
            args=args*dmask*(args>0)
            r=r*(args>0)
            args=(args-args.min())/(args.max()-args.min())*dmask
            args.shape=(len(args),1)
            self.colorbuf+= args.dot([light.color])
        
        self.colorbuf =self.colorbuf*255/self.colorbuf.max()
    def setTex(self,tex):
        self.tex=tex.astype('float')
        self.uv=array([tex.shape[0],tex.shape[1],0])
    def samplefromtexture(self):
        for i,color in enumerate(self.colorbuf):
            if self.uvbuf[i][0] >0:
                self.colorbuf[i] = self.colorbuf[i]*self.tex[512-self.uvbuf[i][0],self.uvbuf[i][1]][0:3]
        #pass
        self.colorbuf=self.colorbuf*255/self.colorbuf.max()
        
    def run(self,pixelin):
        self.colorbuf=pixelin[:,1]
        self.pos=pixelin[:,0]
        self.depthbuf=self.pos[:,2]
        #self.normalbuf=pixelin[:,2]
        uvbuf=(pixelin[:,3]*self.uv)
        self.uvbuf=(pixelin[:,3]*self.uv).astype('int')
        self.samplefromtexture()
        #self.lightfunction()
        return self.colorbuf,self.depthbuf
