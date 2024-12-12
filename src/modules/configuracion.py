import configparser
import time
import datetime
import pyodbc

def configs():
    config = configparser.ConfigParser()
    config.read("config.ini")

    #[Rutas]
    ruta_log = config["Rutas"]["ruta_log"]

    dict_conf = {
        "ruta_log": ruta_log
    }

    return dict_conf

def escribe_log(mensaje):
    with open(configs()['ruta_log'], "a") as file:
        file.write(f"{time.ctime()} - {mensaje}\n")

def obtiene_fecha():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")