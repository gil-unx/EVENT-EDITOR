

import png,shutil
import struct
from FUN import *
import json,io,os
from PIL import Image


def SWPAL(inf,ouf):
    pal = open(inf,"rb")
    outpal = open(ouf,"wb")
    outpal.write(struct.pack("HHIHH",512,0x400,0,256,1))
    pal.read(4)
    for i in range(256):
        v,v1= struct.unpack("BB",pal.read(2))
        biner = ""
        biner+="{0:08b}{1:08b}".format(v,v1)
        r = (int(biner[:5],2))
        g = (int(biner[5:10],2))<<5
        b= (int(biner[10:15],2))<<10
        a = int(biner[15],2)<<15
        if a == 0:
            r,g,b,a = 0,0,0,0
        outpal.write(struct.pack("H",a|b|g|r))
    
    pass


def idle(tileIndex,dictIdx,js,src,target,arr,sub):
    js[target]["POS"].append([len(arr),0])  
    ANIMATIONS = []
    for ar in arr:
        jsc = json.loads(open("{0:04d}/{1}/INFO.json".format(src,ar),"r").read())
        dict =jsc["DICT"][1]
        dict[1] = dict[1]+dictIdx
        ANIMATION = jsc["ANIMATION"][0]
        ANIMATION[0]+=(dictIdx//12)+sub
        ANIMATIONS.append(ANIMATION)
        dictIdx+=12
        js[target]["DICT"].append(dict)
        
        ANIM_INFO =jsc["ANIM_INFO"][0]
        index = ANIM_INFO[0]
      
        
        js[target]["ANIM_INFO"].append(ANIM_INFO)
    js[target]["ANIMATION"].append(ANIMATIONS)
    return js,dictIdx,sub
    
def anim(tileIndex,dictIdx,js,src,target,animation,sub):
    jsc = json.loads(open("{0:04d}/{1}/INFO.json".format(src,animation),"r").read())
    
    ANIMATIONS = []
    for ani in jsc["ANIMATION"]:
       
        ani[0]+=(dictIdx//12)+sub
        ANIMATIONS.append(ani)
    js[target]["ANIMATION"].append(ANIMATIONS)
    for dic in jsc["DICT"]:
        dic[1]+=dictIdx
        js[target]["DICT"].append(dic)
    js[target]["ANIM_INFO"].extend(jsc["ANIM_INFO"])
    dictIdx+= len(jsc["DICT"]*12)-12
    js[target]["POS"].append([len(jsc["ANIM_INFO"]),0])    
    
    return js,dictIdx,sub+1
def g():
    sub = 0
    src  =1
    target ="MARRY"
    js = {target:{
    "RAM_INFO":[],
    "DICT":[],
    "ANIM_INFO":[
    ],
    "POS":[],
    "ANIMATION":[]
    }
    }
    dictIdx = 0
    tileIndex = 1
    #idle0
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION01","ANIMATION03","ANIMATION03_flip","ANIMATION01_flip"],sub)
    #move
    sub+=1
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION06",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION08",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION08_flip",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION06_flip",sub)
    
    #idle1
    sub-=1
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION10","ANIMATION10","ANIMATION10_flip","ANIMATION10_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION11","ANIMATION11","ANIMATION11_flip","ANIMATION11_flip"],sub)
    ##anim
    sub+=1
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION12",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION12_flip",sub)
    ##anim
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION14",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION14_flip",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION15",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION15_flip",sub)
    #idle1
    sub-=1
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION16","ANIMATION16","ANIMATION16_flip","ANIMATION16_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION17","ANIMATION17","ANIMATION17_flip","ANIMATION17_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION18","ANIMATION18","ANIMATION18_flip","ANIMATION18_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION19","ANIMATION19","ANIMATION19_flip","ANIMATION19_flip"],sub)
    
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION22","ANIMATION22","ANIMATION22_flip","ANIMATION22_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION23","ANIMATION23","ANIMATION23_flip","ANIMATION23_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION24","ANIMATION24","ANIMATION24_flip","ANIMATION24_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION25","ANIMATION25","ANIMATION25_flip","ANIMATION25_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION26","ANIMATION26","ANIMATION26_flip","ANIMATION26_flip"],sub)
    
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION27","ANIMATION27","ANIMATION27_flip","ANIMATION27_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION28","ANIMATION28","ANIMATION28_flip","ANIMATION28_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION28","ANIMATION28","ANIMATION28_flip","ANIMATION28_flip"],sub)
    
    
    
 
    
    ##anim
    
    
    sub+=1
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION40",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION40_flip",sub)

    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION41",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION41_flip",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION42",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION42_flip",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION43",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION43_flip",sub)
    
    
    ##idle1
    sub-=1
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION44","ANIMATION44","ANIMATION44_flip","ANIMATION44_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION45","ANIMATION45","ANIMATION45_flip","ANIMATION45_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION46","ANIMATION46","ANIMATION46_flip","ANIMATION46_flip"],sub)
    
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION54","ANIMATION46","ANIMATION46_flip","ANIMATION46_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION55","ANIMATION46","ANIMATION46_flip","ANIMATION46_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION56","ANIMATION46","ANIMATION46_flip","ANIMATION46_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION57","ANIMATION46","ANIMATION46_flip","ANIMATION46_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION58","ANIMATION46","ANIMATION46_flip","ANIMATION46_flip"],sub)
    ##anim
    sub+=1
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION59",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION59_flip",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION64",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION64_flip",sub)
    ##idle1
    sub-=1
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION75","ANIMATION75","ANIMATION75_flip","ANIMATION75_flip"],sub)
    js,dictIdx,sub =idle(tileIndex,dictIdx,js,src,target,["ANIMATION76","ANIMATION76","ANIMATION76_flip","ANIMATION76_flip"],sub)
    #anim
    sub+=1
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION77",sub)
    js,dictIdx,sub =anim(tileIndex,dictIdx,js,src,target,"ANIMATION77_flip",sub)
  
   
    
    fileSave("{0}/BINARY/0000.bin".format(target),json.dumps(js).encode("utf-8"))
    fileSave("{0}/SPRITE/0000.png".format(target),json.dumps(js).encode("utf-8"))
    fileSave("{0}/SPRITE_8bit/0000.png".format(target),json.dumps(js).encode("utf-8"))
    dictPal = {}
    palIdx = 0
    for x in js[target]["ANIM_INFO"]:
        if x[1] not in  dictPal:
            dictPal.update({x[1]:palIdx})
            SWPAL("{0:04d}/BINARY_PALETTE//{1:04d}.bin".format(src,x[1]),"{0}/BINARY/{1:04d}.bin".format(target,palIdx))
            js[target]["RAM_INFO"].append([0,0,256,1])
            im = Image.new('RGBA', (512, 1),(0,255,0,255))
            im.save("{0}/SPRITE_8bit/{1:04d}.png".format(target,palIdx))
            im =im.resize((1024,1))
            im.save("{0}/SPRITE/{1:04d}.png".format(target,palIdx))
            palIdx+=1
    
    print(len(dictPal))
    dictN = {}
    dictIndex =len(dictPal)
   
    for j in range(len(js[target]["ANIM_INFO"])):
        
        index =js[target]["ANIM_INFO"][j][0]
        palindex =js[target]["ANIM_INFO"][j][1]
        if index not in  dictN:
            dictN.update({index:dictIndex})
            dictIndex+=1
        js[target]["ANIM_INFO"][j][0] = dictN[index]
        js[target]["ANIM_INFO"][j][1] = dictPal[palindex]
        shutil.copy("{0:04d}/BINARY_SPRITE//{1:04d}.bin".format(src,index),"{0}/BINARY/{1:04d}.bin".format(target,dictN[index]))
        os.system("rle.exe {0}/BINARY/{1:04d}.bin".format(target,dictN[index]))
        shutil.copy("{0:04d}/PNG//{1:04d}.png".format(src,index),"{0}/SPRITE_8bit/{1:04d}.png".format(target,dictN[index]))
         
        print("{0:04d}/PNG//{1:04d}.png".format(src,index),"{0}/SPRITE_8bit/{1:04d}.png".format(target,dictN[index]))

    for c in  dictN:
        img = Image.open("{0}/SPRITE_8bit/{1:04d}.png".format(target,dictN[c]))
        w,h, = img.size
        img = img.resize((w*2,h))
        img.save("{0}/SPRITE/{1:04d}.png".format(target,dictN[c]))
        js[target]["RAM_INFO"].append([0,0,w//2,h])
        print(w,h)
    pos = 0
    for j in range(len(js[target]["POS"])):
        js[target]["POS"][j][1]+=pos
        pos+=js[target]["POS"][j][0]*10
        
    fileSave("{0}/INFO.json".format(target),json.dumps(js).encode("utf-8"))
    
g()
import GIF