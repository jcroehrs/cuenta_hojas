import argparse
import os
from PyPDF2 import PdfFileReader


def extraer_information(pdf_ubicacion):
    with open(pdf_ubicacion, 'rb') as f:
        pdf = PdfFileReader(f)
        informacion = pdf.getDocumentInfo()
        numero_de_paginas = pdf.getNumPages()

    Resumen = f"""
    Archivo {pdf_ubicacion}:     Paginas: {numero_de_paginas} """

    print(Resumen)
    return informacion


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--ejemplo",
                        help="Muestra un ejemplo", action="store_true")
    parser.add_argument("-f", "--fila", help="Nombre de archivo a procesar")
    args = parser.parse_args()
    # Aquí procesamos lo que se tiene que hacer con cada argumento
    if args.ejemplo:
        print("contar -f <archivo>.pdf")
    if args.fila:
        extraer_information(args.fila)
