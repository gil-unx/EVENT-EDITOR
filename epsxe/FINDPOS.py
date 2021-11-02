import struct
import zlib,io
def decompress(data):
	return zlib.decompress(data[0xa:],-15)
def findPos():
	dat = io.BytesIO(decompress(open("sstates/SLUS_011.15.000","rb").read()))
	dat.seek(0x71cba)
	
	xpos = struct.unpack("<i",dat.read(4))[0]
	zpos = struct.unpack("<i",dat.read(4))[0]
	ypos = struct.unpack("<i",dat.read(4))[0]
	print("(Z{0}),(X{1}),(Y{2}),".format(zpos,xpos,ypos))
	
	
findPos()
