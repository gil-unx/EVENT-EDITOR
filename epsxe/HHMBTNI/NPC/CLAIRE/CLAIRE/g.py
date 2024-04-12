import json,struct,os,glob
from PIL import Image
cwd = os.getcwd()
for jsonName in glob.glob("0014/BINARY/*.bin"):
    f =open(jsonName,"rb")
    f.seek(4)
    size = struct.unpack("H",f.read(2))[0]
    f.seek(12)
    dat = f.read()
    if size != len(dat):
        print(jsonName)
        os.system( "RLE.exe {0} -".format(jsonName))
          
 