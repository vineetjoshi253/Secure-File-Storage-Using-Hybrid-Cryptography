import os
from cryptography.fernet import Fernet

def generateIV():
	iv1 = os.urandom(16)
	iv2 = os.urandom(8)
	f=open(os.path.join(os.getcwd()+"\Infos",'IV.txt'),'wb')
	f.write(iv1)
	f.write(b"::::")
	f.write(iv2)
	f.close()
	return iv1,iv2

def generateKey():
	key1 = os.urandom(16)
	key2 = Fernet.generate_key()
	f=open(os.path.join(os.getcwd()+"\Infos",'KEY1.txt'),'wb')
	f.write(key1)
	f.close()
	f=open(os.path.join(os.getcwd()+"\Infos",'KEY2.txt'),'wb')
	f.write(key2)
	f.close()
	return key1,key2

def FetchIV():
	f=open(os.path.join(os.getcwd()+"\Infos",'IV.txt'),'rb')
	cont=f.read()
	f.close()
	iv=cont.split(b"::::")
	return iv

def FetchKey():
	f=open(os.path.join(os.getcwd()+"\Infos",'KEY1.txt'),'rb')
	key1=f.read()
	f.close()
	f=open(os.path.join(os.getcwd()+"\Infos",'KEY2.txt'),'rb')
	key2=f.read()
	f.close()
	return key1,key2
