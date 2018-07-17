from Encrypt import *
from Decrypt import *
from IVsKeys import *
import threading

def HybridCrypt():
	iv1,iv2=generateIV()
	key1,key2=generateKey()
	HybridCryptKeys()
	t1 = threading.Thread(target=AES, args=(key1,iv1,))
	t2 = threading.Thread(target=BlowFish, args=(key1,iv2,))
	t3 = threading.Thread(target=TrippleDES, args=(key1,iv2,))
	t4 = threading.Thread(target=IDEA, args=(key1,iv2,))
	t5 = threading.Thread(target=EFernet, args=(key2,))

    #Starting the Encription Process	
	t1.start() 
	t2.start() 
	t3.start()
	t4.start()
	t5.start()

    #Thread Sync.
	t1.join() 
	t2.join() 
	t3.join()   
	t4.join()
	t5.join()


 
def HybridDeCrypt():
	HybridDeCryptKeys()
	iv=FetchIV()
	key1,key2=FetchKey()
	t1 = threading.Thread(target=DAES, args=(key1,iv[0],))
	t2 = threading.Thread(target=DBlowFish, args=(key1,iv[1],))
	t3 = threading.Thread(target=DTrippleDES, args=(key1,iv[1],))
	t4 = threading.Thread(target=DIDEA, args=(key1,iv[1],))
	t5 = threading.Thread(target=DFernet, args=(key2,))

    #Starting the Encription Process
	t1.start() 
	t2.start() 
	t3.start()
	t4.start()
	t5.start()

    #Thread Sync.
	t1.join() 
	t2.join() 
	t3.join()
	t4.join()
	t5.join()
	
