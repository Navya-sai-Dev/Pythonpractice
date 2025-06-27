height=int(input("your height:"))
credits=int(input("your credits:"))
if height>=137 and credits>=10:
  print("enjoy the ride")
elif height<137 and credits>=10:
  print("you're not tall enough to take this ride")
elif height>=137 and credits<10:
  print("you don't have enough credits ")
else:
  print("you don't have eligibility ")      
