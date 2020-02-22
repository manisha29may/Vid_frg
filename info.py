import cv2
import numpy as np


def info(v1):
#{
    cap = cv2.VideoCapture(v1)
    
    ret = cap.open(v1)
    print ret
    file=open("vidinfo.txt","w")    
    
    abc = "width:"+ str(int(cap.get(3)))+"\n"
    file.write(abc)
    abc = "height:"+ str(int(cap.get(4)))+"\n"
    file.write(abc)
    abc = "fps:"+ str(int(cap.get(5)))+"\n"
    file.write(abc)
    str1=""
    dec=int(cap.get(6))
    while(dec>0):
        a=dec%256
        str1=str1+chr(a)
        dec=dec/256
    abc = "fourcc:"+str1+"\n"
    file.write(abc)
    abc = "no. of frames:"+ str(int(cap.get(7)))+"\n"
    file.write(abc)
    abc = "duration:" + str(cap.get(7)/cap.get(5)) + "s\n"
    file.write(abc)
        
    
    file.close()
                
    cap.release()
    cv2.destroyAllWindows()
#}


if(__name__=='__main__'):
#{
    v1=raw_input("enter video name: ")
    info(v1)
#}
    
