from Image import *
from component import *
from device import *

if __name__=="__main__":
    vb=[		vertex( [ -1.0, 1.0, -1.0 ], normal=[ 0.0, 1.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, -1.0 ],normal= [ 0.0, 1.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, 1.0 ], normal=[ 0.0, 1.0, 0.0 ] ),
        vertex( [ -1.0, 1.0, 1.0 ], normal=[ 0.0, 1.0, 0.0 ] ),

        vertex( [ -1.0, -1.0, -1.0 ],normal= [ 0.0, -1.0, 0.0 ] ),
        vertex( [ 1.0, -1.0, -1.0 ],normal= [ 0.0, -1.0, 0.0 ] ),
        vertex( [ 1.0, -1.0, 1.0 ],normal= [ 0.0, -1.0, 0.0 ] ),
        vertex( [ -1.0, -1.0, 1.0 ], normal=[ 0.0, -1.0, 0.0 ] ),

        vertex( [ -1.0, -1.0, 1.0 ],normal= [ -1.0, 0.0, 0.0 ] ),
        vertex( [ -1.0, -1.0, -1.0 ],normal= [ -1.0, 0.0, 0.0 ] ),
        vertex( [ -1.0, 1.0, -1.0 ],normal= [ -1.0, 0.0, 0.0 ] ),
        vertex( [ -1.0, 1.0, 1.0 ],normal= [ -1.0, 0.0, 0.0 ] ),

        vertex( [ 1.0, -1.0, 1.0 ],normal= [ 1.0, 0.0, 0.0 ] ),
        vertex( [ 1.0, -1.0, -1.0 ],normal= [ 1.0, 0.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, -1.0 ],normal= [ 1.0, 0.0, 0.0 ] ),
        vertex( [ 1.0, 1.0, 1.0 ],normal= [ 1.0, 0.0, 0.0 ] ),

        vertex( [ -1.0, -1.0, -1.0 ], normal= [ 0.0, 0.0, -1.0 ] ),
        vertex( [ 1.0, -1.0, -1.0 ],normal=  [ 0.0, 0.0, -1.0 ] ),
        vertex( [ 1.0, 1.0, -1.0 ],normal=  [ 0.0, 0.0, -1.0 ] ),
        vertex( [ -1.0, 1.0, -1.0 ],normal=  [ 0.0, 0.0, -1.0 ] ),

        vertex( [ -1.0, -1.0, 1.0 ], normal= [ 0.0, 0.0, 1.0 ] ),
        vertex( [ 1.0, -1.0, 1.0 ],normal=  [ 0.0, 0.0, 1.0 ] ),
        vertex( [ 1.0, 1.0, 1.0 ], normal= [ 0.0, 0.0, 1.0 ] ),
        vertex( [ -1.0, 1.0, 1.0 ],normal=  [ 0.0, 0.0, 1.0 ] ),]#7
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
    
    L1=light([2,2,2],[-2,-1,-1],[244,0,0])

    device = context([400,400],[4,4])
    device.setvertex(vb)
    device.setindex(ib)
    device.setlight([L1])
    device.set_farest_plane(100)
    device.geometrysh.setlootat([0.5,0.5,0.5])
    device.geometrysh.setCamera([1.5,1.5,-1.5])
    device.run()
    device.show()