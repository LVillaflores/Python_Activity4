dict1 = {'No': 1, 'SN': 'A', 'ID': 1, 'Math': 75, 'Eng': 75, 'Phys': 75, 'Psy': 75,
         'ValEd': 75, 'Dist': 75, 'Prog': 75, 'Intro': 75, 'Sem': 0}
dict2 = {'No': 2, 'SN': 'B', 'ID': 2, 'Math': 75, 'Eng': 75, 'Phys': 75, 'Psy': 75,
         'ValEd': 75, 'Dist': 75, 'Prog': 75, 'Intro': 75, 'Sem': 0}
dict3 = {'No': 3, 'SN': 'C', 'ID': 3, 'Math': 75, 'Eng': 75, 'Phys': 75, 'Psy': 75,
         'ValEd': 75, 'Dist': 75, 'Prog': 75, 'Intro': 75, 'Sem': 0}
dict4 = {'No': 4, 'SN': 'D', 'ID': 4, 'Math': 75, 'Eng': 75, 'Phys': 75, 'Psy': 75,
         'ValEd': 75, 'Dist': 75, 'Prog': 75, 'Intro': 75, 'Sem': 0}
dict5 = {'No': 5, 'SN': 'E', 'ID': 4, 'Math': 75, 'Eng': 75, 'Phys': 75, 'Psy': 75,
         'ValEd': 75, 'Dist': 75, 'Prog': 75, 'Intro': 75, 'Sem': 0}

Total1 = dict1.get("Math") + dict1.get("Eng") + dict1.get("Phys") + dict1.get("Psy") + dict1.get("ValEd")\
         + dict1.get("Dist") + dict1.get("Prog") + dict1.get("Intro")
Sem1 = Total1/8

Total2 = dict2.get("Math") + dict2.get("Eng") + dict2.get("Phys") + dict2.get("Psy") + dict2.get("ValEd")\
         + dict2.get("Dist") + dict2.get("Prog") + dict2.get("Intro")
Sem2 = Total2/8

Total3 = dict3.get("Math") + dict3.get("Eng") + dict3.get("Phys") + dict3.get("Psy") + dict3.get("ValEd")\
         + dict3.get("Dist") + dict3.get("Prog") + dict3.get("Intro")
Sem3 = Total3/8

Total4 = dict4.get("Math") + dict4.get("Eng") + dict4.get("Phys") + dict4.get("Psy") + dict4.get("ValEd")\
         + dict4.get("Dist") + dict4.get("Prog") + dict4.get("Intro")
Sem4 = Total4/8

Total5 = dict5.get("Math") + dict5.get("Eng") + dict5.get("Phys") + dict5.get("Psy") + dict5.get("ValEd")\
         + dict5.get("Dist") + dict5.get("Prog") + dict5.get("Intro")
Sem5 = Total5/8

dict1.update(Sem=Sem1)
dict2.update(Sem=Sem2)
dict3.update(Sem=Sem3)
dict4.update(Sem=Sem4)
dict5.update(Sem=Sem5)

for value in dict1.values():
    print(value, end=" ")
print(" ")
for value in dict2.values():
    print(value, end=" ")
print(" ")
for value in dict3.values():
    print(value, end=" ")
print(" ")
for value in dict4.values():
    print(value, end=" ")
print(" ")
for value in dict5.values():
    print(value, end=" ")
