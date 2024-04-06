import API_PI
import random,threading
import numpy as np

def runnow(l):
    for acc in listtach[l]:
        try:
            phone = acc.split("|")[2]
            password = acc.split("|")[3]
            appapi = API_PI.API_PI(phone,password)
            topass = appapi.signin()
            presences = appapi.proof_of_presences()
            print(phone,presences)
            # print(acc)
        except Exception as e:
            print(e)

file = open("AccPI.txt").read().splitlines()
listtach = np.array_split(file,20)
thread  = []
for l in  range(20):
    thread+=[threading.Thread(target=runnow,args={l},)]
for t in thread:
    t.start()
for t in thread:
    t.join()