'''Find the sum of its digits'''


def get_sum():
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum
n=input("Enter the Number:")
print(get_sum())


