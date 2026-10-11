def calculadora():
    print("--- Calculadora Sencilla ---")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            return

        if opcion == '1':
            print(f"Resultado: {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1 * num2}")
        elif opcion == '4':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
            else:
                print(f"Resultado: {num1 / num2}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    calculadora()
