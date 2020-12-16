'''Find the largest integer that divides between two given integer'''

def get_gcd(a,b):
    smallest =min(a,b)
    if a==0 or b==0:
        return max(a,b)
    for i in range (1,smallest+1):
        if a % i ==0 and b % i ==0:
            gcd=i
    return gcd

print(get_gcd(20,10))

def get_gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(get_gcd(20,10))

'''Find the largest integer that divides between n given integer'''

numbers=[16,15,36,8]
gcd =get_gcd(numbers[0],numbers[1])
for i in range(2,len(numbers)):
    gcd=get_gcd(gcd,numbers[i])

print(gcd)

