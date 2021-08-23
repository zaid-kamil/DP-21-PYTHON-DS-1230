# default parameters in function
def power(num, exp=2):
    return num ** exp

out= power(2, 3)
print(out)
out = power(3) # default value of exp is 2
print(out)
out = power(3,10)
print(out)
out =  power(num = 5) # default value of exp is 2
print(out)
out = power(num=5, exp=4)
print(out)

print("this, is great".split())
print("this, is great".split(','))