import json,struct,os,glob
from PIL import Image
cwd = os.getcwd()
for jsonName in glob.glob("NPC/*/BINARY/*.bin"):
    f =open(jsonName,"rb")
    size = struct.unpack("H",f.read(2))[0]
    f.seek(12)
    dat = f.read()
    if size != len(dat):
        print(jsonName)
        os.system( "{0}\\RLE.exe {0}\\{1} -".format( cwd,jsonName))
          
 