# splitting and arraging given string in required manner as stated

i=int(input())
s=[]

for j in range(0,i):
    s1=''
    s2=''
    line=str(input())
    if line:
        s.append(line)
    else:
        break


    l=int(len(line))    
    for j in range (0,l):
        if j%2==0:
            s1=s1+line[j]
    #print(s1)
    for j in range (0,l):
        if j%2==1:
            s2=s2+line[j]
    print(s1,s2)
    



