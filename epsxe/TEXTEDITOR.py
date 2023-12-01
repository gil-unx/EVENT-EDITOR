from FUN import *
table ={0x0000:"A",
0x0001:"B",
0x0002:"C",
0x0003:"D",
0x0004:"E",
0x0005:"F",
0x0006:"G",
0x0007:"H",
0x0008:"I",
0x0009:"J",
0x000A:"K",
0x000B:"L",
0x000C:"M",
0x000D:"N",
0x000E:"O",
0x000F:"P",
0x0010:"Q",
0x0011:"R",
0x0012:"S",
0x0013:"T",
0x0014:"U",
0x0015:"V",
0x0016:"W",
0x0017:"X",
0x0018:"Y",
0x0019:"Z",
0x0020:"a",
0x0021:"b",
0x0022:"c",
0x0023:"d",
0x0024:"e",
0x0025:"f",
0x0026:"g",
0x0027:"h",
0x0028:"i",
0x0029:"j",
0x002A:"k",
0x002B:"l",
0x002C:"m",
0x002D:"n",
0x002E:"o",
0x002F:"p",
0x0030:"q",
0x0031:"r",
0x0032:"s",
0x0033:"t",
0x0034:"u",
0x0035:"v",
0x0036:"w",
0x0037:"x",
0x0038:"y",
0x0039:"z",
0x0040:"0",
0x0041:"1",
0x0042:"2",
0x0043:"3",
0x0044:"4",
0x0045:"5",
0x0046:"6",
0x0047:"7",
0x0048:"8",
0x0049:"9",
0x0050:"{'t}",
0x0051:"{'s}",
0x0052:"{'l}",
0x0053:"{'d}",
0x0054:"{'m}",
0x0055:"{'r}",
0x0056:"{'v}",
0x0057:"Ä",
0x0058:"Ö",
0x0059:"Ü",
0x005A:"ä",
0x005B:"ö",
0x005C:"ü",
0x005D:"β",
0x0062:"?",
0x0063:"!",
0x0064:"⋯",
0x0065:"·",
0x0066:":",
0x0067:";",
0x0068:"+",
0x0069:"-",
0x006A:"(",
0x006B:")",
0x006C:".",
0x006D:"○",
0x006E:"×",
0x006F:"△",
0x0070:"□",
0x0071:"/",
0x0072:"▲",
0x0073:"▼",
0x0074:"~",
0x0075:"_",
0x0076:"&",
0x0077:"☆",
0x0078:"★",
0x0079:"❶",
0x007A:"❷",
0x007B:"❸",
0x007C:"❹",
0x007D:"❺",
0x007E:"❻",
0x007F:"…",
0x0080:"♡",
0x0081:"❤",
0x0087:"↙",
0x0088:"↖",
0x0089:"↗",
0x008A:"↘",
0x008B:"♛",
0x008C:",",
0x008D:"\'",
0x008E:"\"",
0x008F:"%",
0x0090:"👑",
0x0091:"⓷",
0x0092:"⓸",
0x0093:"⓹",
0x0094:"⓺",
0xfffe:"\n",
0x0ffd:" ",
0x0ffc:"[{PRESS}]",
0x0ffb:"[{CLEARBOX}]",
}
ctr_tbl =[
["[{0E2B}]","[{ICON_MARY_HEART}]"],
["[{0E2C}]","[{ICON_ELLI_HEART}]"],
["[{0E2D}]","[{ICON_ANN_HEART}]"],
["[{0E2E}]","[{ICON_KAREN_HEART}]"],
["[{0E2F}]","[{ICON_ARROW}]"],
["[{400A}]","[{MC_NAME}]"],
]
inv_table= {v: k for k, v in table.items()}
import glob,struct,sys
class String:
    def __init__(s,data,tbl):
        s.data = data
        s.tbl = tbl
    def encode(s):
        f = s.data
        tbl = s.tbl
        last = len(f)
        xIn = 0
        bs = Br(io.BytesIO(b""))
        while xIn < last:
            if xIn == last:
                break
            if (f[xIn] == "[") and (f[xIn+1] == "{"):
                if f[xIn:xIn+9] == "[{PRESS}]":
                    bs.writeUint16(tbl[f[xIn:xIn+9]])
                    xIn+=9
                elif f[xIn:xIn+12] == "[{CLEARBOX}]":
                    bs.writeUint16(tbl[f[xIn:xIn+12]])
                    xIn+=12
                else:
                    try:
                        bs.writeUint16(int(f[xIn+2:xIn+6],16))
                        xIn +=8
                    except:
                        print("UNKNOWN CRTL CODE!!")
                        print(f[xIn+2:xIn+6])
                        sys.exit()
            elif f[xIn] == "{":
                try:
                    c = f[xIn:xIn+4]
                    bs.writeUint16(tbl[c])
                    xIn+=4
                except:
                    try:
                        c = f[xIn:xIn+3]
                        bs.writeUint16(tbl[c])
                        xIn+=4
                    except:
                        print("SPESIAL CHAR RUSAK!!")
                        print(f[xIn:xIn+4])
                        sys.exit()
            else:
                try:
                    c = tbl[f[xIn]]
                    bs.writeUint16(c)
                    xIn+=1
                except:
                    print("UNKNOWN CHAR!!")
                    sys.exit()
        bs.writeUint16(0xffff)
        bsize = bs.tell()
        pad = 0x800-bs.getsize()
        bs.write(b"\x00"*pad)
        return bs.getdata(),bsize

def ex():
    for messName in glob.glob("HHMBTNI/MESSEGE/*.bin"):
        print(messName)
        f = open(messName, "rb")
        txt = io.StringIO()
        #txt = open(messName[:-3] + "txt", "w", encoding="utf-8")
        index = 0
        while faceData := f.read(0x1800):
        
            txt.write("[{0:04d}]\n".format(index))
            text = io.BytesIO(f.read(0x800))
            cc = struct.unpack("<H",  text.read(2))[0]
            text.seek(0)
            fileSave(faceData,messName[:-12]+"/FACEDATA/{0}.bin".format(cc))
            while d := text.read(2):
                c = struct.unpack("<H", d)[0]
                if c == 0xffff:
                    break

                try:
                    char = table[c]
                except:
                    char = "[{" + "{0:04X}".format(c) + "}]"
                txt.write(char)


            txt.write("\n---------------------------------------------\n")
            index += 1
        txt.seek(0,0)
        
        txtBuff = txt.read()
        for x in ctr_tbl:
            txtBuff = txtBuff.replace(x[0],x[1])
        outTxt = open(messName[:-3] + "txt", "w", encoding="utf-8").write(txtBuff)
def insertText():
    iso = open("isos/HHMBTNI_BASE.iso","r+b")
    messOff = [
        0x048DE138,
        0x059774B8,
        0x06BF5278 ,
        0x071CC6B8,
        0x07E4BF78 ,]
    i = 0
    for messName in glob.glob("HHMBTNI/MESSEGE/*.bin"):
    
        f = open(messName, "r+b")
        txtBuff = open(messName[:-3] + "txt", "r", encoding="utf-8").read()
        for x in ctr_tbl:
            txtBuff = txtBuff.replace(x[1],x[0])
        txt = Br(io.StringIO(txtBuff))
        index = 0
        while d := f.read(4):
            txt.readline()
            stringText = txt.rt()[:-1]
            cc = stringText[2:6]
            try:
                
                faceD = open(messName[:-12]+"/FACEDATA/{0}.bin".format(cc),"rb")
                faceD.seek(4)
                f.write(faceD.read())
            except:
                f.read(0x1800-4)
            bstring = String(stringText, inv_table)
            bstring, bsize = bstring.encode()
            f.write(bstring)
            index += 1
        f.seek(0,0)
        f.seek(0,0)
        iso.seek(messOff[i])
        while dat := f.read(0x800):
            iso.write(dat)
            iso.read(0x130)
        i+=1
    print("INSERT TEXT DONE!!!")
