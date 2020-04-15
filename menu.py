import os
import cv2
import getpass
cap=cv2.VideoCapture(0)
os.system("tput setaf 1")
print("\t\t\tHey welcome to my project")
os.system("tput setaf 7")
print("\t\t\t-------------------------------------------")
#define menu
passw=getpass.getpass('plz entre password  :  ')
apssw='root'
if passw!=apssw:
    print('incorrect authirizatio')
    exit()
print ("where you want to perform your jobs(local/remote)",end='') #ask user
location=input()

print(location)
if location=="remote":
    remoteIP=input("enter your Ip:")
print("""press1:to open camera it work localy
press2:to check cal
press3:start docker services

""")

print("enter your choice :",end="")
ch=input()

if location == "local":
	
		if int(ch)==1:
			while True:
				status,photo=cap.read()
				cv2.imshow('my img',photo)
				if cv2.waitKey(1)==27:
					break
			cv2.distroyAllWindows()
			cap.release()
		elif int(ch)==2:
			os.system("cal")
		elif int(ch)==3:
				os.system("systemctl start docker")

		else:
			print("option not supported")
elif location=="remote":
	if int(ch)==1:
    		os.system("ssh {0} date".format(remoteIP))
	elif int(ch)==2:
			os.system("ssh {0} cal".format(remoteIP))
	elif int(ch)==3:
			os.system("ssh {0} systemctl start docker".format(remoteIP))
	else:
		print("option not supported")