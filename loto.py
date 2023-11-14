import random

data = []
superball = []

while len(data) != 5:
    data.append(random.randint(1, 69))
    
while len(superball) != 1:
    superball.append(random.randint(1, 26))

print(data, superball)