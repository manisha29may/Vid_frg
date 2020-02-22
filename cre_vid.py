import cv2


def cre_vid():
#{
    i=0
    cc = cv2.VideoWriter_fourcc('D','I','V','X')
    vid = cv2.VideoWriter('vid1.avi',cc,30.0,(320,240))
    
    while(i<544):
        name='f1_'+str(i)+'.jpg'
        frame = cv2.imread(name)
        vid.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i += 1
    vid.release()
    cv2.destroyAllWindows() 
    
#}

    
if (__name__=="__main__"):
#{    
        cre_vid()

#}
