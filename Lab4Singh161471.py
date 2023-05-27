###################### 
# Course: COMP 1113x2, 2020 
# Lab 4
# Author: Sanvir Singh 
# Student ID: 161471
# email address: 161471s@acadiau.ca
# Date: 2021/02/09 
# I certify that this code is my own and I have not broken any rules concerning Academic Dishonesty. 
######################
print("Greetings")

while True :
    
    n = int(input('Please enter your numerical grade. '))
    
    if n < 50 :
        print("Your grade is F")
        
    if 50 <= n < 53 :
        print("Your grade is D-")
    
    if 53 <= n < 57 :
        print("Your grade is D")
    
    if 57 <= n < 60 :
        print("Your grade is D+")
    
    if 60 <= n < 63 :
        print("Your grade is C-")
    
    if 63 <= n < 67 :
        print("Your grade is C")
        
    if 67 <= n < 70 :
        print("Your grade is C+")
    
    if 70 <= n < 73 :
        print("Your grade is B-")
    
    if 73 <= n < 77 :
        print("Your grade is B")
    
    if 77 <= n < 80 :
        print("Your grade is B+")
        
    if 80 <= n < 85 :
        print("Your grade is A-")
    
    if 85 <= n < 90 :
        print("Your grade is A")
    
    if n >= 90 :
        print("Your grade is A+")

    while True :
        
        q = input("Do you want to convert another grade? (y/n) ")
        if q in ("y","n"):
            break
        print("Invalid input.")
    
    if q == "y" :
        continue
    else : 
        print("Goodbye")
        break
        
    
        
    
    