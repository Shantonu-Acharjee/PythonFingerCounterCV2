from pyfirmata import Arduino
import time

port = 'COM6'
board = Arduino(port)




def ledState(led1, led2, led3, led4, led5):

    board.digital[7].write(led1)
    board.digital[8].write(led2)
    board.digital[9].write(led3)
    board.digital[10].write(led4)
    board.digital[11].write(led5)
    #time.sleep(0.1)
            
 