from PIL import Image


def frm_frg( f1 , f2 , i):
#{

        img_o = Image.open(f1)             #original file
        img_c = Image.open(f2)             #cropped file
        img_o=img_o.convert("RGB")
        img_c=img_c.convert("RGB")
        img_n=Image.new("RGB",img_o.size,"rgb(0,0,0)")
        size_o= ox,oy=img_o.size
        size_c= cx,cy=img_c.size
        o_x=-1   #initialize
        o_y=0    #initialize
        dr=cx*cy
        val=0.0
        nr=0.0          #initialize
#        pi= int(raw_input("enter pixel range :"))
        pi=10
        for x in list(img_o.getdata()):                        # wandering in main image
            o_x += 1                        #increment
            if(o_x>=ox):                    #increment
                o_x=o_x-ox                  #increment
                o_y += 1                    #increment
            o_cor=o_x,o_y                   #initialize
            try:                        # if right bounds are reached
                    r1,g1,b1 = img_o.getpixel(o_cor)
                    r2,g2,b2 = img_c.getpixel(o_cor)
                    r=r2-r1
                    g=g2-g1
                    b=b2-b1
                    per=240*(o_x-25)/295
                    if((not(( -pi<r and r<pi ) and ( -pi<g and g<pi ) and ( -pi<b and b<pi ))) and o_y<per):   # checking matching point
                            img_n.putpixel(o_cor,img_o.getpixel(o_cor))
                   #         img_n.putpixel(o_cor,(0,0,0))
                            nr += 1
                            #break
                    else:
                            img_n.putpixel(o_cor,img_c.getpixel(o_cor))
            except:
                         nr += 1
                         #break
                         

#        val=nr/dr
#        print nr,dr
#        if (nr==0):
#                print "2nd img is not present in 1st"
#        elif(val<0.8):
#            print "2nd img not properly found in first"
#            print "\n % match is:"+str(val*100)
#        elif(val>=0.8):
#                print "yup 2nd img is present in 1st"
#                print "\n % match is:"+str(val*100)
#                
#        img_n.show()
        name="f1_"+str(i)+".jpg"
        img_n.save(name)
#        raw_input(" ")
#        print "\a"
#}

    
if (__name__=="__main__"):       #python interpreter is running this module as the main program so it sets the special __name__ variable to have a value "__main__"
#{                                thus any one can import this as  well

#        f1 = raw_input("enter main file name :")
#        f2 = raw_input("enter croped file name :")
        f1 = '1.jpg'
        f2 = '2.jpg'
        frm_frg( f1 , f2 , 0 )

#}

