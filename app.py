from plano_cartesiano import punto
punto1 = punto(3,6)
punto2 = punto(6,8)

punto1.imprimir()
punto2.imprimir()

punto2.mover_punto(2,-2)

punto2.imprimir()

distancia = punto1.distancia_entre(punto2)
print("la distancia entre los puntos 1 y 2 es: ", distancia)