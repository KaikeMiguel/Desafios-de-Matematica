print("--------DETERMINANTE DE MATRIZ--------\n")

mtx_linha = int(input("Digite o tamanho da matriz quadrada: "))
mtx_coluna = mtx_linha
mtx_size = mtx_linha

matriz = []

# ======================================================
# Criação da Matriz Quadrada

for linha in range(mtx_linha):
    new_linha = []
    
    for coluna in range(mtx_coluna):
        new_linha.append(int(input(f"{linha+1}m X {coluna+1}n: ")))
        
    
    matriz.append(new_linha)


print("\n---------ESTRUTURA DA MATRIZ----------\n")
for linha in range(mtx_linha):
    for coluna in range(mtx_coluna):
        print("[",matriz[linha][coluna], "]",end="")

    print()

# ======================================================
# Calculo do Sn

n = mtx_size
i = 1
Sn = 1

while i <= n:
    Sn *= i
    i += 1

    
# ======================================================
# Funções: sigma (σ)

sigma = []
j = 1
sgn = ""    

while j <= mtx_size:
    sgn += str(j)
    j+=1


def permutation(lst):
    if len(lst) < 2:
        return [lst]
    
    l = []
    
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       
       for p in permutation(remLst):
           l.append([m] + p)
           
    return l


for i in permutation([i+1 for i in range(mtx_size)]):
    sigma.append("".join(map(str,i)))
    

def lev(a,b):
    if len(a) == 0:
        return len(b)
    
    elif len(b) == 0:
        return len(a)-1
    
    elif a[0] == b[0]:
        return lev(a[1:], b[1:])
    
    else:
        return 1 + min( lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]) )

    
# ======================================================
# Produtório (∏)

def produtorio(e,n):
    p = 1
    
    for i in range(n):
        p *= e

    return p
       
            
# ======================================================
# Somatória (∑)

def somatoria(e,n):
    s = 0
    
    for i in range(n):
        s += e

    return s

    
# ======================================================
# Conclusão


print("\n-----------RESULTADO FINAL------------\n")
print("Sn =",Sn)
print("σ =",sigma)
print("∏ =",)
print("∑ =",)
print("det(A) =",)
    