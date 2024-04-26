notas = [5,8,5,6,6,2,4,8,9,5,4,2,6,8,4,8,9,9,5]
# notaMayor = 0
# for nota in notas:
#     if nota >= notaMayor:
#         notaMayor = nota
# print(notaMayor)

# for indice in range(12):
#         if ((notas[indice]*0.05)+notas[indice]) <= 5.0:
#             notas[indice] = notas[indice] + (notas[indice] *0.05)
# print(notas)

# for indice in range(12):
#     if notas[indice] > 4.0: 
#         notas[indice] -= 0.5
#     elif notas[indice] < 2.0: 
#         notas[indice] += 0.5
# print (notas)

# notaMenor = 5.0
# for nota in notas:
# #     if nota <= notaMenor:
# #         notaMenor = nota 
# # print (notaMenor)

# rango1 = 0
# rango2 = 0
# rango3 = 0
        
# for nota in notas:
#     if nota >= 0.0 and nota <= 1.99:
#         rango1 += 1
#     elif nota >= 2.0 and nota <= 3.49:
#         rango2 += 1
#     elif nota >= 3.5 and nota <= 5.0:
#         rango3 +=1
# if rango1 > rango2 and rango1 > rango3:
#     print("rango1")
# elif rango2 > rango1 and rango2 > rango3:
#     print ("rango2")
# elif rango3 > rango2 and rango3 > rango1:
#     print("rango3")
# print(rango1)
# print(rango2)
# print(rango3)

# menores = []
# for i in range(len(notas)):
#     menorLocal = 0
#     for a in range(len(notas)):
#         if notas[i] > notas[a]:
#             menorLocal += 1
#     menores.append(menorLocal)
# menores.sort()

# print(menores[round(len(notas)/2)])
# print(menores)


# notaMasrecurrente = 0
# cantidadOcurrencias = 0
# for nota in notas:
#     for nota2 in notas:
#         contador = 0
#         if nota == nota2:
#             contador += 1
#     if contador > cantidadOcurrencias:
#         notaMasrecurrente = nota2
#         cantidadOcurrencias = contador
# print(notaMasrecurrente)



datoMenoresMitad = 0
datoMenoresMitad2 = 0
for i in range(len(notas)):
    menores = 0
    for i2 in range(len(notas)):
        if notas[i2] < notas[i]:
            menores += 1
    if menores == len(notas)/2:
        datoMenoresMitad = notas[i]
    elif menores == (len(notas)/2) + 0.5:
            datoMenoresMitad = notas[i]
            datoMenoresMitad2 = notas[i-1]
    elif menores == (len(notas)/2) - 0.5:
        datoMenoresMitad = notas[i]
        datoMenoresMitad2 = notas[i+1]
if len(notas)/2 == int:
    print (datoMenoresMitad)
else:
    print(f"{datoMenoresMitad} {datoMenoresMitad2}")
    