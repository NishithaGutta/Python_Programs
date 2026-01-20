''' Program to convert alternate chars to caps
    Ex:  data   output: dAtA'''

s1 = "PythonProgramming"
s2 = ""
for index in range(0,len(s1)):
    if index % 2 == 0:
        s2 = s2 + s1[index].upper()
    else:
        s2 = s2 + s1[index].lower()
print("converted string:", s2)