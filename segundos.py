dias = int(input("Quantos dias?: "))
horas = int(input("Quantas horas?: "))
minutos = int(input("Quantos minutos?: "))
segundos = int(input("Quantos segundos?: "))

dias2 = dias*(24*60*60)
horas2 = horas*(60*60)
minutos2 = minutos*60

soma = dias2+horas2+minutos2+segundos

print ("O total em segundos é:" ,soma,)
