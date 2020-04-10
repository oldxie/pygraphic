from Image import *
from component import *
from device import *

if __name__=="__main__":
    
    #vb=loadfromobj('./rabbit.obj')
    vb=[		vertex( [ -1.0, 1.0, -1.0, 1.0 ], normal=[ 0.0, 1.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, -1.0, 1.0 ],normal= [ 0.0, 1.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, 1.0, 1.0  ], normal=[ 0.0, 1.0, 0.0 ] ),
        vertex( [ -1.0, 1.0, 1.0, 1.0  ], normal=[ 0.0, 1.0, 0.0 ] ),

        vertex( [ -1.0, -1.0, -1.0, 1.0  ],normal= [ 0.0, -1.0, 0.0 ] ),
        vertex( [ 1.0, -1.0, -1.0, 1.0  ],normal= [ 0.0, -1.0, 0.0 ] ),
        vertex( [ 1.0, -1.0, 1.0, 1.0  ],normal= [ 0.0, -1.0, 0.0 ] ),
        vertex( [ -1.0, -1.0, 1.0, 1.0  ], normal=[ 0.0, -1.0, 0.0 ] ),

        vertex( [ -1.0, -1.0, 1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ] ),
        vertex( [ -1.0, -1.0, -1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ] ),
        vertex( [ -1.0, 1.0, -1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ] ),
        vertex( [ -1.0, 1.0, 1.0, 1.0  ],normal= [ -1.0, 0.0, 0.0 ] ),

        vertex( [ 1.0, -1.0, 1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ] ),
        vertex( [ 1.0, -1.0, -1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, -1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, 1.0, 1.0  ],normal= [ 1.0, 0.0, 0.0 ] ),

        vertex( [ -1.0, -1.0, -1.0, 1.0  ], normal= [ 0.0, 0.0, -1.0 ] ),
        vertex( [ 1.0, -1.0, -1.0, 1.0  ],normal=  [ 0.0, 0.0, -1.0 ] ),
        vertex( [ 1.0, 1.0, -1.0, 1.0  ],normal=  [ 0.0, 0.0, -1.0 ] ),
        vertex( [ -1.0, 1.0, -1.0, 1.0  ],normal=  [ 0.0, 0.0, -1.0 ] ),

        vertex( [ -1.0, -1.0, 1.0, 1.0  ], normal= [ 0.0, 0.0, 1.0 ] ),
        vertex( [ 1.0, -1.0, 1.0, 1.0  ],normal=  [ 0.0, 0.0, 1.0 ] ),
        vertex( [ 1.0, 1.0, 1.0, 1.0  ], normal= [ 0.0, 0.0, 1.0 ] ),
        vertex( [ -1.0, 1.0, 1.0, 1.0  ],normal=  [ 0.0, 0.0, 1.0 ] ),]#7
    ib=[
        3,1,0,
        2,1,3,

        6,4,5,
        7,4,6,

        11,9,8,
        10,9,11,

        14,12,13,
        15,12,14,

        19,17,16,
        18,17,19,

        22,20,21,
        23,20,22
        ]
    #img = plt.imread("rabbit_texture.png")


    L1=light([0,0.5,-1.2],[-2,-1,-1],[200,200,200],"parell")
    #L2=light([2,4,-4],[2,1,-1],[200,200,200],"spot")

    
    device = context([400,400],[5,5],[0,0])
    device.setvertex(vb)
    device.setindex(ib)
    device.inputlayout(1,0,1,0)
    device.setlight([L1])
    #device.set_mode("line")
    device.set_farest_plane(100)
    device.geometrysh.setlootat([0.0,0.0,0.0])
    device.geometrysh.setCamera([2.0,2.0,-2.0])
    #device.geometrysh.setlootat([0.0,0.0,15])
    #device.geometrysh.setCamera([18.0,-16.0,35.0])
    #device.pixelsh.setTex(img)
    device.run()
    device.show()