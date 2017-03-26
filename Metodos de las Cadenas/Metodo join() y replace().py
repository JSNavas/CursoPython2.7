#Funcion join y replace

saludo = ["hola", "como","esta","Sr. Navas"]

espacio = " "       # Se crea una variable con el
                    # dato que queremos agregar al
                    # final de cada elemento de la lista 

mostrar = espacio.join(saludo)  # la funcion join se utiliza colocando
                                # la variable donde se guarda el dato
                                # seguido de ".join()" y dentro de los
                                # parentesis la lista a la que le queremos
                                # agregar tal dato.

nombre = raw_input("Ingrese nombre del invitado: ")

print mostrar
print mostrar.replace("Navas",nombre)   # Se utiliza el ".replace()" despues de la cadena
                                        # a la cual le quermos reemplazar un dato
                                        # y dentro de los parentesis de replace se coloca  
                                        # primero lo que va a buscar, y luego lo que va a
                                        # reemplazar.
