class Auto: 
  def __init__(self,marca=None,modelo=None,color=None):
    self.marca=marca
    self.modelo=modelo
    self.color=color
    if marca is not None and modelo is not None and color is not None: 
      print(f"El Auto marca {self.marca}, modelo {self.modelo} de color {self.color} fue creado")
    else: 
      print("No se establecio ninguna propiedad del auto")
  def __str__(self): 
    return f" Auto: {self.marca} \n Modelo: {self.modelo} \n Color: {self.color}" 
  def __del__(self): 
    print("Objeto borrado")     


pocho=Auto("Volkswagen","Combi","Verde")
print(pocho.marca)
evaluacion=eval("5*8")
print(evaluacion)


