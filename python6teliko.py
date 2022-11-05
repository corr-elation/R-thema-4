import math
x=("Green", "Potato", "Ford")
y=("Tyrian purple", "Pasta", "Opel")
nominal_distance=0
k=0
if (len(x) != len(y)):
      print("different  number of variables inside the vectors")
else:
  for i in range(1,len(x)):
    if (x[i]==y[i]):
        k=0
    else:
        k=1
        nominal_distance=nominal_distance+k
print(nominal_distance)


x=("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")
y=("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")
nominal_distance=0
k=0
if (len(x) != len(y)):
      print("different  number of variables inside the vectors")
else:
  for i in range(1,len(x)):
    if (x[i]==y[i]):
        k=0
    else:
        k=1
        nominal_distance=nominal_distance+k
print(nominal_distance)


x=("Werner Herzog", "Aquirre, the wrath of God", "Audi", "Spanish red")
y=("Martin Scorsese", "Taxi driver", "Toyota", "Spanish red")
nominal_distance=0
k=0
if (len(x) != len(y)):
      print("different  number of variables inside the vectors")
else:
  for i in range(1,len(x)):
    if (x[i]==y[i]):
        k=0
    else:
        k=1
        nominal_distance=nominal_distance+k
print(nominal_distance)




      


  




