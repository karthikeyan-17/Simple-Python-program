''' Find reverse of given number '''

rev = 0
n=int(input("Enter the reverse number:"))
while (n > 0):
    dig= n % 10
    rev = rev * 10 + dig
    n = n // 10

print(rev)