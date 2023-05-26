import re
def substr(str, start, end):
    string=""
    for i in range(len(str)):
        if i>=start and i < end:
            string+=str[i]
    return string
str1="hello"
str2="Hello world"
pattern="world"
print("str1 is: ", str1, "\n", "str2 is:", str2)
print("After Concatenation:", str1+str2)
print("The length of the str1 is: ", len(str1))
print("The substring with start-1 and end-3:", substr(str1, 1, 3))
match=re.search(pattern, str2)
if match:
   print("Pattern is h matching with str2:", match.group())
if str1==str2:
    print("Both strings mactched")
else:
    print("Both strings not matched")
print("The str1 starts with h:", str1.startswith('h'))
print("The str1 ends with o:", str1.endswith('o'))
print("Trimming d in str2 :", str2.strip("d"))
print("Replacing o with h in str2:", str2.replace('o', 'h'))
print("Splitting str2 with whitespace:", str2.split(" "))
print("Integer to String: ", str(123))
print("UpperCase: ", str2.upper(), "\n""LowerCase:", str2.lower())