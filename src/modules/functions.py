import shutil
import os
import time
import traceback

categorias_archivos = {
    "imagen" : ["jpg", "jpeg", "png", "gif", "svg", "bmp", "webp"],
    "documentos" : ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt"],
    "videos" : ["mp4", "avi", "flv", "mov", "wmv", "mkv", "webm"],
    "musica" : ["mp3", "wav", "flac", "ogg", "wma", "aac"],
    "comprimidos" : ["zip", "rar", "7z", "tar", "gz", "bz2"],
    "ejecutables" : ["exe", "msi", "deb", "rpm"],
    "otros" : []
}

#crea las carpetas en la ruta especificada
def crear_carpetas(ruta):
    for carpeta in categorias_archivos.keys():
        ruta_carpeta = os.path.join(ruta, carpeta)
        print(f'Creando carpeta {ruta_carpeta}')
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)

#mueve los archivos a las carpetas correspondientes
def organizar_archivos(ruta):
    try:
        if not os.path.exists(ruta):
            print("La ruta especificada no existe")
            return
        crear_carpetas(ruta)

        for archivo in os.listdir(ruta):
            ruta_archivo = os.path.join(ruta, archivo)

            if os.path.isdir(ruta_archivo):
                continue 

            _, extension = os.path.splitext(ruta_archivo)
            archivo_movido = False

            for categoria, extensiones in categorias_archivos.items():
                if extension[1:] in extensiones:
                    ruta_carpeta = os.path.join(ruta, categoria)
                    shutil.move(ruta_archivo, ruta_carpeta)
                    archivo_movido = True
                    break
        print("Archivos organizados correctamente")
    except Exception as e:
        print(f"Ocurrió un error: {repr(e)}")
        traceback.print_exc()