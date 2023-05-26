# Print “Bright IT Career” ten times

for i in range(10):
    print("Bright IT Career")

# Write a program to print the odd and even numbers.

for i in range(10):
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        print(i, "is an odd number")

# Write a program to print even number between 10 and 20 using while
i=0
while(i <= 20):
    if i % 2:
        print(i)
    i+=1

# Write a program to find Armstrong number or not
n=input("Enter a number: ")
sum=0
for i in range(len(n)):
    mul=1
    for j in range(len(n)):
        mul*=int(n[i])
    sum+=mul
if str(sum) == n:
    print(n, "is an armstrong number")

# Write a program to find the prime or not.
 
n=int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print(n, "is not a prime number")
        break
else:
    print(n, "is a prime number")

# Write a program to palindrome or not.
n=input("Enter a number: ")
s=""
for i in reversed(range(len(n))):
    s+=n[i]
if s == n:
    print(n, "is an palindrome number")
else:
    print(n, "is not an palindrome number")

#  Print gender (Male/Female) program according to given M/F using switch
s=input("Enter character M or F: ")
if s == 'M':
    print("Male")
else:
    print("Female")
    