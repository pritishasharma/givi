n=int(input())
m=n
s=0
while(n>=1):
    r=n%10
    s=s*10+r
    n=n//10
if(s==m):
    print("yes")
else:
    print("no")
