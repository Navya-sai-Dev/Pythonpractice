gry=0
rav=0
huf=0
sly=0
q1=int(input("do you like dawn or dusk?:"))
if q1==1:
  gry=gry+1
  rav=rav+1
elif q1==2:
  huf=huf+1
  sly=sly+1
else:
  print("Wrong input.")
q2=int(input("When I’m dead, I want people to remember me as:"))
if q2==1:
  huf=huf+2
elif q2==2:
  sly=sly+2
elif q2==3:
  rav=rav+2
elif q2==4:
  gry=gry+2
else:
  print("wrong input.")
q3=int(input("Which kind of instrument most pleases your ear?:"))
if q3==1:
  sly=sly+4
elif q3==2:
  huf=huf+4
elif q3==3:
  rav=rav+4
elif q3==4:
  gry=gry+4
else:
  print("Wrong input.")

print("gryffinder:",gry)
print("ravenclaw:",rav)
print("hufflepuf:",huf)
print("slytherin:",sly)