def triangulo(n):
    if n==1:
        return 1
    return triangulo(n-1)+ 3 *n-3

#####################################
def quadrado(n):
    if n==1:
        return 1
    return quadrado(n-1)+4 *n-4

#####################################
def hexagono(n):
    if n==1:
        return 1
    return hexagono(n-1) + 6 * n - 6

#####################################

def sequencias():
    t= int(input("Digite um numero natural para que seja o numero de termos:"))
    if t<=0:
        print("Por favor digite um numero maior que zero.")
        return
    
    Tt= [] 
    Tq= []
    th= []
    
    for i in range(1, t + 1):
        Tt.append(triangulo(i))
        Tq.append(quadrado(i))
        th.append(hexagono(i))
    
    print(f"\nOs primeiros {t} termos de cada sequência:")
    print(f"Triângulos (Tt): {Tt}")
    print(f"Quadrados  (Tq): {Tq}")
    print(f"Hexágonos  (th): {th}")    
    
    
    comuns_Tt_Tq = []
    for termo in Tt:
        if termo in Tq:
            comuns_Tt_Tq.append(termo)

    comuns_Tt_th = []
    for termo in Tt:
        if termo in th:
            comuns_Tt_th.append(termo)

    comuns_Tq_th = []
    for termo in Tq:
        if termo in th:
            comuns_Tq_th.append(termo)
            
    print(50*"=")
    print("Listas de termos comuns:")
    print(f"Entre Triângulos (Tt) e Quadrados (Tq): {comuns_Tt_Tq}")
    print(f"Entre Triângulos (Tt) e Hexágonos (th): {comuns_Tt_th}")
    print(f"Entre Quadrados  (Tq) e Hexágonos (th): {comuns_Tq_th}")
    
sequencias()    