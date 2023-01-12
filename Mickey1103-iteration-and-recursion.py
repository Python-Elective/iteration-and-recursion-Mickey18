'''
The function iterativePower contain base and exponential
    if the exponent is 0 
        it will return as 1
    else the original base is equal to base
        for every value in range of the exponent decrease by 1
            multiply base with the original base
        then store the value to base
print iterativePower contain base 6 and exponent 2

'''

def iterativePower(base, exp):
    if exp == 0:
        return 1
    else:
        OriginalBase = base
        for i in range (exp - 1):
            base *= OriginalBase
        return base

print(iterativePower(6,2))

'''
The function recursivePower contain base and exponential
    if the exponent is 0 
        it will return as 1
    else multiply the base value with the recursivePower:
        contain base and exponent that decrease by 1
print recursivePower contain base 6 and exponent 2

'''

def recursivePower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * (recursivePower(base, exp - 1))
        
print(recursivePower(6,2))

