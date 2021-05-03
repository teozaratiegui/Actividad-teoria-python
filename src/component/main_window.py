from src.windows import window
from src.handlers import datasets

def start():
    main_window = window.build()
    while True:
        result,event = main_window.read()
        if event in ("Salir","-Salir-"):
            break
        else:
            if event == "-opcion uno-":
                datasets.start("gun-violence-data",lambda crimen: crimen[2] == "California" and int(crimen[6])=>2)
                sg.popup("Archivo json creado con exito.")
            if event == "-opcion dos-":
                datasets.start("bestsellers with categories",lambda bestsellers: int(bestsellers[4])=>10 and bestsellers[6] == "Fiction")
                sg.popup("Archivo json creado con exito.")
    main_window.close()