# Usando for loop
print("Usando for loop:")
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)

# Usando while loop
print("\nUsando while loop:")
andar = 20
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1

# Simulando do-while loop com while
print("\nSimulando do-while loop com while:")
andar = 20
while True:
    if andar != 13:
        print(andar)
    andar -= 1
    if andar == 0:
        break