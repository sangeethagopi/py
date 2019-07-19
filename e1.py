jj1,bh1=input().split()
jj1=int(jj1)
bh1=int(bh1)
sac=''
urn1=2
if(jj1+bh1<=3):
    for i in range(0,jj1+bh1):
        if(i%2!=0):
            sac=sac+'0'
        else:
            sac=sac+'1'
else:    
    for i in range(0,jj1+bh1):
        if(i==urn1):
            sac=sac+'0'
            if(urn1==bh1):
                urn1=urn1+2
            else:
                urn1=urn1+3
        else:
            sac=sac+'1'
x=len(sac)-1
if(int(sac[x])==0):
    print('-1') 
elif jj1==1 and bh1==2: 
     print("011")
else:
    print(sac)
