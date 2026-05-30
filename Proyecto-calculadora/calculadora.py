print("===================================")
print("          CALCULADORA BÁSICA       ")
print("===================================")
print("1) Sumar")
print("2) Restar")
op = input("\nSeleccione una opción (1/2): ").strip()
if op not in ("1", "2"):
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

if op == "1":
    print(f"\nSuma: {sumar(num1, num2)}")
else:
    print(f"\nResta: {restar(num1, num2)}")
