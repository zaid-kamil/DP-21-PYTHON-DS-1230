# variable arguments example in functions

def nums(*args):
    print(args)
    print(type(args))

def mean(*numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0

nums()
nums(1, 2, 3, 4, 5)
nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nums(1,1,1,1)
nums('hi','there','what is this')
print(mean())
print(mean(1,2,3,4,5))
print(mean(1,2,3,4,5,6,7,8,9,10))
print(mean(1,1,1,1))
# print(mean('hi','there','what is this'))
