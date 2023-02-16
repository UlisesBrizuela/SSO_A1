#Actividad 1 - Seminario de solucion de problemas de sistemas operativos
#Brizuela Arias Ulises Israel


with open("prueba2.txt", "r") as Archivo, open("salida.txt", "a") as Salida:    #abro los archivos con with 1 para asegurar que esta abierto y 2 de esta forma el archivo se cierra solo al terminarse de usa
                                                                                #el archivo origen en modo lectura y el destino en modo append, para agregar siempre los registros al final del documento
    for Registros in Archivo:                                                   #con este for recorro cada linea del archivo individualmente
        Registro = Registros.split(",")                                         #separo cada linea en su correspondiente sub cadena delimitada por ,
        Hex = Registro[0].split("/")                                            #tomo el primer dato correspondiente a la cadena en HEX separandola primero por / para eliminar la basura                               
        HexaDec = " : ".join(str(int(h,16)) for h in Hex[0].split(":"))         #primero con el for se recorre la lista de los segmentos guardados en Hex[0] y los separa con split delimitados con :
                                                                                #con int(g, 16) convierto cada segmento individual en un entero y con srt se vuelve a convertir en cadena
                                                                                #para despues concatenar cada segmento ya convertido con un : usando el join
        Cadena = Registro[2]                                                    #tomo el siguiente dato y pasa directamente la cadena sin modificar
        Dec = Registro[5]                                                       #tomo el ultimo dato que corresponde a lo que parece una IP
        DecaHex = ".".join('{:02x}'.format(int(d)) for d in Dec.split('.'))     #con for recorro la lista de los datos resultantes de separar Dec con split
                                                                                #con int(g) convierto cada segmento indiviaul en un entero decimal 
                                                                                #y con {:02x}'.format decimos que cada sub elemento sera rellenado con ceros a dos caracteres en formato hexadecimal indicado por la x
                                                                                #al final con el join concateno los elementos con un . formando la nueva cadena
        Salida.write(Cadena+" : "+HexaDec+" : "+DecaHex+"\n")                   #escribo cada linea con las cadenas en el formato solicitado en la actividad