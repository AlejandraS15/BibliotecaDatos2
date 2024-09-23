def busquedaGeneral(palabra):
    try:
        with open('Libros.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                if palabra.lower() in linea.lower():
                    nombre_libro = linea.split(',')[0]
                    print(nombre_libro)
    except FileNotFoundError:
        print(f"El archivo {'Libros.txt'} no fue encontrado.")

def busquedaPorCriterio(palabra, indice):
    try:
        with open('Libros.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                columnas = linea.split(',')
                if len(columnas) > indice:
                    if palabra.lower() in columnas[indice].lower():
                        nombre_libro = columnas[0]
                        print(nombre_libro)
    except FileNotFoundError:
        print("El archivo 'Libros.txt' no fue encontrado.")


if __name__ == '__main__':
    print("¡BIENVENIDO A TU BIBLIOTECA DIGITAL FAVORITA!")
    print("1. Deseas buscar general")
    print("2. Deseas buscar por criterio")
    print("3. Deseas salir del programa")
    opcion1 = int(input())

    while(opcion1 == 1 or opcion1 == 2):
        if(opcion1 == 1):
            print("Clave: tu clave es una palabra o palabras sin conectores de tu interes para buscarte el mejor libro")
            print("Ingrese una clave")
            palabras = str(input()).split()
            print("TE PODRIAN GUSTAR ESTOS LIBROS")
            for palabra in palabras:
                busquedaGeneral(palabra)

        else:
            if(opcion1 == 2):
                print("Ingresa por cual criterio quieres buscar")
                print("1.Titulo")
                print("2. Autor")
                print("3. Genero")
                print("4. Año de publicacion")
                print("5. Palabra en el resumen")
                opcion2 = int(input())
                if(opcion2==1 or opcion2==2 or opcion2==3 or opcion2==4 or opcion2==5):
                    if(opcion2==3):
                        print("Tu clave debe ser de los generos disponibles, los cuales son: Romance, Ficcion, Terror, Clasicos y académicos")

                    if(opcion2==4):
                        print("Si deseas ver la lista de los años de publicacion de los libros disponibles ingresa 1, sino ingresa 2")
                        opcion3 = int(input())
                        if(opcion3==1):
                            print('1813', '1897', '1949', '1967', '1859', '1847', '1818', '1925', '1916', '1605', '1862', '1890', '1985', '1897', '1977', '1943', '1851', '1869', '2007', '1927', '1869', '1947', '1986', '1974', '1980', '1989', '1963', '1995', '1915', '1954', '1988', '1866', '1320', '2003', '2008', '1985', '1953', '1985', '700', '750', '1977', '1982', '1864', '1968', '1926', '1998', '2001', '1970', '1946', '1981')

                    print("Clave: tu clave es una palabra o palabras sin conectores de tu interes para buscarte el mejor libro")
                    print("Ingrese una clave")
                    palabras = str(input()).split()
                    print("TE PODRIAN GUSTAR ESTOS LIBROS")
                    for palabra in palabras:
                        busquedaPorCriterio(palabra,opcion2-1)
                else:
                    print("Criterio invalido")

        print("¡BIENVENIDO A TU BIBLIOTECA DIGITAL FAVORITA!")
        print("1. Deseas buscar general")
        print("2. Deseas buscar por criterio")
        print("3. Deseas salir del programa")
        opcion1 = int(input())

    if(opcion1 == 3):
        print("Gracias por utilizar este programa, hasta pronto :)")
    else:
        print("Opcion invalida")