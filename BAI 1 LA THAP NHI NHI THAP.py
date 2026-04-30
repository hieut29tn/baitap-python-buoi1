def Nhi_thap(b):
    t=0
    mu=len(b)-1
    for bi in b:
        t+=int(bi)*2**mu
        mu-=1
    return t

def Thap_nhi(s):
    n=int(s)     
    b=''
    while n>0:
        du=n%2
        b+=str(du)
        n=n//2
    return b[::-1], sum(int(i) for i in b)
  
fi=open("BAI1LA.INP")
fo=open("BAI1LA.OUT","w")
s, n=fi.readline().split()
m=Nhi_thap(s)
bmax=0
tmax=0

for i in range(m,int(n)+1,):
    b, d=Thap_nhi(str(i))
    if bmax<d:
        bmax=d
        tmax=i
b, d=Thap_nhi(str(i))
fo.write(f"{m}\n{b}\n{tmax}")
fi.close()
fo.close()