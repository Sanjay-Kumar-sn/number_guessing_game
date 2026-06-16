import random

target=random.randint(1,100)
attempt=10

while True:
    guess=int(input("Enter guess:"))
    attempt=attempt-1
    
    if guess==0:
        print("you lost. The number was ",target)
        break
    
    elif guess==target:
        print("You won at attempt=",attempt)
        break
    
    elif guess>target:
        print("Too High")
        
    else:
        print("Too Low")
        
    if attempt==0:
         print("No attempts left.You lost")
         print("The number was", target)
         break
    print("You have ",attempt," Left")
