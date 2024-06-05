x=int(input("Digite um número: "))
n=int(input("Digite um número>0: "))
def pot(x, n):
    if n==0:
        return 1
    elif n>0:
        return x * pot(x, (n-1))
print(pot(x, n))