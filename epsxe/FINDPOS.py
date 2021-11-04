import struct
import gzip,io
def findPos():
	dec = gzip.decompress(open("sstates/SLUS_011.15.004","rb").read())
	dat = io.BytesIO(dec)
	dat.seek(0x71cba)
	xpos = struct.unpack("<i",dat.read(4))[0]
	zpos = struct.unpack("<i",dat.read(4))[0]
	ypos = struct.unpack("<i",dat.read(4))[0]
	print("(Z{0}),(X{1}),(Y{2}),".format(zpos,xpos,ypos))
	
findPos()
