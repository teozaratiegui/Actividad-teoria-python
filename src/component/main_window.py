from src.windows import window
from src.handlers import datasets
import PySimpleGUI as sg

def start():
    main_window = window.build()
    while True:
        event,result = main_window.read()
        if event in ("Salir","-Salir-"):
            break
        else:
            if event == "-opcion uno-":
                datasets.start("NBA_player_of_the_week",lambda week: week[2] == "East" and week[4]== "SG")
                sg.popup("Archivo json creado con exito.")
            if event == "-opcion dos-":
                datasets.start("bestsellers with categories",lambda bestsellers: int(bestsellers[4])>9 and bestsellers[6] == "Fiction")
                sg.popup("Archivo json creado con exito.")
    main_window.close()
