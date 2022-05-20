km=int(input("Enter the kiometer"))
if km<=10:
 a=km*11
elif km>10 and km<=100:
 a=110+(km-10)*10
elif km>100:
 a=1010+(km-10)*9
 print("Your rent is:",a)