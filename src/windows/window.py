import PySimpleGUI as sg

sg.theme("DarkRed")
texto_uno = "Obtener, dentro de un archivo de la nba del premio al mejor jugador de la semana, aquellos jugadores que pertenezcan a la conferencia este y jueguen de escolta"
texto_dos = "Obtener, dentro de los top 50 libros de amazon de los ultimos 10 años, los libros de ficcion con un precio mayor a los 10 dolares"
def build():
     layout_left = [[sg.Text(texto_uno,size=(35,4),justification = 'c')],
                   [sg.Button("Analizar archivo",key = "-opcion uno-",size = (30,4))],
                   [sg.Text("Dataset:\nNBA_player_of_the_week",size=(30,4),justification = 'c')]]

     layout_right = [[sg.Text(texto_dos,size=(35,4),justification = 'c')],
                    [sg.Button("Analizar top 50",key = "-opcion dos-",size = (30,4))],
                    [sg.Text("Dataset:\nBestsellers with categories",size=(30,4),justification = 'c')]]

     layout = [[sg.Text("Escoger datos a analizar",size=(50,4),justification = 'c')],
               [sg.Column(layout_left,element_justification='c'),sg.Column(layout_right, element_justification='c')],
               [sg.Button("Salir",key = "-Salir-")]]

     window = sg.Window('',layout,font=('Courier 12',16),element_justification='center',no_titlebar=True,grab_anywhere=True)
     return window
