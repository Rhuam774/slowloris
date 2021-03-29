from time import sleep
import matplotlib.pyplot as plt
y = []
x = []

while True:
    
    try:
        arquivo = open('pontos_G', 'r')
    except:
        exit()
    string = [] #----------------------------arquivo .txt virou uma string_lista
    for i in arquivo:
        string.append(str(i))#---------------= adicione cada item do arquivo para a estring
    for val in string:
        y.append(int(val))
    #===============================================================================================

    if len(x) < len(y):
        while len(x) != len(y):
            
            x.append(1+ len(x))
    plt.plot(x, y)
    plt.pause(2.0)

    





