import random

# generate a random float between 0 and 1
# every function call is same but value is different
# thats why is called random library
val1 = random.random()
val2 = random.random()
val3 = random.random()
val4 = random.random()
print(val1,val2,val3,val4)

# generate a random integer between 0 and 10
val1 = random.randint(0,10)x
val2 = random.randint(0,10)
val3 = random.randint(0,10)
val4 = random.randint(0,10)
print(val1,val2,val3,val4)

x = [100,200,300,400,500]
val1 = random.choice(x)
val2 = random.choice(x)
val3 = random.choice(x)
print(val1,val2,val3)

val1 = random.choices(x,k=3)
val2 = random.choices(x,k=3)
val3 = random.choices(x,k=3)
print(val1,val2,val3)


