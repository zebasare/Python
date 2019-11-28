class Auto: 
  def __init__(self,marca=None,modelo=None,color=None):
    self.marca=marca
    self.modelo=modelo
    self.color=color
    
    if marca is not None and modelo is not None and color is not None: 
      print(f"El Auto marca {self.marca}, modelo {self.modelo} de color {self.color} fue creado \n")
    else: 
      print("No se establecio ninguna propiedad del auto")
  def __str__(self): 
    return f" Marca: {self.marca} \n Modelo: {self.modelo} \n Color: {self.color} \n" 
  def __del__(self): 
    print("Objeto borrado") 
  #__len__ tiene que retornar un numero
  def __len__(self): 
    return  self.kilometros       

class Automotora: 
    automotora=[]

    def __init__(self,automotora=[]): 
      self.automotora=automotora

    def agregar_autos(self,a): 
      self.automotora.append(a)

    def mostrar_autos(self): 
      for idx,i in enumerate(self.automotora): 
          print(idx,": \n  ")
          print(i)
    def borrar_autos(self,auto): 
        
        self.automotora.remove(auto)
        print(f"El Auto marca {auto.marca} ha sido borrado \n")




pocho=Auto("Volkswagen","Combi","Verde")
oso=Auto("Renault","Bingo","Rojo")
pantera=Auto("Kia","Besta","Blanca")

daniel=Automotora([Auto("VWK","Escarabajo","Lila"),Auto("Suzuki","Alto","Amarillo"),pocho,oso,pantera])

#daniel.borrar_autos(pocho)

daniel.mostrar_autos()

