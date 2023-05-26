d={1 : "Shell", 2 : "Pro", 3 : "Ravi", 4 : "Shetti", 5 : "yesh"}
print("The dictionary is: ", d)
d[6]="Bast"
print("After Addition: ", d)
d.update({6 : "Bash"})
print("After Update Operation: ", d)
# Nested loop dictionary
nd={1: {"name": "shek", "roll" : 2}, 2 : {"name" : "kret", "roll" : 4}}
# Accessing keys and values from dictionary
# for i in nd.values():
#     for j,k in i.items():
#         print( j, k, end=" ")
print()
print("The dictionary keys are: ", end=" ")
for i in d:
    print(i, end=" ")
d.pop(6)
print("After delete operation: ", d)