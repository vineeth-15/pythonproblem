unit = int(input("Enter Electricity unit: "))
if(unit>0 and unit<=200):
    cost = unit * 0.5
    print("cost to be paid: ",cost)
if(unit>200 and unit<=400):
    cost = 100+((unit-200)*0.65)
    print("cost to be paid: ",cost)
elif(unit>400 and unit<=600):
    cost = 230+((unit-400)*0.85)
    print("cost to be paid: ",cost)
else:
    cost = 400+((unit-600)*1)
    print("cost to be paid: ",cost)
