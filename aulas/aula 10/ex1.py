v=[1,2,3,4,5,6]
k=int(input("Digite um número: "))
def s(k):
    if k ==0:
        return v[0]
    elif k<len(v):
        return(s(k-1)+v[k])
print(s(k))