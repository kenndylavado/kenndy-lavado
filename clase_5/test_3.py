    
a = int(input("ingese el primer numero: "))
b = int(input("ingese el segundo numero:"))

def multiplos(a, b):
   if a % b == 0:
       print(" {} es multiplo de {}".format(a,b))
       return multiplos
   elif b % a:
       print("{} es multiplo de {}".format(b,a))
       return multiplos
   else:
       print("ninguno es multiplo")
       return multiplos
print(multiplos(a, b))