# Love Calculator


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your crush's name? \n")

name1 = name1.lower()
name2 = name2.lower()

#for true
true=0
true+=name1.count('t')
true+=name2.count('t')
true+=name1.count('r')
true+=name2.count('r')
true+=name1.count('u')
true+=name2.count('u')
true+=name1.count('e')
true+=name2.count('e')

# for love
love=0
love+=name1.count('l')
love+=name2.count('l')
love+=name1.count('o')
love+=name2.count('o')
love+=name1.count('v')
love+=name2.count('v')
love+=name1.count('e')
love+=name2.count('e')

per = true*10+love
if(per<10 or per>90):
    print(f"Your score is {per}, you go together like coke and mentos.")
elif(per<50 and per>40):
    print(f"Your score is {per}, you are alright together.")
else:
    print(f"Your score is {per}.")