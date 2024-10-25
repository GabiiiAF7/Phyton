import math
a=int(input("dime un numero a: "))
b=int(input("dime un numero b: "))
c=int(input("dime un numero c: "))

raiz= b**2-4*a*c
if raiz<=0:
    print("ERROR")

neg= (-b-raiz)/(2*a)
pos=(-b+raiz)/(2*a)

print ("El valor de x1 es: ",neg)
print ("El valor de x1 es: ",pos)
        
    


