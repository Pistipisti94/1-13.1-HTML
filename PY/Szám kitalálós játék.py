import random
A = random.randint(1,100)
win = False
Turns =0
while win==False:
    B = input("írj egy számot 1 és 100 között: ")
    Turns +=1
    if A==int(B):
        print("Talált!")
        print("Próbák száma: ",Turns)
        win == True
        break
    else:
     if A>int(B):
        print("Kevés")
     else:
        print("Sok")