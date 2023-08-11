class punto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def imprimir(self):
        print("el punto esta en las coordenas x: ", self.x, " y esta en las coordenadas y: ", self.y)
    
    def mover_punto(self, delta_x, delta_y):
        self.x = delta_x
        self.y = delta_y

    def distancia_entre(self, punto2):
        distancia = ((punto2.x - self.x)**2 + (punto2.y - self.y)**2)**0.5
        return distancia
        