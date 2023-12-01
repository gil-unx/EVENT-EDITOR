from FUN import *
import struct
iso = open("isos/HHMBTNI_BASE.iso","r+b")
for mapName in TRIGGER_POS:
    iso.seek(TRIGGER_POS[mapName])
    iso.write(struct.pack("10i",65535,0,0,0,0,0,0,0,0,0))
print("Trigger cleaned!!!")
input()
