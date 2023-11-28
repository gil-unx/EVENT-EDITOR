import shutil
for i in range(319):
    print(i)
    try:
        
            shutil.rmtree("ITEM/{0:04d}/PNG".format(i))
    except:
        continue