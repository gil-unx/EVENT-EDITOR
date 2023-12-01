import struct
import gzip,io,os
def printPos(index ):
    dec = gzip.decompress(open("sstates/SLUS_011.15.{0:03d}".format(index),"rb").read())
    dat = io.BytesIO(dec)
    dat.seek(0x71cba)
    xpos = struct.unpack("<i",dat.read(4))[0]
    zpos = struct.unpack("<i",dat.read(4))[0]
    ypos = struct.unpack("<i",dat.read(4))[0]
    print("Save State {3}>>(Z{0}) (X{1}) (Y{2})".format(zpos,xpos,ypos,index+1))
    
def findPos():
    for i in range(5):
        try:
            printPos(i)
        except FileNotFoundError:
            continue
        
findPos()
