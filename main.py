from Image import *
from vertex import *
from rasterizaton import *
if __name__=="__main__":
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
    device = context([400,400],[4,4])
    device.setvertex(vb)
    device.setindex(ib)
    device.set_farest_plane(100)
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