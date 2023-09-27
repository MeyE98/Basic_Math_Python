def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b

def es_primo(num):
    if num < 2: 
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Verificar si un número es primo")
        
        opcion = int(input("Elige una opción: "))
        
        if opcion in [1, 2, 3, 4]:
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
        
        if opcion == 1:
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {division(num1, num2)}")
        elif opcion == 5:
            num = int(input("Ingresa un número para verificar si es primo: "))
            if es_primo(num):
                print(f"{num} es un número primo.")
            else:
                print(f"{num} no es un número primo.")
        
        continuar = input("¿Deseas volver al menú? (s/n): ")
        
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
