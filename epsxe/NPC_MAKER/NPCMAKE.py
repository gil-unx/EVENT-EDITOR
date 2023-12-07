import os,glob,json
import json,png,struct,io
from PIL import Image
js = {
    "BASE": {
        "RAM_INFO": [
		[0,0,256,1],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60],
		[0,0,20,60]],
"DICT":[
[1,0], 
[1,12], 
[1,24], 
[1,36], 
[0,48], 
[1,48], 
[1,60], 
[1,72], 
[1,84], 
[1,96], 
[1,108], 
[1,120], 
[1,132], 
[0,144], 
[1,144], 
[1,156], 
[1,168], 
[1,180], 
[1,192], 
[1,204], 
[1,216], 
[1,228], 
[0,240], 
[1,240], 
[1,252], 
[1,264], 
[1,276], 
[1,288], 
[1,300], 
[1,312], 
[1,324], 
[0,336], 
[1,336], 
[1,348], 
[1,360], 
[1,372], 
[1,384], 
[1,396], 
[1,408], 
[1,420]],
"ANIM_INFO":[
[1,0,-20,-49,-128,-128,-128,-128],
[2,0,-20,-49,-128,-128,-128,-128],
[2,0,-20,-49,-127,-128,-128,-128],
[1,0,-20,-49,-127,-128,-128,-128],
[3,0,-20,-49,-128,-128,-128,-128],
[4,0,-20,-49,-128,-128,-128,-128],
[3,0,-20,-49,-128,-128,-128,-128],
[1,0,-20,-49,-128,-128,-128,-128],
[5,0,-20,-49,-128,-128,-128,-128],
[6,0,-20,-49,-128,-128,-128,-128],
[5,0,-20,-49,-128,-128,-128,-128],
[1,0,-20,-49,-128,-128,-128,-128],
[7,0,-20,-49,-128,-128,-128,-128],
[8,0,-20,-49,-128,-128,-128,-128],
[7,0,-20,-49,-128,-128,-128,-128],
[2,0,-20,-49,-128,-128,-128,-128],
[9,0,-20,-49,-128,-128,-128,-128],
[10,0,-20,-49,-128,-128,-128,-128],
[9,0,-20,-49,-128,-128,-128,-128],
[2,0,-20,-49,-128,-128,-128,-128],
[7,0,-20,-49,-127,-128,-128,-128],
[8,0,-20,-49,-127,-128,-128,-128],
[7,0,-20,-49,-127,-128,-128,-128],
[2,0,-20,-49,-127,-128,-128,-128],
[9,0,-20,-49,-127,-128,-128,-128],
[10,0,-20,-49,-127,-128,-128,-128],
[9,0,-20,-49,-127,-128,-128,-128],
[2,0,-20,-49,-127,-128,-128,-128],
[3,0,-20,-49,-127,-128,-128,-128],
[4,0,-20,-49,-127,-128,-128,-128],
[3,0,-20,-49,-127,-128,-128,-128],
[1,0,-20,-49,-127,-128,-128,-128],
[5,0,-20,-49,-127,-128,-128,-128],
[6,0,-20,-49,-127,-128,-128,-128],
[5,0,-20,-49,-127,-128,-128,-128],
[1,0,-20,-49,-127,-128,-128,-128]
],
"POS":[
[4,0],
[8,40],
[8,120],
[8,200],
[8,280]],
"ANIMATION":[
[[0,0,0,-255,0],[1,0,0,-255,0],[2,0,0,-255,0],[3,0,0,-255,0]],
[[5,0,0,9,0],[6,0,0,9,0],[7,0,0,9,0],[8,0,0,9,0],[9,0,0,9,0],[10,0,0,9,0],[11,0,0,9,0],[12,0,0,-32759,0]],
[[14,0,0,9,0],[15,0,0,9,0],[16,0,0,9,0],[17,0,0,9,0],[18,0,0,9,0],[19,0,0,9,0],[20,0,0,9,0],[21,0,0,-32759,0]],
[[23,0,0,9,0],[24,0,0,9,0],[25,0,0,9,0],[26,0,0,9,0],[27,0,0,9,0],[28,0,0,9,0],[29,0,0,9,0],[30,0,0,-32759,0]],
[[32,0,0,9,0],[33,0,0,9,0],[34,0,0,9,0],[35,0,0,9,0],[36,0,0,9,0],[37,0,0,9,0],[38,0,0,9,0],[39,0,0,-32759,0]]]}}
tab = {0x0: 0,
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

def make_gif(jsonName):
    folder = jsonName[:-9]
    js = json.loads(open(jsonName,"r").read())
    npc=""
    for j in js:
        npc = str(j)
    list_image = []
    
    ws =[]
    hs = []
    for raminfo in  js[npc]["RAM_INFO"]:
        x,y,w,h = raminfo
        if w == 256:
            w =1
        ws.append(w*4)
        hs.append(h)
    maxw = max(ws)
    maxh = max(hs)
    if (maxw%2) == 1:
        maxw+=1
    if (maxh%2) == 1:
        maxh+=1
    xcenter = 64
    ycenter = 64
    for animinfo in js[npc]["ANIM_INFO"]:
        index,pal,xmin,ymin,flip,q,r,s = animinfo

        im = Image.new('RGBA', (128, 128))
        img = Image.open("{1}/SPRITE-8bit/{0:04d}.png".format(index,folder)).convert("RGBA")
        
        width,height = img.size
        xpos = xcenter+xmin
        ypos = ycenter+ymin
     
        
        if (flip == 1)or(flip == -127):
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        im.paste(img,(xpos,ypos))
        list_image.append(
        {
            
            "image":im,
            "animinfo":animinfo
            
        
        })
    i=0
  
    for anim in js[npc]["ANIMATION"]:
        imd = Image.new('RGBA', (128, 128*len(anim)))
        frames = []
        imy =0
       
        j=0
        for x in anim:
           
            frames.append(list_image[js[npc]["DICT"][x[0]][1]//12]["image"])
            imd.paste(list_image[js[npc]["DICT"][x[0]][1]//12]["image"],(0,imy))
            imy+=128
            j+=1
            
        frame_one = frames[0]
        
        frame_one.save("{1}/ANIMATION{0:02d}.gif".format(i,folder), format="GIF", append_images=frames[1:], optimize = True,save_all=True, duration=100, loop=0, transparency=0, disposal=2)
        
        
        i+=1
    

def MakeBinary():
    for name in glob.glob("MOD_NPC/*.png"):
        print("Membuat >>  "+name)
        baseNameNpc = os.path.basename(name)[:-4]
        outFolder = "NEW_NPC/"+baseNameNpc +"/"
        os.makedirs(os.path.dirname(outFolder), exist_ok=True)
        os.makedirs(os.path.dirname(outFolder+"SPRITE-8bit/"), exist_ok=True)
        os.makedirs(os.path.dirname(outFolder+"SPRITE/"), exist_ok=True)
        os.makedirs(os.path.dirname(outFolder+"BINARY/"), exist_ok=True)
         
        reader = png.Reader(name)
        meta = reader.read_flat()
        if meta[3]["planes"] !=1:
            print("RGBA!!!")
            Image.open(name).quantize(256,2).save(name)
            reader = png.Reader(name)
            meta = reader.read_flat()
        
        #buat fake png palette
        imgpal = Image.new("RGBA",(1024,1),(0,255,0,255))
        imgpal.save(outFolder+"SPRITE/0000.png")
        imgpal.save(outFolder+"SPRITE-8bit/0000.png")
        #cek warna bg
        bgcolor = meta[2][0x7AC]
        #buat binary palette
        palette = meta[3]["palette"]
        binpal = open(outFolder+"BINARY/0000.bin","wb")
        binpal.write(struct.pack("hhhhhh",0x200,0x400,0,0,256,1))
        
        for i in range(256):
            color = palette[i]
            r,g,b,a =color
            blue = tab[b]<<10
            green = tab[g]<<5
            red = tab[r]
            alpha = a
            if a != 0:
                alpha = 1
            if i == bgcolor:
                red, green,blue, alpha = 0,0,0,0
            binpal.write(struct.pack("H",blue|green|red|alpha))
        #buat binary sprite        
        tiles = io.BytesIO(bytes(meta[2]))
        img = Image.open(name)
        ypos = 0
        box =[44, 15, 84, 75]
        for i in range(1,11):
            spr = img.crop(tuple(box))
            box[1]+=128
            box[3]+=128
            spr.save(outFolder+"SPRITE-8bit/{0:04d}.png".format(i))
            w,h = spr.size
            spr =spr.resize((w*2,h))
            spr.save(outFolder+"SPRITE/{0:04d}.png".format(i))
            binsprite = open(outFolder+"BINARY/{0:04d}.bin".format(i),"wb")
            binsprite.write(struct.pack("hhhhhh",0x960,0x400,0,0,20,60))
            tiles.read(128*15)
            for j in range(60):
                tiles.read(44)
                binsprite.write(tiles.read(40))
                tiles.read(44)
            tiles.read(128*53)
        open(outFolder+"INFO.json","w").write(json.dumps(js,indent=4).replace("BASE",baseNameNpc))
        make_gif(outFolder+"INFO.json")

if __name__ == "__main__":
    MakeBinary()
