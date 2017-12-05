import random
import numpy as np
import matplotlib.pyplot as plt
matriz=[]
iteracion=1000
juegos=100
for i in range(iteracion):
    matriz.append([0]*(juegos+1))
def generar_baraja():
    palos = ['C', 'D', 'T', 'P']
    valores = ['A'] + [v for v in range(2,11)] + ['J', 'Q', 'K']
    return [(valor, palo) for palo in palos for valor in valores]
baraja=generar_baraja()
def baraja_mezclada():
    baraja = generar_baraja() 
    while len(baraja) > 0:
        carta = random.choice(baraja)
        baraja.remove(carta)
        yield carta
def valor_mano(cartas):
    valor = 0
    
    for carta in cartas:
        valor_carta = carta[0]
        if valor_carta in ('J','Q','K'):
            valor += 10
        elif valor_carta == 'A':
            valor=valor+11 if valor+11<=21 else (valor+10 if valor+10<=21 else valor+1)
        else:
            valor += valor_carta
    return valor
def blackjack(pozo, apuesta_minima,j):
    print("Bienvenido al juego de black jack")
    cont=0
    apuesta = solicitar_apuesta(pozo, apuesta_minima)
    while apuesta_minima <= apuesta <= pozo and cont<juegos and pozo<1000:
        resultado = jugar_mano(apuesta, pozo)
        pozo  += resultado
        mostrar_resultado(resultado, pozo)
        apuesta = solicitar_apuesta(pozo, apuesta_minima)
        cont+=1
        matriz[j][cont]=pozo
    while cont<juegos:
        if pozo==0:
            matriz[j][cont]=0
        elif pozo>=1000:
            matriz[j][cont]=pozo
            
        cont+=1
    print("Gracias por participar, su pozo final es: ", pozo)
def solicitar_apuesta(pozo, apuesta_minima):
    valor = -1
    if pozo < apuesta_minima:
        print ("Su pozo no le alcanza para seguir jugando, inténtelo de nuevo en otra oportunidad")
    else:
        while valor != 0 and not (apuesta_minima <= valor <= pozo):
            if apuesta_minima*2<=pozo/2:
                valor=apuesta_minima*2
            else:
                valor=apuesta_minima
    print ("")
    return valor
def mostrar_resultado(resultado, pozo):
    if resultado > 0:
        print("Jugador gana $", resultado)
    elif resultado < 0:
        print("Jugador pierde $", -resultado)
    else:
        print("Empate")
    print("Su pozo es: $", pozo, "\n")
def mostrar_mano(mensaje, mano):
    print(mensaje,
        " ".join ( str(carta[0])+"-"+carta[1] for carta in mano),
        " ( Valor: ", valor_mano(mano), ")\n")
def solicitar_jugada(jugada, valor_mano):
    if jugada == 'I':
        prompt = "Jugada? ('R':Retirarse, 'D':Doblar, 'O':Otra carta, 'M': Mantener cartas) --> "
        print(prompt)
        if valor_mano >=17:
            opcion='M'
        elif valor_mano ==[10,11]:
            opcion='D'
        else:
            opcion='O'
    else:
        prompt = "Jugada? ('R':Retirarse, 'O':Otra carta, 'M': Mantener cartas) --> "
        print(prompt)
        if valor_mano >=15:
            opcion='M'
        else:
            opcion='O'
    """while opcion not in opciones:
        print("opción incorrecta")
        opcion = input(prompt).strip().upper()
        print("Opción elegida: ", opcion, "\n")"""
    return opcion
def jugar_mano(apuesta, pozo):
    print ("Nueva mano, apuesta $", apuesta, " pozo $", pozo-apuesta, "\n")
    baraja = baraja_mezclada()
    mano_jugador, mano_couprier  = [next(baraja), next(baraja)], [next(baraja), next(baraja)]
    ganancia = 0
    if valor_mano(mano_jugador) == 21:
        mostrar_manos(mano_jugador, mano_couprier)
        print ("¡Jugador tienen black jack!")
        ganancia = (3*apuesta)//2
    else:
        jugada = 'I'
        while jugada in ['I', 'O']:
            # mostrar_manos(mano_jugador, mano_couprier)
            mostrar_mano("Cartas Jugador:  ", mano_jugador)
            jugada = solicitar_jugada(jugada, valor_mano(mano_jugador))
            if jugada == 'M':
                mano_couprier = jugar_couprier(mano_couprier, baraja)
            elif jugada == 'D':
                mano_jugador.append(next(baraja))
                mano_couprier = jugar_couprier(mano_couprier, baraja)
            elif jugada == 'O':
                mano_jugador.append(next(baraja))
                if valor_mano(mano_jugador) > 21:
                    jugada = 'R'
        mostrar_manos(mano_jugador, mano_couprier)
        ganancia = determinar_ganancia(mano_jugador, mano_couprier, apuesta, jugada)
    return ganancia
def mostrar_manos(mano_jugador, mano_couprier):
    mostrar_mano("Cartas Jugador:  ", mano_jugador)
    mostrar_mano("Cartas Couprier: ", mano_couprier)
def jugar_couprier(mano, baraja):
    while valor_mano(mano) <17:
        mano.append(next(baraja))
    return mano
def determinar_ganancia(mano_jugador, mano_couprier, apuesta, jugada):
    if jugada == 'R':
        ganancia = -apuesta
    else:
        jugador, couprier = valor_mano(mano_jugador), valor_mano(mano_couprier)
        ganancia = 0
        if jugador <= 21 < couprier or couprier < jugador <= 21:
            ganancia = apuesta
        elif couprier <= 21 < jugador or jugador < couprier <= 21:
            ganancia = -apuesta
        if jugada == 'D':
            ganancia *= 2
    return ganancia
j=0
for i in range(iteracion):
    blackjack(500,10,j)
    j+=1
mediapordias2=[]

for i in range(iteracion):
	mediapordias2.append(np.average	(matriz[i]))


print("-----------------------------------")
print("media total: ")
print(np.average(mediapordias2))
print("desviacion estandar")
print(np.std(mediapordias2))

plt.hist(mediapordias2,bins=20,alpha=0.5,facecolor='b',edgecolor="w")
plt.xlabel("pozo")
plt.ylabel("concentracion de dias")
plt.title("Blackjack")
plt.show()






