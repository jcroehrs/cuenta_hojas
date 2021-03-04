from PyPDF2 import PdfFileReader
import argparse
import os


def extraer_information(pdf_ubicacion):
    with open(pdf_ubicacion, 'rb') as f:
        pdf = PdfFileReader(f)
        informacion = pdf.getDocumentInfo()
        numero_de_paginas = pdf.getNumPages()

    Resumen = f""" Archivo {pdf_ubicacion}:     Paginas: {numero_de_paginas} """

    print(Resumen)
    return informacion, numero_de_paginas


if __name__ == '__main__':
    total_de_paginas = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--ejemplo",
                        help="Muestra un ejemplo", action="store_true")
    parser.add_argument("-f", "--fila", help="Nombre de archivo a procesar")
    parser.add_argument(
        "-d", "--directorio", help="Busca todos los archivos PDF del directorio actual o en otro directorio")
    args = parser.parse_args()

    # Aquí procesamos lo que se tiene que hacer con cada argumento

    if args.ejemplo:
        print("contar -f <archivo>.pdf")
        print("contar -d <ruta de la carpeta donde se encuentran los pdf>")
        print('Si esta en la carpeta : contar -d ./')

    if args.fila:
        extraer_information(args.fila)

    if args.directorio:
      #  obtiene el contenido del directorio
        directorio_def = args.directorio  # toma el directorio pasado por parametro
        # lee el contenifo de la carpeta
        contenido = os.listdir(directorio_def)
        pdfs = []
        for fichero in contenido:  # recorre el contenido del directorio para identificar los archivos PDF
            if os.path.isfile(os.path.join(directorio_def, fichero)) and fichero.endswith('.pdf'):
                pdfs.append(fichero)

        for ARCHIVO in pdfs:  # Recorremos la lista de Archivos PDF y sacamos las hojas
            datosgenerales, paginas_parcial = extraer_information(
                directorio_def+ARCHIVO)
            total_de_paginas = total_de_paginas + int(paginas_parcial)

    if total_de_paginas > 0:
        print(' El total de paginas en esta carpeta es de: ', total_de_paginas)
