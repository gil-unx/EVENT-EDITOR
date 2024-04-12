import json
js = json.loads(open("INFO.json", "r").read())
target ="KAREN"
js2 = {
target:
{
    "RAM_INFO":[],
    "DICT":[],
    "ANIM_INFO":[
    ],
    "POS":[],
    "ANIMATION":[]
    }
    }
list = [0,1,2,3,4]
x =0 
js2[target]["ANIMATION"].append(js["POPURI"]["ANIMATION"][x])
js2[target]["POS"].append(js["POPURI"]["POS"][x])
dictS = js["POPURI"]["POS"][x][1]//12
count = js["POPURI"]["POS"][x][1]//12+js["POPURI"]["POS"][x][0]
for i in range(dictS,count):
    dict = js["POPURI"]["DICT"][i]
    print(dict[1]//12)
    js2[target]["ANIM_INFO"].append(js["POPURI"]["ANIM_INFO"][dict[1]//12])
    js2[target]["DICT"].append(dict)


print(js2)