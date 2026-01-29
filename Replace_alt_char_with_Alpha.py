s1 = "PythonProgramming"
s2=""
count = 65
for index in range(0,len(s1)):
    if index % 2 == 0:
        s2 = s2 + chr(count)
        count += 1
    else:
        s2 = s2 + s1[index]
print("s2:", s2)



