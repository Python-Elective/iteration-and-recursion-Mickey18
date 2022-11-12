'''
The function iterativePower contain base and exponential
    if the base is the power of 0 
        it will equal to 1
    else the base will multiply itself with the amount of exponent
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
The function iterativePower contain base and exponential
    if the base is the power of 0 
        it will equal to 1
    else multiply the result with the base
print recursivePower contain base 6 and exponent 2

'''

def recursivePower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * (recursivePower(base, exp - 1))
        
print(recursivePower(6,2))

