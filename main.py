from Image import *
from component import *
from device import *
<<<<<<< HEAD
import sample

if __name__=="__main__":
    
    sample.animal.dog()

=======
import matplotlib.image as mpimg
import sys
if __name__=="__main__":
    
    vb=loadfromobj('./model/rabbit.obj')

    img = mpimg.imread("./model/rabbit_texture.png")
    #plt.imshow(img[0:512,0:512])
    #plt.show()
    
    #"""
    #L1=light([0,0.5,-1.2],[-2,-1,-1],[200,200,200],"parell")
    L1=light([30,30,14],[2,1,-1],[200,200,200],"spot")

    
    device = context([400,400],[4,4],[0,0])
    device.setvertex(vb)#[12:15]
    #device.setindex(ib)
    device.inputlayout(1,0,1,1)
    device.setlight([L1])
    #device.set_mode("line")
    device.set_farest_plane(100)
    #device.geometrysh.setlootat([0.0,0.0,0.0])
    #device.geometrysh.setCamera([2.0,2.0,-2.0])
    device.geometrysh.setlootat([0.0,0.0,15])
    device.geometrysh.setCamera([30.0,-30.0,14.0])
    device.pixelsh.setTex(img)
    device.run()
    device.show()
    #"""
>>>>>>> 21f6ded06283429d1a8f036e09cd8856dfa5d69b
