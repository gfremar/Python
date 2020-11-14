import random
x=random.sample(range(0,100),random.randint(1,40))
y=random.sample(range(0,100),random.randint(1,40))
comun=[a for a in y if a in x]
print("Los valores en común de las matrices son ", comun)