import random

passengers=0
pedestrians=0

for i in range(100):
    case = random.randint(0,1)
    if case==0:
        passengers+=1
    else:
        pedestrians+=1
        
stat1=passengers/100
stat2=pedestrians/100

print(stat1,stat2)

if stat1>stat2:
    print("kill passengers")
elif stat1<stat2:
    print("kill pedestrians")
else:
    pass
