class Matrix:
    
    
    def __init__(self, matrix_string):
        filas = matrix_string.split("\n")
        self.filas = []
        for fila in filas:
            columnas = list(map(lambda n: int(n), fila.split()))
            self.filas.append(columnas)

    def fila(self, index):
        return self.filas[index-1]

    def column(self, index):
        col = []
        for fila in self.filas:
            col.append(fila[index-1])
        return col
        