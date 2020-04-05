from Image import *
from component import *
from device import *

#if __name__=="__main__":
def cube_parell_light():    
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

    L1=light([0,0.5,-1.2],[-2,-1,-1],[200,200,200],"parell")
  
    device = context([400,400],[5,5],[0,0])
    device.setvertex(vb)
    device.setindex(ib)
    device.inputlayout(1,0,1,0)
    device.setlight([L1])
    device.set_farest_plane(100)
    device.geometrysh.setlootat([0.0,0.0,0.0])
    device.geometrysh.setCamera([2.0,2.0,-2.0])
    device.run()
    device.show()

def cube_parell_light_cut():    
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

    L1=light([0,0.5,-1.2],[-2,-1,-1],[200,200,200],"parell")
  
    device = context([400,400],[5,5],[2,0])
    device.setvertex(vb)
    device.setindex(ib)
    device.inputlayout(1,0,1,0)
    device.setlight([L1])
    device.set_farest_plane(100)
    device.geometrysh.setlootat([0.0,0.0,0.0])
    device.geometrysh.setCamera([2.0,2.0,-2.0])
    device.run()
    device.show()

def cube_texture():
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

    img = plt.imread("./model/slonik_tekst.jpg")
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

def cube_blend_2():
    vb=[vertex([0,1,0],[255,0,0]), #0
        vertex([1,1,0],[0,255,0]),#1
        vertex([1,1,1],[0,0,255]),#2
        vertex([0,1,1],[255,0,255]),#3
        vertex([0,0,0],[0,255,255]),#4
        vertex([1,0,0],[255,255,0]),#5
        vertex([1,0,1],[255,255,255]),#6
        vertex([0,0,1],[0,0,0]),]#7
    ib=[
        3,1,0,
        2,1,3,

        0,5,4,
        1,5,0,

        3,4,7,
        0,4,3,

        1,6,5,
        2,6,1,

        2,7,6,
        3,7,2,

        6,4,5,
        7,4,6
        ]
    ib_dbtest=[1,5,0,
               ]
    
    #tri1=triangle([v0,v1,v2])
    #vec1=
    #ib.reverse()
    device = context([400,400],[4,4],[0,0])
    device.setvertex(vb)
    device.setindex(ib)
    device.set_farest_plane(100)
    device.inputlayout(1,1,0,0)
    device.geometrysh.setlootat([0.5,0.5,0.5])
    device.geometrysh.setCamera([1.5,1.5,-1.5])
    #device.mode="line"
    #device.creatwindow([255,255,255])
    device.run()

    vb[0].color=[255,255,255]
    vb[2].color=[255,255,255]
    vb[6].color=[255,255,255]
    vb[7].color=[255,255,255]
    db2=[0,2,6,
         0,6,4]
    device.blendmode="Additive"
    device.setvertex(vb)
    device.setindex(db2)
    db2=[2,6,3]
    device.run()
    device.show()



def cube_parell_light_ani():    
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

    L1=light([0,0.5,-1.2],[-2,-1,-1],[100,100,100],"parell")
  
    device = context([400,400],[5,5],[0,0])
    device.setvertex(vb)
    device.setindex(ib)
    device.inputlayout(1,0,1,0)
    device.setlight([L1])
    device.set_farest_plane(100)
    device.geometrysh.setlootat([0.0,0.0,0.0])
    device.geometrysh.setCamera([2.0,2.0,-2.0])
    device.runani()
    device.showani()