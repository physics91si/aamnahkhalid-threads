import threading
import time



def main():
	threads = []
	for i in range (1, 51):
		t= threading.currentThread().getName()
		t= threading.Thread(target = hellowrld, args = (i,))
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

def hellowrld(i):
	sup = "Hello from Thread " + str(i) + "!"
	print (sup)

main()