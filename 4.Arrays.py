# Performing operations on Arrays
def dup(l):
    arr=[]
    dup=[]
    count=0
    count1=0
    for i in l:
        if i in arr and i not in dup:
            dup.insert(count1, i)
            count1+=1
        else:
            arr.insert(count, i)
            count+=1
    return dup
def eveodd(l):
    eve=[]
    odd=[]
    count=0
    count1=0
    for i in l:
        if i % 2 == 0:
            eve.insert(count, i)
            count+=1
        else:
            odd.insert(count1, i)
            count1+=1
    return eve,odd

l=[1,2,3,4,5,2,2,1,3,4]
copy=[]
sum=0
search=5
max=0
min=99999999
for i in range(len(l)-1):
    sum+=l[i]
    if l[i] >= max:
        max=l[i]
    if l[i] <= min:
        min=l[i]
    if l[i] == 5:
        print("Element found at ", i)
        del l[i]
copy=l
print("The Actual list is: ", l)
print("Sum is: ", sum)
print("Average of the list is: ", sum/len(l))
print("The copied list is: ", copy)
print("The minimum value in the list is: ", min)
print("The maximum value in the list is: ", max)
print("The duplicate values in list are: ", dup(copy))
eve,odd=eveodd(dup(copy))
print("The even numbers in the list are: ", eve)
print("The odd numbers in the list are: ", odd)
l.insert(2,4)
# print(l)

