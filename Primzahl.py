#Primzahlen Programm

def isPrim(zahl):
    isprim = True
    for i in range (2, zahl):
        if zahl%i==0:
            isprim = False
            break
    return isprim 

print ("Geben Sie eine Zahl ein!")
zahl = input()
lo = isPrim(int(zahl))

if lo :
    print (zahl," ist eine Primzahl!")
else:
    print (zahl," ist keine Primzahl!")
    

    


           
#if zahl%2 != 0:
 #   print ("Diese Zahl ist eine Primzahl!")
#else:
#    print ("Diese Zahl ist keine Primzahl!")
    
