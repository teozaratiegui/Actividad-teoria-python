from src.windows import window

def start():
    while True:
        main_window = window.build()
        result,event = main_window.read()
        if (())