# keyword arguement example in python

def cat_properties(**kwargs):
    print(kwargs)

def dog(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

cat_properties()
cat_properties(color='red', size='big')
cat_properties(color='red', size='big', sound='meow')
cat_properties(age = 3,color='yellow', size='small', sound='mew')

dog('fido', 'brown', 'big', age=3, color='black', size='big')
dog('jimmy', 'black', color='brown', sound='bark')

