
import os
#------------------------------------------------------------------------------------------------------
k = input("FIND STRING : ")
k = k.encode("utf-8")
for root, dirs, files in os.walk("HHMBTNI/MESSEGE/", topdown = False):
   for file in files:
    name = os.path.join(root, file)
    #rint(file)
    f =open(name, 'rb')
    s= f.read()
    p = s.find(k)
    x = int(p)
    if p != -1:
        f.seek(x,0)
        print("{0:08X}".format(x))
        string = f.read(100).replace(b'\x00', b'\n----------------------------\n').decode('utf-8','backslashreplace')
        print ("NAME_FILE=",name)
        print(string)
