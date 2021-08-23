def adder(a, b, c):
    return a + b + c

# positional parameter call
out = adder(1, 2, 3)
# names parameter calls
out = adder(a=1, b=2, c=3)
print(out)

out = adder(b=5,c=2,a=3)
print(out)

out = adder(10, c=10, b=1)
print(out)

out = adder(b=3,c=1,a=2)
print(out)