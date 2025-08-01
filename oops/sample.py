
#number pattern
for x in range(1,6):
    str1=0
    str2=''
    for j in range(x+1):
        str1=str1*10+j
        str2+=str(j)+str2
    print(str1)
    print(str2)
