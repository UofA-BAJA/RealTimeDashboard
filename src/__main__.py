
from data.database_wrapper_class import Database_Wrapper
from serial.port import Port
from widgets.mainwidgets import setupApp, showapp
#beep boop bop
SCREEN_SCALAR = 2
'''
SCREEN SCALAR LETS YOU CHOOSE HOW BIG THE WINDOW IS WHILE DEVELOPING
    width, height
0 = 800, 480
1 = 1600, 960
2 = 2400, 1440
'''

def main():

    d = Database_Wrapper()

    d.create_table_if_not_exists()

    ex, app = setupApp(SCREEN_SCALAR)

    showapp(ex, app)


if __name__ == '__main__':
    main()
    