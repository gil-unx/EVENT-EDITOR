import io,png,glob,os

class Br:
    def __init__(self,data):
        self.data = data
    def readUint8(self,endian="little"):
        return int.from_bytes(self.data.read(1), byteorder=endian, signed=False)
    def readUint16(self,endian="little"):
        return  int.from_bytes(self.data.read(2), byteorder=endian, signed=False)
    def readUint24(self,endian="little"):
        return  int.from_bytes(self.data.read(3), byteorder=endian, signed=False)
    def readUint32(self,endian="little"):
        return int.from_bytes(self.data.read(4), byteorder=endian, signed=False)
    def readInt8(self,endian="little"):
        return int.from_bytes(self.data.read(1), byteorder=endian, signed=True)
    def readInt16(self,endian="little"):
        return  int.from_bytes(self.data.read(2), byteorder=endian, signed=True)
    def readInt24(self,endian="little"):
        return  int.from_bytes(self.data.read(3), byteorder=endian, signed=True)
    def readInt32(self,endian="little"):
        return int.from_bytes(self.data.read(4), byteorder=endian, signed=True)
    def wpad(self,num,pad= b"\x00"):
        padding = num - (self.data.tell() % num or num)
        if padding:
            self.data.write(pad * padding)
        return 0
    def rpad(self,num,t=False):
        pos = self.data.tell()
        if t:
            pos = num
        padding = num - (pos % num or num)
        self.data.read(padding)
        return 0
    def getUtf8(self,offset=0):
        base = self.data.tell()
        if offset:
            self.data.seek(offset,0)
        chars = b""
        while True:
            c = self.data.read(1)
            if c == b"\x00":
                if offset:
                    self.data.seek(base,0)
                return chars.decode('utf-8')
            chars+=c
    def getUtf8B(self):

        chars = b""
        while True:
            c = self.data.read(1)
            if c == b"\x00":
                return chars
            chars+=c
    def getJis(self,offset=0):
        base = self.data.tell()
        if offset:
            self.data.seek(offset,0)
        chars = b""
        while True:
            c = self.data.read(1)
            if c == b"\x00":
                if offset:
                    self.data.seek(base,0)
                return chars.decode('shift-jis',"backslashreplace")
            chars+=c
    def getUtf16(self,offset):
        base = self.data.tell()
        self.data.seek(offset,0)
        chars = b""
        while True:
            c = self.data.read(2)
            if (c == b"\x00\x00") or (c == b"\xFF\xFF"):
                self.data.seek(base,0)
                return chars.decode('utf-16')
            chars+=c
    def getsize(self):
        pos = self.data.tell()
        self.data.seek(0,0)
        size = len(self.data.read())
        self.data.seek(pos,0)
        return size
    def getdata(self):
        pos = self.data.tell()
        self.data.seek(0,0)
        dat =self.data.read()
        self.data.seek(pos,0)
        return dat
    def getBytes(self,pos,size):
        base = self.data.tell()
        self.data.seek(pos,0)
        bin = self.data.read(size)
        self.data.seek(base,0)
        return bin
    def rt(self):
        text = []
        while True :
            c = self.data.readline()

            if c[:30] == "------------------------------":
                return "".join(text)

            text.append(c)
    def readline(self):
        data = self.data.readline()
        return data
    def seek(self,offset, origin=0):
        self.data.seek(offset,origin)
        return ""
    def tell(self):
        data = self.data.tell()
        return data
    def read(self,x=False):
        if x:
            output = self.data.read(x)
        else:
            output = self.data.read()
        return output
    def write(self,indata):
        self.data.write(indata)
        return ""
    def writeUint32B(self,x):
        self.data.write(x.to_bytes(4, byteorder="big", signed=False))
    def writeUint32(self,x):
        self.data.write(x.to_bytes(4, byteorder='little', signed=False))
    def writeUint16(self,x):
        self.data.write(x.to_bytes(2, byteorder='little', signed=False))
    def writeUint8(self,x):
        self.data.write(x.to_bytes(1, byteorder="big", signed=False))
    def writeintB(self,x,y):
        self.data.write(x.to_bytes(y, byteorder="big", signed=False))
    def writeInt16(self,x):
        self.data.write(x.to_bytes(2, byteorder='little', signed=True))

    def close(self):
        self.data.close()
        return ""
def globList(path):
    files = glob.glob(path)
    return files
def fileSave(data,name):
    os.makedirs(os.path.dirname(name), exist_ok=True)
    output = open(name, "wb")
    output.write(data)


class Pal:
    def __init__(self,data):
        self.data = Br(io.BytesIO(data))
        self.total = len(data)//2

    def getpal(self):
        f = self.data
        total =self.total
        ray = []
        tab = {0: 0x00,
               1: 0x08,
               2: 0x10,
               3: 0x18,
               4: 0x21,
               5: 0x29,
               6: 0x31,
               7: 0x39,
               8: 0x42,
               9: 0x4A,
               10: 0x52,
               11: 0x5A,
               12: 0x63,
               13: 0x6B,
               14: 0x73,
               15: 0x7B,
               16: 0x84,
               17: 0x8C,
               18: 0x94,
               19: 0x9C,
               20: 0xA5,
               21: 0xAD,
               22: 0xB5,
               23: 0xBD,
               24: 0xC6,
               25: 0xCE,
               26: 0xD6,
               27: 0xDE,
               28: 0xE7,
               29: 0xEF,
               30: 0xF7,
               31: 0xFF,
               }
        for x in range(total):
            p = f.readUint16()
            blue = tab[(p & 0x7fff) >> 10]
            green = tab[(p & 0x3ff) >> 5]
            red = tab[(p & 0x1f)]
            alpha = (p >> 15) * 255
            ray.append((red,green,blue,alpha),)
        return  ray

class Tile:
    def __init__(self,data,w,h):
        self.data = Br(io.BytesIO(data))
        self.size = len(data)
        self.w = w
        self.h = h
        self.tile = Br(io.BytesIO(data))

    def getpng(self,pal):
        h =self.h
        w = self.w
        f = self.tile
        s =[]
        for x in range(h):
            ww = []
            for y in range(w):
                ww.append(f.readUint8())
            s.append(ww)
        tmp =png.Writer(len(s[0]), len(s), palette=pal, bitdepth=8)
        f = Br(io.BytesIO(b''))
        tmp.write(f, s)
        return f.getdata()

class Tile4:
     def __init__(self,data,info):
         self.data = Br(io.BytesIO(data))
         self.size = len(data)
         self.w = info[2]<<2
         self.h = info[3]
         self.tile = Br(io.BytesIO(data))

     def getpng(self,pal):
        w = self.w
        h = self.h
        f = self.tile
        f.seek(0,0)
        s =[]
        for x in range(h):
            ww = []
            for y in range(w//2):
                c = f.readUint8()
                ww.append(c & 0x0f)
                ww.append((c & 0xf0)>>4)
            s.append(ww)
        tmp =png.Writer(len(s[0]), len(s), palette=pal, bitdepth=4)
        f = Br(io.BytesIO(b''))
        tmp.write(f, s)
        return f.getdata()
        
tabpal = {0x0: 0,
          0x1: 0,
          0x2: 0,
          0x3: 0,
          0x4: 0,
          0x5: 0,
          0x6: 0,
          0x7: 0,
          0x8: 1,
          0x9: 1,
          0xa: 1,
          0xb: 1,
          0xc: 1,
          0xd: 1,
          0xe: 1,
          0xf: 1,
          0x10: 2,
          0x11: 2,
          0x12: 2,
          0x13: 2,
          0x14: 2,
          0x15: 2,
          0x16: 2,
          0x17: 2,
          0x18: 3,
          0x19: 3,
          0x1a: 3,
          0x1b: 3,
          0x1c: 3,
          0x1d: 3,
          0x1e: 3,
          0x1f: 3,
          0x20: 4,
          0x21: 4,
          0x22: 4,
          0x23: 4,
          0x24: 4,
          0x25: 4,
          0x26: 4,
          0x27: 4,
          0x28: 4,
          0x29: 5,
          0x2a: 5,
          0x2b: 5,
          0x2c: 5,
          0x2d: 5,
          0x2e: 5,
          0x2f: 5,
          0x30: 5,
          0x31: 6,
          0x32: 6,
          0x33: 6,
          0x34: 6,
          0x35: 6,
          0x36: 6,
          0x37: 6,
          0x38: 6,
          0x39: 7,
          0x3a: 7,
          0x3b: 7,
          0x3c: 7,
          0x3d: 7,
          0x3e: 7,
          0x3f: 7,
          0x40: 7,
          0x41: 7,
          0x42: 8,
          0x43: 8,
          0x44: 8,
          0x45: 8,
          0x46: 8,
          0x47: 8,
          0x48: 8,
          0x49: 8,
          0x4a: 9,
          0x4b: 9,
          0x4c: 9,
          0x4d: 9,
          0x4e: 9,
          0x4f: 9,
          0x50: 9,
          0x51: 9,
          0x52: 10,
          0x53: 10,
          0x54: 10,
          0x55: 10,
          0x56: 10,
          0x57: 10,
          0x58: 10,
          0x59: 10,
          0x5a: 11,
          0x5b: 11,
          0x5c: 11,
          0x5d: 11,
          0x5e: 11,
          0x5f: 11,
          0x60: 11,
          0x61: 11,
          0x62: 11,
          0x63: 12,
          0x64: 12,
          0x65: 12,
          0x66: 12,
          0x67: 12,
          0x68: 12,
          0x69: 12,
          0x6a: 12,
          0x6b: 13,
          0x6c: 13,
          0x6d: 13,
          0x6e: 13,
          0x6f: 13,
          0x70: 13,
          0x71: 13,
          0x72: 13,
          0x73: 14,
          0x74: 14,
          0x75: 14,
          0x76: 14,
          0x77: 14,
          0x78: 14,
          0x79: 14,
          0x7a: 14,
          0x7b: 15,
          0x7c: 15,
          0x7d: 15,
          0x7e: 15,
          0x7f: 15,
          0x80: 15,
          0x81: 15,
          0x82: 15,
          0x83: 16,
          0x84: 16,
          0x85: 16,
          0x86: 16,
          0x87: 16,
          0x88: 16,
          0x89: 16,
          0x8a: 16,
          0x8b: 16,
          0x8c: 17,
          0x8d: 17,
          0x8e: 17,
          0x8f: 17,
          0x90: 17,
          0x91: 17,
          0x92: 17,
          0x93: 17,
          0x94: 18,
          0x95: 18,
          0x96: 18,
          0x97: 18,
          0x98: 18,
          0x99: 18,
          0x9a: 18,
          0x9b: 18,
          0x9c: 19,
          0x9d: 19,
          0x9e: 19,
          0x9f: 19,
          0xa0: 19,
          0xa1: 19,
          0xa2: 19,
          0xa3: 19,
          0xa4: 20,
          0xa5: 20,
          0xa6: 20,
          0xa7: 20,
          0xa8: 20,
          0xa9: 20,
          0xaa: 20,
          0xab: 20,
          0xac: 20,
          0xad: 21,
          0xae: 21,
          0xaf: 21,
          0xb0: 21,
          0xb1: 21,
          0xb2: 21,
          0xb3: 21,
          0xb4: 21,
          0xb5: 22,
          0xb6: 22,
          0xb7: 22,
          0xb8: 22,
          0xb9: 22,
          0xba: 22,
          0xbb: 22,
          0xbc: 22,
          0xbd: 23,
          0xbe: 23,
          0xbf: 23,
          0xc0: 23,
          0xc1: 23,
          0xc2: 23,
          0xc3: 23,
          0xc4: 23,
          0xc5: 24,
          0xc6: 24,
          0xc7: 24,
          0xc8: 24,
          0xc9: 24,
          0xca: 24,
          0xcb: 24,
          0xcc: 24,
          0xcd: 24,
          0xce: 25,
          0xcf: 25,
          0xd0: 25,
          0xd1: 25,
          0xd2: 25,
          0xd3: 25,
          0xd4: 25,
          0xd5: 25,
          0xd6: 26,
          0xd7: 26,
          0xd8: 26,
          0xd9: 26,
          0xda: 26,
          0xdb: 26,
          0xdc: 26,
          0xdd: 26,
          0xde: 27,
          0xdf: 27,
          0xe0: 27,
          0xe1: 27,
          0xe2: 27,
          0xe3: 27,
          0xe4: 27,
          0xe5: 27,
          0xe6: 28,
          0xe7: 28,
          0xe8: 28,
          0xe9: 28,
          0xea: 28,
          0xeb: 28,
          0xec: 28,
          0xed: 28,
          0xee: 28,
          0xef: 29,
          0xf0: 29,
          0xf1: 29,
          0xf2: 29,
          0xf3: 29,
          0xf4: 29,
          0xf5: 29,
          0xf6: 29,
          0xf7: 30,
          0xf8: 30,
          0xf9: 30,
          0xfa: 30,
          0xfb: 30,
          0xfc: 30,
          0xfd: 30,
          0xfe: 30,
          0xff: 31, }


mapdict = {
0x00:"MAP00",
0x01:"MAP01",
0x02:"MAP02",
0x03:"MAP03",
0x04:"MAP04",
0x05:"MAP05",
0x06:"MAP06",
0x07:"MAP07",
0x08:"FARM1SPRING",
0x09:"FARM1SUMMER",
0x0A:"FARM1FALL",
0x0B:"FARM1WINTER",
0x0C:"FARM2SPRING",
0x0D:"FARM2SUMMER",
0x0E:"FARM2FALL",
0x0F:"FARM2WINTER",
0x10:"FARM3SPRING",
0x11:"FARM3SUMMER",
0x12:"FARM3FALL",
0x13:"FARM3WINTER",
0x14:"FARM4SPRING",
0x15:"FARM4SUMMER",
0x16:"FARM4FALL",
0x17:"FARM4WINTER",
0x18:"MAPPOULTRYFAMSPRING",
0x19:"MAPPOULTRYFAMSUMMER",
0x1A:"MAPPOULTRYFAMFALL",
0x1B:"MAPPOULTRYFAMWINTER",
0x1C:"MAPYODELRANCHSPRING",
0x1D:"MAPYODELRANCHSUMMER",
0x1E:"MAPYODELRANCHFALL",
0x1F:"MAPYODELRANCHWINTER",
0x20:"MAPBLACKSMITHSPRING",
0x21:"MAPBLACKSMITHSUMMER",
0x22:"MAPBLACKSMITHFALL",
0x23:"MAPBLACKSMITHWINTER",
0x24:"MAPPERPUSSPRING",
0x25:"MAPPERPUSSUMMER",
0x26:"MAPPERPUSFALL",
0x27:"MAPPERPUSWINTER",
0x28:"MAPKLINIKSPRING",
0x29:"MAPKLINIKSUMMER",
0x2A:"MAPKLINIKFALL",
0x2B:"MAPKLINIKWINTER",
0x2C:"MAPGEREJASPRING",
0x2D:"MAPGEREJASUMMER",
0x2E:"MAPGEREJAFALL",
0x2F:"MAPGEREJAWINTER",
0x30:"MAPINNSPRING",
0x31:"MAPINNSUMMER",
0x32:"MAPINNFALL",
0x33:"MAPINNWINTER",
0x34:"MAPALUNALUNSPRING",
0x35:"MAPALUNALUNSUMMER",
0x36:"MAPALUNALUNFALL",
0x37:"MAPALUNALUNWINTER",
0x38:"MAPPANTAISPRING",
0x39:"MAPPANTAISUMMER",
0x3A:"MAPPANTAIFALL",
0x3B:"MAPPANTAIWINTER",
0x3C:"MAPHILLTOPSPRING",
0x3D:"MAPHILLTOPSUMMER",
0x3E:"MAPHILLTOPFALL",
0x3F:"MAPHILLTOPWINTER",
0x40:"MAPHILL2SPRING",
0x41:"MAPHILL2SUMMER",
0x42:"MAPHILL2FALL",
0x43:"MAPHILL2WINTER",
0x44:"MAPLAKESPRING",
0x45:"MAPLAKESUMMER",
0x46:"MAPLAKEFALL",
0x47:"MAPLAKEWINTER",
0x48:"MAPHOTSPRINGSPRING",
0x49:"MAPHOTSPRINGSUMMER",
0x4A:"MAPHOTSPRINGFALL",
0x4B:"MAPHOTSPRINGWINTER",
0x4C:"MAPGOTZSPRING",
0x4D:"MAPGOTZSUMMER",
0x4E:"MAPGOTZFALL",
0x4F:"MAPGOTZWINTER",
0x50:"MCHOUSE1SPRING",
0x51:"MCHOUSE1SUMMER",
0x52:"MCHOUSE1FALL",
0x53:"MCHOUSE1WINTER",
0x54:"MCHOUSE2SPRING",
0x55:"MCHOUSE2SUMMER",
0x56:"MCHOUSE2FALL",
0x57:"MCHOUSE2WINTER",
0x58:"MCHOUSE3SPRING",
0x59:"MCHOUSE3SUMMER",
0x5A:"MCHOUSE3FALL",
0x5B:"MCHOUSE3WINTER",
0x5C:"KNDGKUDASPRING",
0x5D:"KNDGKUDASUMMER",
0x5E:"KNDGKUDAFALL",
0x5F:"KNDGKUDAWINTER",
0x60:"KNDGDOMBASPRING",
0x61:"KNDGDOMBASUMMER",
0x62:"KNDGDOMBAFALL",
0x63:"KNDGDOMBAWINTER",
0x64:"KNDGDOMBAUPSPRING",
0x65:"KNDGDOMBAUPSUMMER",
0x66:"KNDGDOMBAUPFALL",
0x67:"KNDGDOMBAUPWINTER",
0x68:"KNDGDOMBAUP1SPRING",
0x69:"KNDGDOMBAUP1SUMMER",
0x6A:"KNDGDOMBAUP1FALL",
0x6B:"KNDGDOMBAUP1WINTER",
0x6C:"KNDGDOMBAUP2SPRING",
0x6D:"KNDGDOMBAUP2SUMMER",
0x6E:"KNDGDOMBAUP2FALL",
0x6F:"KNDGDOMBAUP2WINTER",
0x70:"KNDGAYAMSPRING",
0x71:"KNDGAYAMSUMMER",
0x72:"KNDGAYAMFALL",
0x73:"KNDGAYAMWINTER",
0x74:"KNDGAYAMUP1SPRING",
0x75:"KNDGAYAMUP1SUMMER",
0x76:"KNDGAYAMUP1FALL",
0x77:"KNDGAYAMUP1WINTER",
0x78:"KNDGAYAMUP2SPRING",
0x79:"KNDGAYAMUP2SUMMER",
0x7A:"KNDGAYAMUP2FALL",
0x7B:"KNDGAYAMUP2WINTER",
0x7C:"HOTHOUSESPRING",
0x7D:"HOTHOUSESUMMER",
0x7E:"HOTHOUSEFALL",
0x7F:"HOTHOUSEWINTER",
0x80:"RMHPOPURILANTAI1SPRING",
0x81:"RMHPOPURILANTAI1SUMMER",
0x82:"RMHPOPURILANTAI1FALL",
0x83:"RMHPOPURILANTAI1WINTER",
0x84:"RMHPOPURILANTAI2SPRING",
0x85:"RMHPOPURILANTAI2SUMMER",
0x86:"RMHPOPURILANTAI2FALL",
0x87:"RMHPOPURILANTAI2WINTER",
0x88:"RMHBARLEYLANTAI1SPRING",
0x89:"RMHBARLEYLANTAI1SUMMER",
0x8A:"RMHBARLEYLANTAI1FALL",
0x8B:"RMHBARLEYLANTAI1WINTER",
0x8C:"RMHBARLEYLANTAI2SPRING",
0x8D:"RMHBARLEYLANTAI2SUMMER",
0x8E:"RMHBARLEYLANTAI2FALL",
0x8F:"RMHBARLEYLANTAI2WINTER",
0x90:"RMHMANNALT1SPRING",
0x91:"RMHMANNALT1SUMMER",
0x92:"RMHMANNALT1FALL",
0x93:"RMHMANNALT1WINTER",
0x94:"RMHMANNALT2SPRING",
0x95:"RMHMANNALT2SUMMER",
0x96:"RMHMANNALT2FALL",
0x97:"RMHMANNALT2WINTER",
0x98:"RMHMANNABASEMENTSPRING",
0x99:"RMHMANNABASEMENTSUMMER",
0x9A:"RMHMANNABASEMENTFALL",
0x9B:"RMHMANNABASEMENTWINTER",
0x9C:"RMHSAIBARAHSPRING",
0x9D:"RMHSAIBARAHSUMMER",
0x9E:"RMHSAIBARAHFALL",
0x9F:"RMHSAIBARAHWINTER",
0xA0:"PERPUSTAKAANSPRING",
0xA1:"PERPUSTAKAANSUMMER",
0xA2:"PERPUSTAKAANFALL",
0xA3:"PERPUSTAKAANWINTER",
0xA4:"RMHMARRYLANTAI1SPRING",
0xA5:"RMHMARRYLANTAI1SUMMER",
0xA6:"RMHMARRYLANTAI1FALL",
0xA7:"RMHMARRYLANTAI1WINTER",
0xA8:"RMHMARRYLANTAI2SPRING",
0xA9:"RMHMARRYLANTAI2SUMMER",
0xAA:"RMHMARRYLANTAI2FALL",
0xAB:"RMHMARRYLANTAI2WINTER",
0xAC:"RMHELLISPRING",
0xAD:"RMHELLISUMMER",
0xAE:"RMHELLIFALL",
0xAF:"RMHELLIWINTER",
0xB0:"RMHMAYORSPRING",
0xB1:"RMHMAYORSUMMER",
0xB2:"RMHMAYORFALL",
0xB3:"RMHMAYORWINTER",
0xB4:"TOKOR1SPRING",
0xB5:"TOKOR1SUMMER",
0xB6:"TOKOR1FALL",
0xB7:"TOKOR1WINTER",
0xB8:"TOKOR2SPRING",
0xB9:"TOKOR2SUMMER",
0xBA:"TOKOR2FALL",
0xBB:"TOKOR2WINTER",
0xBC:"KLINIKLANTAI1SPRING",
0xBD:"KLINIKLANTAI1SUMMER",
0xBE:"KLINIKLANTAI1FALL",
0xBF:"KLINIKLANTAI1WINTER",
0xC0:"KLINIKLANTAI2SPRING",
0xC1:"KLINIKLANTAI2SUMMER",
0xC2:"KLINIKLANTAI2FALL",
0xC3:"KLINIKLANTAI2WINTER",
0xC4:"GEREJASPRING",
0xC5:"GEREJASUMMER",
0xC6:"GEREJAFALL",
0xC7:"GEREJAWINTER",
0xC8:"RMHHARVESTSPRITESPRING",
0xC9:"RMHHARVESTSPRITESUMMER",
0xCA:"RMHHARVESTSPRITEFALL",
0xCB:"RMHHARVESTSPRITEWINTER",
0xCC:"INNSPRING",
0xCD:"INNSUMMER",
0xCE:"INNFALL",
0xCF:"INNWINTER",
0xD0:"INNDAPURSPRING",
0xD1:"INNDAPURSUMMER",
0xD2:"INNDAPURFALL",
0xD3:"INNDAPURWINTER",
0xD4:"RMHGOTZSPRING",
0xD5:"RMHGOTZSUMMER",
0xD6:"RMHGOTZFALL",
0xD7:"RMHGOTZWINTER",
0xD8:"MINESPRING",
0xD9:"MINESUMMER",
0xDA:"MINEFALL",
0xDB:"MINEWINTER",
0xDC:"MINELAKE",
0xDD:"FESTTORCH",
0xDE:"FESTBALAPKUDA",
0xDF:"FESTMASAK",
0xE0:"FESTSUMOAYAM",
0xE1:"FESTTOMATO",
0xE2:"FESTSUP",
0xE3:"FESTDOG",
0xE4:"FESTUNK",
0xE5:"MTHILLSORE",
0xE6:"PASTFARM",
0xE7:"PASTHILL",
0xE8:"PASTMTHIKL",
0xE9:"NIGHTMTHILL",
0xEA:"MINEINLAKE",
0xEB:"MAPEB",
0xEC:"MAPEC",
0xED:"MAPED",
0xEE:"MAPEE",
0xEF:"MAPEF",
0xF0:"MAPF0",
0xF1:"MAPF1",
0xF2:"MAPF2",
0xF3:"MAPF3",
0xF4:"MAPF4",
0xF5:"MAPF5",
0xF6:"MAPF6",
0xF7:"MAPF7",
0xF8:"MAPF8",
0xF9:"MAPF9",
0xFA:"MAPFA",
0xFB:"MAPFB",
0xFC:"MAPFC",
0xFD:"MAPFD",
-2:"MAPFE",
-1:"MAPFF",
}
inv_mapdict = {v: k for k, v in mapdict.items()}
direction = {0 :"DIR↙",1:"DIR↖",2:"DIR↗",3:"DIR↘",}
inv_direction= {v: k for k, v in direction.items()}
cod = {
    -1 : "END",
0x01: "MOVE-NPC",
0x02: "OPENTEXTBOX",
0x04: "SETNPCPOS",
0x05: "SETNPCDIR",
0x08: "CHANGEMAP",
0x15: "MOVE-CAM",
0x17: "SOUND-MV",
0x18: "BGM",
0x1b: "LIGHT",
0x28 :"OPEN-DOOR",
0x32:"CALL-EVENT",
0x33: "MOVE-CAM-TO-NPC",
0x34: "SET-OBJ-POS",
0x3d: "SETMCPOS",
0x3e: "MOVE-MC",
0x3f: "MC-ACTION",
0x40: "SET-MC-DIR",
0x4C: "ADVANCE-TIME",
0x52: "MOVE-NPC(SP1)",
}
inv_cod = {v: k for k, v in cod.items()}
