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
["[{0E2B}]","[{ICON_MARY_HEART}]\n"],
["[{0E2C}]","[{ICON_ELLI_HEART}]\n"],
["[{0E2D}]","[{ICON_ANN_HEART}]\n"],
["[{0E2E}]","[{ICON_KAREN_HEART}]\n"],
["[{0E2F}]","[{ICON_ARROW}]\n"],
["[{400A}]","[{MC_NAME}]"],
["[{0EED}]","[{ANN_FEST_MARAH}]"],
["[{0EEE}]","[{ANN_FEST_BIASA}]"],
["[{0EEF}]","[{ANN_NIKAH}]"],
["[{0FC2}]","[{ANN_CINTA}]"],
["[{0FC3}]","[{ANN_KAGET}]"],
["[{0FC4}]","[{ANN_MIKIR}]"],
["[{0FC5}]","[{ANN_TSUNDERE}]"],
["[{0FC6}]","[{ANN_HEHE}]"],
["[{0FC7}]","[{ANN_NANGIS}]"],
["[{0FC8}]","[{ANN_MARAH}]"],
["[{0FC9}]","[{ANN_SENANG}]"],
["[{0FCA}]","[{ANN_BIASA}]"],
["[{0F9C}]","[{ANNA_MIKIR}]"],
["[{0F9D}]","[{ANNA_SEDIH}]"],
["[{0F9E}]","[{ANNA_MARAH}]"],
["[{0F9F}]","[{ANNA_SENANG}]"],
["[{0FA0}]","[{ANNA_BIASA}]"],
["[{0F1C}]","[{BAYI_MIKIR}]"],
["[{0F1D}]","[{BAYI_SEDIH}]"],
["[{0F1E}]","[{BAYI_MARAH}]"],
["[{0F1F}]","[{BAYI_SENANG}]"],
["[{0F20}]","[{BAYI_BIASA}]"],
["[{0F8D}]","[{BARLEY_MIKIR}]"],
["[{0F8E}]","[{BARLEY_SEDIH}]"],
["[{0F8F}]","[{BARLEY_MARAH}]"],
["[{0F90}]","[{BARLEY_SENANG}]"],
["[{0F91}]","[{BARLEY_BIASA}]"],
["[{0FA1}]","[{BASIL_MARAH}]"],
["[{0FA2}]","[{BASIL_SEDIH}]"],
["[{0FA4}]","[{BASIL_SENANG}]"],
["[{0FA5}]","[{BASIL_BIASA}]"],
["[{0FAD}]","[{CARTER_MIKIR}]"],
["[{0FAE}]","[{CARTER_SEDIH}]"],
["[{0FAF}]","[{CARTER_MARAH}]"],
["[{0FB0}]","[{CARTER_SENANG}]"],
["[{0FB1}]","[{CARTER_BIASA}]"],
["[{0FA6}]","[{CLIFF_HALU}]"],
["[{0FA7}]","[{CLIFF_PANIK}]"],
["[{0FA8}]","[{CLIFF_MARAH}]"],
["[{0FA9}]","[{CLIFF_SEDIH}]"],
["[{0FAA}]","[{CLIFF_TEKAD}]"],
["[{0FAB}]","[{CLIFF_SENANG}]"],
["[{0FAC}]","[{CLIFF_BIASA}]"],
["[{0EE1}]","[{DOKTER_NIKAH}]"],
["[{0FBC}]","[{DOKTER_MARAH}]"],
["[{0FBD}]","[{DOKTER_MIKIR}]"],
["[{0FBE}]","[{DOKTER_SEDIH}]"],
["[{0FC0}]","[{DOKTER_SENANG}]"],
["[{0FC1}]","[{DOKTER_BIASA}]"],
["[{0FCB}]","[{DOUG_MIKIR}]"],
["[{0FCC}]","[{DOUG_SEDIH}]"],
["[{0FCD}]","[{DOUG_MARAH}]"],
["[{0FCE}]","[{DOUG_SENANG}]"],
["[{0FCF}]","[{DOUG_BIASA}]"],
["[{0F68}]","[{DUKE_KAGET}]"],
["[{0F69}]","[{DUKE_MIKIR}]"],
["[{0F6A}]","[{DUKE_SEDIH}]"],
["[{0F6B}]","[{DUKE_MARAH}]"],
["[{0F6C}]","[{DUKE_SENANG}]"],
["[{0F6D}]","[{DUKE_BIASA}]"],
["[{0F5E}]","[{ELLEN_SEDIH}]"],
["[{0F61}]","[{ELLEN_SENANG}]"],
["[{0F62}]","[{ELLEN_BIASA}]"],
["[{0EE6}]","[{ELLI_FEST_MARAH}]"],
["[{0EE7}]","[{ELLI_FEST_BIASA}]"],
["[{0EE8}]","[{ELLI_NIKAH}]"],
["[{0FB2}]","[{ELLI_MIKIR}]"],
["[{0FB3}]","[{ELLI_SEDIH}]"],
["[{0FB4}]","[{ELLI_KAGET}]"],
["[{0FB5}]","[{ELLI_CINTA}]"],
["[{0FB6}]","[{ELLY_TSUNDERE}]"],
["[{0FB7}]","[{ELLI_NANGIS}]"],
["[{0FB8}]","[{ELLI_MARAH}]"],
["[{0FB9}]","[{ELLI_SENANG}]"],
["[{0FBA}]","[{ELLI_BIASA}]"],
["[{0F59}]","[{GOTZ_MIKIR}]"],
["[{0F5A}]","[{GOTZ_SEDIH}]"],
["[{0F5B}]","[{GOTZ_MARAH}]"],
["[{0F5C}]","[{GOTZ_SENANG}]"],
["[{0F5D}]","[{GOTZ_BIASA}]"],
["[{0F37}]","[{GOURMET_PANIK}]"],
["[{0F3A}]","[{GOURMET_MARAH}]"],
["[{0F3B}]","[{GOURMET_SENANG}]"],
["[{0F3C}]","[{GOURMET_BIASA}]"],
["[{0EE2}]","[{GRAY_NIKAH}]"],
["[{0FD0}]","[{GRAY_HALU}]"],
["[{0FD1}]","[{GRAY_MALU}]"],
["[{0FD2}]","[{GRAY_KAGET}]"],
["[{0FD3}]","[{GRAY_TSUNDERE}]"],
["[{0FD4}]","[{GRAY_MIKIR}]"],
["[{0FD5}]","[{GRAY_MARAH}]"],
["[{0FD6}]","[{GRAY_SENANG}]"],
["[{0FD7}]","[{GRAY_BIASA}]"],
["[{0F2D}]","[{GREG_MIKIR}]"],
["[{0F2E}]","[{GREG_SEDIH}]"],
["[{0F2F}]","[{GREG_MARAH}]"],
["[{0F30}]","[{GREG_SENANG}]"],
["[{0F31}]","[{GREG_BIASA}]"],
["[{0F28}]","[{DEWI_MARAH}]"],
["[{0F2B}]","[{DEWI_SENANG}]"],
["[{0F2C}]","[{DEWI_BIASA}]"],
["[{0EF3}]","[{KAPPA}]"],
["[{0EFA}]","[{KURCACIHIJAU_NO}]"],
["[{0EFD}]","[{KURCACIHIJAU_YES}]"],
["[{0EFF}]","[{KURCACIOREN_NO}]"],
["[{0F02}]","[{KURCACIOREN_YES}]"],
["[{0F04}]","[{KURCACIBIRUMUDA_NO}]"],
["[{0F07}]","[{KURCACIBIRUMUDA_YES}]"],
["[{0F09}]","[{KURCACIUNGU_NO}]"],
["[{0F0C}]","[{KURCACIUNGU_YES}]"],
["[{0F0E}]","[{KURCACIKUNING_NO}]"],
["[{0F11}]","[{KURCACIKUNING_YES}]"],
["[{0F13}]","[{KURCACIBIRU_NO}]"],
["[{0F16}]","[{KURCACIBIRU_YES}]"],
["[{0F48}]","[{KURCACIMERAH_NO}]"],
["[{0F4B}]","[{KURCACIMERAH_YES}]"],
["[{0F42}]","[{HARRIS_MIKIR}]"],
["[{0F43}]","[{HARRIS_SEDIH}]"],
["[{0F44}]","[{HARRIS_MARAH}]"],
["[{0F45}]","[{HARRIS_SENANG}]"],
["[{0F46}]","[{HARRIS_BIASA}]"],
["[{0FEA}]","[{JEFF_AKTING}]"],
["[{0FEB}]","[{JEFF_MIKIR}]"],
["[{0FEC}]","[{JEFF_SEDIH}]"],
["[{0FED}]","[{JEFF_MARAH}]"],
["[{0FEE}]","[{JEFF_SENANG}]"],
["[{0FEF}]","[{JEFF_BIASA}]"],
["[{0EDE}]","[{KAI_NIKAH_KAGUM}]"],
["[{0EDF}]","[{KAI_NIKAH_BIASA}]"],
["[{0F51}]","[{KAI_SENANG}]"],
["[{0F52}]","[{KAI_KAGUM}]"],
["[{0F53}]","[{KAI_MIKIR}]"],
["[{0F54}]","[{KAI_SEDIH}]"],
["[{0F55}]","[{KAI_MARAH}]"],
["[{0F57}]","[{KAI_BIASA}]"],
["[{0F3D}]","[{KANO_MIKIR}]"],
["[{0F3E}]","[{KANO_SEDIH}]"],
["[{0F40}]","[{KANO_SENANG}]"],
["[{0F41}]","[{KANO_BIASA}]"],
["[{0EF0}]","[{KAREN_FEST_MARAH}]"],
["[{0EF1}]","[{KAREN_FEST_BIASA}]"],
["[{0EF2}]","[{KAREN_NIKAH}]"],
["[{0FDD}]","[{KAREN_MIKIR}]"],
["[{0FDE}]","[{KAREN_KAGET}]"],
["[{0FDF}]","[{KAREN_CINTA}]"],
["[{0FE0}]","[{KAREN_KECEWA}]"],
["[{0FE1}]","[{KAREN_NANGIS}]"],
["[{0FE2}]","[{KAREN_MARAH}]"],
["[{0FE3}]","[{KAREN_SENANG}]"],
["[{0FE4}]","[{KAREN_BIASA}]"],
["[{0F7E}]","[{LILIA_MIKIR}]"],
["[{0F7F}]","[{LILIA_SEDIH}]"],
["[{0F80}]","[{LILIA_MARAH}]"],
["[{0F81}]","[{LILIA_SENANG}]"],
["[{0F82}]","[{LILIA_BIASA}]"],
["[{0F33}]","[{LOUISE_SEDIH}]"],
["[{0F35}]","[{LOUISE_SENANG}]"],
["[{0F36}]","[{LOUISE_BIASA}]"],
["[{0F63}]","[{MANNA_MIKIR}]"],
["[{0F64}]","[{MANNA_SEDIH}]"],
["[{0F65}]","[{MANNA_MARAH}]"],
["[{0F66}]","[{MANNA_SENANG}]"],
["[{0F67}]","[{MANNA_BIASA}]"],
["[{0EE9}]","[{MARRY_FEST_MARAH}]"],
["[{0EEB}]","[{MARRY_FEST_BIASA}]"],
["[{0EEC}]","[{MARRY_NIKAH}]"],
["[{0F92}]","[{MARRY_MIKIR}]"],
["[{0F93}]","[{MARRY_DILEMA}]"],
["[{0F94}]","[{MARRY_RAGU}]"],
["[{0F95}]","[{MARRY_KAGET}]"],
["[{0F96}]","[{MARRY_CINTA}]"],
["[{0F97}]","[{MARRY_KECEWA}]"],
["[{0F98}]","[{MARRY_BERLINANG}]"],
["[{0F99}]","[{MARRY_MARAH}]"],
["[{0F9A}]","[{MARRY_SENANG}]"],
["[{0F9B}]","[{MARRY_BIASA}]"],
["[{0F88}]","[{MAY_MIKIR}]"],
["[{0F89}]","[{MAY_SEDIH}]"],
["[{0F8A}]","[{MAY_MARAH}]"],
["[{0F8B}]","[{MAY_SENANG}]"],
["[{0F8C}]","[{MAY_BIASA}]"],
["[{0EE3}]","[{POPURI_FEST_MARAH}]"],
["[{0EE4}]","[{POPURI_FEST_BIASA}]"],
["[{0EE5}]","[{POPURI_NIKAH}]"],
["[{0F6E}]","[{POPURI_HABISNANGIS}]"],
["[{0F6F}]","[{POPURI_NANGIS}]"],
["[{0F70}]","[{POPURI_TSUNDERE}]"],
["[{0F71}]","[{POPURI_CINTA}]"],
["[{0F72}]","[{POPURI_MIKIR}]"],
["[{0F73}]","[{POPURI_SEDIH}]"],
["[{0F74}]","[{POPURI_MARAH}]"],
["[{0F75}]","[{POPURI_SENANG}]"],
["[{0F76}]","[{POPURI_BIASA}]"],
["[{0EE0}]","[{RICK_NIKAH}]"],
["[{0F77}]","[{RICK_KESAL}]"],
["[{0F78}]","[{RICK_KAGET}]"],
["[{0F79}]","[{RICK_MIKIR}]"],
["[{0F7A}]","[{RICK_SEDIH}]"],
["[{0F7B}]","[{RICK_MARAH}]"],
["[{0F7C}]","[{RICK_SENANG}]"],
["[{0F7D}]","[{RICK_BIASA}]"],
["[{0FD8}]","[{SAIBARA_MIKIR}]"],
["[{0FD9}]","[{SAIBARA_SEDIH}]"],
["[{0FDA}]","[{SAIBARA_MARAH}]"],
["[{0FDB}]","[{SAIBARA_SENANG}]"],
["[{0FDC}]","[{SAIBARA_BIASA}]"],
["[{0FE5}]","[{SASHA_MIKIR}]"],
["[{0FE6}]","[{SASHA_SEDIH}]"],
["[{0FE7}]","[{SASHA_MARAH}]"],
["[{0FE8}]","[{SASHA_SENANG}]"],
["[{0FE9}]","[{SASHA_BIASA}]"],
["[{0F21}]","[{STU_HABISNANGIS}]"],
["[{0F22}]","[{STU_NANGIS}]"],
["[{0F23}]","[{STU_MIKIR}]"],
["[{0F24}]","[{STU_SEDIH}]"],
["[{0F25}]","[{STU_MARAH}]"],
["[{0F26}]","[{STU_SENANG}]"],
["[{0F27}]","[{STU_BIASA}]"],
["[{0F83}]","[{THOMAS_MIKIR}]"],
["[{0F84}]","[{THOMAS_SEDIH}]"],
["[{0F85}]","[{THOMAS_MARAH}]"],
["[{0F86}]","[{THOMAS_SENANG}]"],
["[{0F87}]","[{THOMAS_BIASA}]"],
["[{0EF4}]","[{WON_MARAH}]"],
["[{0EF7}]","[{WON_SENANG}]"],
["[{0EF8}]","[{WON_BIASA}]"],
["[{0F4C}]","[{ZACK_MIKIR}]"],
["[{0F4D}]","[{ZACK_SEDIH}]"],
["[{0F4E}]","[{ZACK_MARAH}]"],
["[{0F4F}]","[{ZACK_SENANG}]"],
["[{0F50}]","[{ZACK_BIASA}]"],
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
            fileSave(faceData,messName[:-12]+"/FACEDATA/{0:04X}.bin".format(cc))
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
                f.seek(-4,1)
                f.write(faceD.read())
                print("Sip")
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
if __name__ == "__main__":
   insertText()
    
        
    