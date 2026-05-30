print("===================================")
print("          CALCULADORA BÁSICA       ")
print("===================================")
print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")
print("===================================")
op = input("\nSeleccione una opción (1/2/3/4): ").strip()
if op not in ("1", "2", "3", "4"):
    print("Opción inválida. Fin.")
    exit()

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Entrada inválida. Use números.")
    exit()

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

if op == "1":
    print(f"\nSuma: {sumar(num1, num2)}")
elif op == "2":
    print(f"\nResta: {restar(num1, num2)}")
elif op == "3":
    print(f"\nMultiplicación: {multiplicar(num1, num2)}")
else:
    resultado = dividir(num1, num2)
    print(f"\nDivisión: {resultado}")