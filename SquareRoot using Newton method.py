'''Find the squareRoot of given number by using Newton method '''

def get_sqrt(number):
    sqroot = number
    while abs(number-sqroot * sqroot)>precision:
        print(sqroot)
        sqroot=(sqroot+number/sqroot)/2
    return sqroot

number=7
precision=0.01
print(get_sqrt(number))
