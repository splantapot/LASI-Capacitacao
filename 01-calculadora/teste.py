print("Oi eros")
try:
    x = input("Digite algo: ")
    x = int(x)
except ValueError:
    print("Digite um número.")
else:
    print(x)