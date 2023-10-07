def es_palindromo(palabra):
    n = len(palabra)
    for i in range(n // 2):
        if palabra[i] != palabra[n - i - 1]:
            return False
    return True

texto = input("Ingrese un texto: ")
palabras = texto.split()

num_palindromos = 0
for palabra in palabras:
    if es_palindromo(palabra):
        num_palindromos += 1
        print(f"'{palabra}' es un palíndromo")

print(f"Hay {num_palindromos} palíndromos en el texto.")