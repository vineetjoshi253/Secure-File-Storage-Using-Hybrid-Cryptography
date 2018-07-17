from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os


def DAES(key,iv):
    f=open(os.path.join(os.getcwd()+"\Segments","0.txt"),"rb")
    content=f.read()
    f.close()
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    content=decryptor.update(content) + decryptor.finalize()
    f=open(os.path.join(os.getcwd()+"\Segments","0.txt"),"wb")
    f.write(content)
    f.close()
    
def DBlowFish(key,iv):
    f=open(os.path.join(os.getcwd()+"\Segments","1.txt"),"rb")
    content=f.read()
    f.close()
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    content=decryptor.update(content) + decryptor.finalize()
    f=open(os.path.join(os.getcwd()+"\Segments","1.txt"),"wb")
    f.write(content)
    f.close()

def DTrippleDES(key,iv):
    f=open(os.path.join(os.getcwd()+"\Segments","2.txt"),"rb")
    content=f.read()
    f.close()
    backend = default_backend()
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    content=decryptor.update(content) + decryptor.finalize()
    f=open(os.path.join(os.getcwd()+"\Segments","2.txt"),"wb")
    f.write(content)
    f.close()
    
def DIDEA(key,iv):
    f=open(os.path.join(os.getcwd()+"\Segments","3.txt"),"rb")
    content=f.read()
    f.close()
    backend = default_backend()
    cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    content=decryptor.update(content) + decryptor.finalize()
    open(os.path.join(os.getcwd()+"\Segments","3.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"\Segments","3.txt"),"wb")
    f.write(content)
    f.close()
    
def DFernet(key):
	f=open(os.path.join(os.getcwd()+"\Segments","4.txt"),"rb")
	content=f.read()
	f.close()
	fer = Fernet(key)
	content=fer.decrypt(content)
	open(os.path.join(os.getcwd()+"\Segments","4.txt"),"w").close()
	f=open(os.path.join(os.getcwd()+"\Segments","4.txt"),"wb")
	f.write(content)
	f.close()

def HybridDeCryptKeys():
    f=open('Original.txt','rb')
    key=f.read()
    f.close()
    fer = Fernet(key)
    listDir=os.listdir(os.path.join(os.getcwd(),"Infos"))
    for i in listDir:
        path=os.path.join(os.getcwd()+"\Infos",i)
        print(path)
        k=open(path,"rb")
        content=k.read()
        print(content)
        k.close()
        content=fer.decrypt(content)
        open(os.path.join(os.getcwd()+"\Infos",i),"wb").close()
        f=open(os.path.join(os.getcwd()+"\Infos",i),"wb")
        print(i)
        f.write(content)
        f.close()
