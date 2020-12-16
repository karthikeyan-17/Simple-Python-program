''' Find the reverse of given numbers'''

rev = 0
n=int(input("Enter the number:"))
num=n
while (n > 0):
    dig= n % 10
    rev = rev * 10 + dig
    n = n // 10


if (num == rev):
    print("The Number is palindrome")
else:
    print("The Number is not palindrome")