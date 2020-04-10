
from Image import *
from component import *
from device import *
import matplotlib.image as mpimg
import sys
if __name__=="__main__":
    
    vb=[		vertex( [ -1.0, 1.0, -1.0, 1.0 ], normal=[ 0.0, 1.0, 0.0 ] ,uv=[0.0,0.0]),
        vertex( [ 1.0, 1.0, -1.0, 1.0 ],normal= [ 0.0, 1.0, 0.0 ] ,uv=[0.0,1.0]),
        vertex( [ 1.0, 1.0, 1.0, 1.0  ], normal=[ 0.0, 1.0, 0.0 ] ,uv=[1.0,0.0]),
        vertex( [ -1.0, 1.0, 1.0, 1.0  ], normal=[ 0.0, 1.0, 0.0 ],uv=[1.0,1.0]),

        vertex( [ -1.0, -1.0, -1.0, 1.0  ],normal= [ 0.0, -1.0, 0.0 ],uv=[0.0,0.0]) ,
        vertex( [ 1.0, -1.0, -1.0, 1.0  ],normal= [ 0.0, -1.0, 0.0 ],uv=[0.0,1.0]) ,
        vertex( [ 1.0, -1.0, 1.0, 1.0  ],normal= [ 0.0, -1.0, 0.0 ],uv=[1.0,0.0]) ,
        vertex( [ -1.0, -1.0, 1.0, 1.0  ], normal=[ 0.0, -1.0, 0.0 ] ,uv=[1.0,1.0]),

        vertex( [ -1.0, -1.0, 1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ],uv=[0.0,0.0]) ,
        vertex( [ -1.0, -1.0, -1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ],uv=[1.0,0.0]),
        vertex( [ -1.0, 1.0, -1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ],uv=[0.0,1.0]),
        vertex( [ -1.0, 1.0, 1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ] ,uv=[1.0,1.0]),#11

        vertex( [ 1.0, -1.0, 1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ],uv=[1.0,1.0]) ,
        vertex( [ 1.0, -1.0, -1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ],uv=[0.0,1.0]) ,
        vertex( [ 1.0, 1.0, -1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ],uv=[0.0,0.0]) ,
        vertex( [ 1.0, 1.0, 1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ],uv=[1.0,0.0] ),#15

        vertex( [ -1.0, -1.0, -1.0, 1.0  ], normal= [ 0.0, 0.0, -1.0 ],uv=[1.0,0.0] ),
        vertex( [ 1.0, -1.0, -1.0, 1.0  ],normal=  [ 0.0, 0.0, -1.0 ],uv=[1.0,1.0] ),
        vertex( [ 1.0, 1.0, -1.0, 1.0  ],normal=  [ 0.0, 0.0, -1.0 ],uv=[0.0,1.0] ),
        vertex( [ -1.0, 1.0, -1.0, 1.0  ],normal=  [ 0.0, 0.0, -1.0 ],uv=[0.0,0.0] ),#19

        vertex( [ -1.0, -1.0, 1.0, 1.0  ], normal= [ 0.0, 0.0, 1.0 ],uv=[0.0,0.0] ),
        vertex( [ 1.0, -1.0, 1.0, 1.0  ],normal=  [ 0.0, 0.0, 1.0 ],uv=[1.0,0.0] ),
        vertex( [ 1.0, 1.0, 1.0, 1.0  ], normal= [ 0.0, 0.0, 1.0 ],uv=[0.0,1.0] ),
        vertex( [ -1.0, 1.0, 1.0, 1.0  ],normal=  [ 0.0, 0.0, 1.0 ],uv=[1.0,1.0] ),]#23
    ib=[
        #3,1,0,
        #2,1,3,

        #6,4,5,
        #7,4,6,

        #11,9,8,
        #10,9,11,

        14,12,13,
        15,12,14,

        19,17,16,
        18,17,19,

        #22,20,21,
       # 23,20,22
        ]

    img = plt.imread("slonik_tekst.jpg")
    #plt.imshow(img[0:512,0:512])
    #plt.show()
    
    #"""
    L1=light([0,0.5,-1.2],[-1,-1,1],[200,200,200],"parell")
    #L2=light([2,4,-4],[2,1,-1],[200,200,200],"spot")

    
    device = context([200,200],[3,3],[0,0])
    device.setvertex(vb)
    device.setindex(ib)
    device.inputlayout(1,0,1,1)
    device.setlight([L1])
    #device.set_mode("line")
    device.set_farest_plane(100)
    #device.geometrysh.setlootat([0.0,0.0,0.0])
    #device.geometrysh.setCamera([2.0,2.0,-2.0])
    device.geometrysh.setlootat([0.0,0.0,0.0])
    device.geometrysh.setCamera([2.0,2.0,-2.0])
    device.pixelsh.setTex(img)
    device.run()
    device.show()
    #"""