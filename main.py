M=float(input("Enter Molar mass: "))
Q=float(input("Enter added heat: "))
Msam=float(input("Enter mass of sample: "))
Ti=int(input("Enter Ti:"))
Tf=int(input("Enter Tf: "))
m=(M*0.001)
msam=(Msam*0.001)
Delt=Tf-Ti
print("..........Number A solution...........")
c=(Q/(msam*Delt))
print("specific Heat: ",c)
print("..........Number C solution...........")
n=(msam/m)
print("Number of moles are in sample:",n)
print("..........Number B solution..........")
Msh=(Q/(n*Delt))
print("Molar specific heat:",Msh)