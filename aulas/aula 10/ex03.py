x=int(input("Digite um número: "))
y=int(input("Digite um número: "))
def MDC(x, y):
    if x>=y and x%y==0:
        return y
    elif x<y:
        return MDC(y, x)
    else:
        return MDC(y, x%y)
print(MDC(x, y))