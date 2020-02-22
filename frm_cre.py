import cv2
import frm_frg

def frm_cre(v1):
#{
    cap = cv2.VideoCapture(v1)
#cap.open('file.avi')
    i=0
    if (cap.isOpened()==False):
        print "img not loded"
    
    while(cap.isOpened()):
        ret,frame = cap.read()
        #gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)

        cv2.imwrite('f1_'+str(i)+'.jpg',frame)

        if(i>80 and i<280):
            img='f1_'+str(i)+'.jpg'
            frm_frg.frm_frg('f1_50.jpg',img,i)
            
        i+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
#}

if __name__=='__main__':
#{
    v1 = raw_input("enter video name :")
    frm_cre( v1 )
#}
