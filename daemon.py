import threading
import time
import os

flag= True
def cleanup(cache_obj):
    i=0
    file1 = "log"
    if(os.path.exists("C:\Users\pinkaravi\Desktop\CoAPthon-master\log")):

        f = open(file1,'w')
    else:
        f = open(file1,'a')
    time.sleep(10)
    #print cache_obj.keys()
    while(flag):
        for key in cache_obj.keys():
            if cache_obj[key].creation_time+cache_obj[key].max_age-time.time()<=0:
                f.write("Deleting : " + str(key)+str(cache_obj[key])+"\n")
                del cache_obj[key]
        time.sleep(10)
    f.close()
    return