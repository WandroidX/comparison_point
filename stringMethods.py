from tiempo import tiempo

entrada = input("write:\n")

if entrada.isalpha():
    print(entrada.upper())

elif entrada.isspace() or entrada == "":
    print("the input cant be empty".upper())

print(tiempo(864000))
