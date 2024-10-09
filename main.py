import cmath
from math import sin, cos, pi, ceil, log2

s, t, k = map(int, input().split())
S = input()
T = input()

def aprox_coincidences(S, T, s, t, k):
    ''' Returns the number of relaxed coincidences between S and T '''
    T = T[::-1]
    
    # Se calcula la potencia de 2 siguiente más grande que la suma de los largos de los strings
    # contiene todas las muestras y es eficiente para fft
    n_for_fft = 2**ceil(log2(s + t))
    C = [0] * n_for_fft

    C_A = count_letter_ocurrencies(S, T, s, t, k, C, n_for_fft, "A")
    C_B = count_letter_ocurrencies(S, T, s, t, k, C, n_for_fft, "B")
    C_C = count_letter_ocurrencies(S, T, s, t, k, C, n_for_fft, "C")

    C = sum_poly(C_A, C_B, C_C)

    return check_relaxed_coincidences(C, len(C), t)

def count_letter_ocurrencies(S, T, s, t, k, C, n_for_fft, letter):
    count_S = [0] * n_for_fft
    for i in range(s):
        if S[i] == letter:
            # marcamos ocurrencia en rango i - k hasta i + k
            min_s = max(0, i - k)
            # aplicamos relajacion
            max_s = i + k + 1
            # contamos ocurrencia de la letra
            count_S[min_s] += 1
            # registrar que se ha salido del rango permitido para la ocurrencia de la letra de interés
            if max_s < s: count_S[max_s] -= 1

    # identificar las posiciones donde se encontraron coincidencias relajadas
    aux = 0
    for i in range(s):
        aux += count_S[i]
        if aux > 0:
            count_S[i] = 1
    count_T = convert_to_poly(T, n_for_fft, letter)
    result = multiply_poly(count_S, count_T)        
    
    return result

def check_relaxed_coincidences(C, c, t):
    ''' Checks the number of relaxed coincidences in C '''
    coincidences = 0
    for i in range(c):
        if C[i] == t:
            coincidences += 1
    return coincidences

def sum_poly(A, B, C):
    ''' Sums three polynomials A, B and C of the same degree '''
    return [a+b+c for a, b, c in zip(A, B, C)]

def convert_to_poly(W, length, letter):
    ''' Converts a string W of length "length" to a polynomial of degree length - 1 '''
    L = [0]*length
    for i in range(len(T)):
        if W[i] == letter:
            L[i] = 1
    return L

def fft(a):
    ''' obtain fft extracted from https://www.geeksforgeeks.org/fast-fourier-transformation-poynomial-multiplication/ '''

    n = len(a)
 
    # caso base
    if n == 1:
        return [a[0]]
 
    # raices de la unidad
    theta = -2*pi/n
    w = list( complex(cos(theta*i), sin(theta*i)) for i in range(n) ) 
     
    # dividir la lista en dos partes, pares e impares
    Aeven = a[0::2]
    Aodd  = a[1::2]
 
    # Llamar recursivamente a fft para los coeficientes pares
    Yeven = fft(Aeven) 
 
    # Llamar recursivamente a fft para los coeficientes impares
    Yodd = fft(Aodd)
 
    # Combinar los resultados de las dos partes
    Y = [0]*n
    
    middle = n//2
    for k in range(n//2):
        w_yodd_k  = w[k] * Yodd[k]
        yeven_k   =  Yeven[k]
         
        Y[k]          =  yeven_k  +  w_yodd_k
        Y[k + middle] =  yeven_k  -  w_yodd_k
     
    return Y

def iift(a):
    n = len(a)
    # Se obtiene la conjugación de la lista a
    a_conjugate = [x.conjugate() for x in a]

    # Se aplica FFT en la lista conjugada
    transformed = fft(a_conjugate)

    # Se obtiene la conjugación de la transformada y se divide por n
    result_conjugate = [x.conjugate() / n for x in transformed]

    # Se retorna la parte real de los elementos, redondeada al entero más cercano
    return [round(x.real) for x in result_conjugate]

def multiply_poly(poly1, poly2):
    ''' multiply two fft polynomials '''
    fft_poly1 = fft(poly1)
    fft_poly2 = fft(poly2)
    m = len(fft_poly2)
    # se multiplica cada coeficiente de los polinomios
    fft_result = [fft_poly1[i] * fft_poly2[i] for i in range(m)]

    # Transformada inversa de Fourier rápida para obtener el resultado
    fft_inversed = iift(fft_result)
    m = len(fft_inversed)

    # Se redondea el componente real de cada elemento (resultado de la transformada inversa) para obtener el polinomio resultante.
    result = [round(x.real) for x in fft_inversed]

    return result

print(aprox_coincidences(S, T, s, t, k))