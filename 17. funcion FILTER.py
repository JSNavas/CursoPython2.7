def filtro(elemento):
	return (elemento > 0)

l = [1,-3,-2,4,6,7,-9,-5]

filtrar = filter(filtro,l)

print l
print filtrar