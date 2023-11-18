print("--------DETERMINANTE DE MATRIZ--------\n")

mtx_size = int(input("Digite o tamanho da MATRIZ: "))

matrix = []
mtx_column = mtx_size
mtx_line = mtx_size


# -- CRIAÇÃO DA MATRIZ QUADRADA --

for line in range(mtx_line):
    new_line = []
    
    for column in range(mtx_column):
        new_line.append(int(input(f"{line+1}m X {column+1}n: ")))
        
    matrix.append(new_line)
    
    
# ==================================================================
# -- CÁLCULO DO Sn --

def SnFunc(mtx_size):
    i = 1
    Sn = 1
    
    while i <= mtx_size:
        Sn *= i
        i += 1
    
    return Sn

Sn = SnFunc(mtx_size)


# ==================================================================
# -- SIGMA (σ) --

def sigmaFunc(mtx_size):
    sigma = []
    sgn = ''
    i = 1
    
    while i <= mtx_size:
        sgn += str(i)
        i += 1
    
    # -- PERMUTAÇÃO --
    
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
    
    return sigma
    
sigma = sigmaFunc(mtx_size)


# -- RESULTADO DA PERMUTAÇÃO --
    
def permResult(sigma):
    base = sigma[0]   
    sigma_changes = []
        
    for i in range(len(sigma)):
        count = 0
        diff = sigma[i]
            
        for j in range(len(base)):
            count += diff[j] != base[j]
            
        resp = count -1 if count > 0 else 0
        sigma_changes.append(resp)
        
    return sigma_changes

sign_sigma = permResult(sigmaFunc(mtx_size))

    
# ==================================================================     
# -- PRODUTÓRIO --


def product(sigma):
    prod = []
    
    for j in range(len(sigma)):
        base = sigma[j]
    
        for i in range(len(base)):
            u = base[i]
            c = 1
            
            while u != str(c):
                c += 1
              
            a = matrix[i][c-1]
            e = ((-1)**sign_sigma[i])*a
            
            prod.append(e)
    
    return prod

prod = product(sigma)

        
# ==================================================================     
# -- SOMATÓRIA --    
        
        
# ==================================================================     
# -- CONCLUSÃO -- 
        
print("\n---------ESTRUTURA DA MATRIZ----------\n")
for line in range(mtx_line):
    for column in range(mtx_column):
        print("[",matrix[line][column], "]",end="")

    print()


print("\n-----------RESULTADO FINAL------------\n")
print("Sn =",Sn)
print("σ =",sigma)
print("∏ =",prod)
print("∑ =",)
print("det(A) =",)        
