#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import sys
from PIL import Image
import pyautogui
import chardet
import subprocess
import clipboard
import time
import base64
import zbar
import cv2
import platform

# To naormally close the program
def signal_handler(signal, frame):
        print "You pressed Ctrl+C"
        cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)

# Use clipboard to past str
def paste_str(s,ends):
    clipboard.copy(s+ends)
    pyautogui.hotkey('ctrl', 'v')  
    clipboard.copy('')

# fill in invoice software
def fill_in(s):
    paste_str(s,'')
    pyautogui.hotkey('tab')

def fill_4_in(s1,s2,s3,s4):
    fill_in(s1)
    fill_in(s2)
    fill_in(s3)
    fill_in(s4)
   

# Install the signal_handler
signal.signal(signal.SIGINT, signal_handler)
print('####################################')
print('PC Scanner is running ...')
print('Press Ctrl+C to close camera.')
print('####################################')


# Zbar ralated
scanner = zbar.ImageScanner()
scanner.parse_config('enable')


# To store the last string
last_str=''


# Time related 
TIME_INTERVAL=2
old_time = time.time()
new_time = time.time()

OS = platform.system()
if OS == 'Linux':
	OUTPUT_FORMAT='utf-8'
else:
	OUTPUT_FORMAT='gbk'


# Opencv related
cap = cv2.VideoCapture(0)
while 1:
    ret, output = cap.read()
    if not ret:
            continue
    gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    pil = Image.fromarray(gray)
    width,height = pil.size
    raw = pil.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)
    new_time = time.time()
    for symbol in image:
            s=symbol.data
            time_offset = new_time - old_time
            # Disable output when time offset is so small
            if s==last_str and time_offset < TIME_INTERVAL:
                print "..."          
                pass
            else:
                # We should output the result
                # print s
                En_Coding=chardet.detect(s)
                En_Coding=En_Coding['encoding']
                print En_Coding
                # print s 
                if(En_Coding=='ascii'):
                    if(s[0]!='$'):
                        pyautogui.typewrite(s+'\n')
                    # Guo Shui
                    elif(s[0]=='$'):
                        if(s[1]=='0' and s[2]=='1'):
                            s0=s[3:]
                            s2=base64.b64decode(s0)
                            # print s2
                            En_Coding_format=chardet.detect(s2)
                            En_Coding_format=En_Coding_format['encoding']
                            temp=s2.decode(En_Coding_format)
                            s3=temp.encode(OUTPUT_FORMAT)
                            if(s3.count('</>')==4):
                                a=s3.split('</>')
                                str1=a[0][0:]
                                
                                # Add try-except to haddle error
                                try:
                                    str2=a[1][0:]
                                    str3=a[2][0:]
                                    str4=a[3][0:]
                                    fill_4_in(str1,str2,str3,str4)
                                except:  
                                    print "Decode Error"
                                    pass
                                print "Input end"
                    else:
                        pass

                else:
                    if ("AALIPAY" in s)and("→" in s):
                        # Fill tables
                        a=s.split('→')  # DO NOT CHANGE THIS LINE if you do not know 
                        # Deleta extra char
                        # print a[0][2:]
                        str1=a[0][2:]
                        # Add try-except to haddle error 
                        try:
                            temp1=str1.decode(En_Coding)
                            section1=temp1.encode(OUTPUT_FORMAT)
                            str2=a[1][1:]
                            temp2=str2.decode(En_Coding)
                            section2=temp2.encode(OUTPUT_FORMAT)
                            str3=a[2][1:]
                            temp3=str3.decode(En_Coding)
                            section3=temp3.encode(OUTPUT_FORMAT)
                            str4=a[3][1:]
                            temp4=str4.decode(En_Coding)
                            section4=temp4.encode(OUTPUT_FORMAT)
                            fill_4_in(section1,section2,section3,section4)
                        except:
                            #print "Decode Error" 
                            pass

                    elif ("AALIPAY" not in s)and("→" in s):
                          a=s.split('→')  # DO NOT CHANGE THIS LINE if you do not know
                          str1=a[0][9:]
                          
                          try:
                              
                              temp1=str1.decode(En_Coding)
                              section1=temp1.encode(OUTPUT_FORMAT)
                              str2=a[1][1:]
                              temp2=str2.decode(En_Coding)
                              section2=temp2.encode(OUTPUT_FORMAT)
                              str3=a[2][1:]
                              temp3=str3.decode(En_Coding)
                              section3=temp3.encode(OUTPUT_FORMAT)
                              str4=a[3][1:]
                              temp4=str4.decode(En_Coding)
                              section4=temp4.encode(OUTPUT_FORMAT)
                              fill_4_in(section1,section2,section3,section4)
                          except:
                              #print "Decode Error"  
                              pass
                        
                    else:
                        # Other utf8 code just covert code and past
                        try:
                            s=s.decode(En_Coding)
                            s=s.encode('gbk') 
                            fill_in(s)
                        except:
                            pass
                        
                old_time = time.time()
            # Update last_str
            last_str=s

