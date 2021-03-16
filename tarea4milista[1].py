#A continuación veremos cómo crear una lista, y darle valores a dicha lista.

milista = [ "Rachel", "Lyan", "Nahu", "Isabel" ]
print(milista[:]) 
print(milista[2])
print(milista[0:3])
print(milista[:3])
print(milista[3:])

#El siguiente bloque es para añadir elementos a una lista.

milista.append("Cammie")
print(milista[:])

#Para insertar elementos en una posición determinada

milista.insert(1,"Melania")
print(milista[:])

#Para agregar varios elementos

milista.extend(["Sofía", "Bianca"])
print(milista[:])