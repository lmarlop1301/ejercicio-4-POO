class Robot():
    def __init__(self,nombre,ruedas,color,largo,ancho,funcion,posicion,habla):
        self.__nombre=nombre
        self.__ruedas=ruedas
        self.__color=color
        self.__largo=largo
        self.__ancho=ancho
        self.__funcion=funcion
        self.__posicion=posicion
        self.__habla=habla   
    def setnombre(self,nombre):
        self.__nombre=nombre
    def getnombre(self):
        return self.__nombre
    def setruedas(self,ruedas):
        self.__ruedas=ruedas
    def getruedas(self):
        return self.__ruedas
    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color
    def setlargo(self,largo):
        self.__largo=largo
    def getlargo(self):
        return self.__largo
    def setancho(self,ancho):
        self.__ancho=ancho
    def getancho(self):
        return self.__ancho
    def setfuncion(self,funcion):
        self.__funcion=funcion
    def getfuncion(self):
        return self.__funcion
    def setposicion(self,posicion):
        self.__posicion=posicion
    def getposicion(self):
        return self.__posicion
    def sethabla(self,habla):
        self.__habla=habla
    def gethabla(self):
        return self.__habla
    
class RobotDeCocina(Robot):  
    def __init__(self,temporizador,temperatura,nombre,ruedas,color,largo,ancho,funcion,posicion,habla):
        self.__temporizador=temporizador
        self.__temperatura=temperatura
        super().__init__(nombre,ruedas,color,largo,ancho,funcion,posicion,habla)
    def settemporizador(self,temporizador):
        self.__temporizador=temporizador
    def gettemporizador(self):
        return self.__temporizador
    def settemperatura(self,temperatura):
        self.__temperatura=temperatura
    def gettemperatura(self):
        return self.__temperatura
if __name__=="__main__":
    lista_caracteristicas_robot = []
    pregunta=input("desea introducir otro robot?")
    while pregunta=="si":
        nombre=input("que nombre tiene el robot:")
        ruedas=input("cuantas ruedas quieres que tenga:")
        color=input("de que color quieres que sea en robot:")
        largo=input("que largo quieres que tenga tu robot:")
        ancho=input("que ancho quieres que tenga el robot:")
        funcion=input("cual es su funcion?")
        posicion=input("que posicion tiene:")
        habla=input("el robot habla?")
        temporizador=input("tiene temporizador:")
        temperatura=input("que temperatura tiene:")
        miRobot=RobotDeCocina(temporizador,temperatura,nombre,ruedas,color,largo,ancho,funcion,posicion,habla)
        lista_caracteristicas_robot.append(miRobot)
        pregunta=input("desea introducir otro robot?")
           
    for x in range(0,len(lista_caracteristicas_robot)):
        print(lista_caracteristicas_robot[x].getnombre())
        print(lista_caracteristicas_robot[x].getruedas())
        print(lista_caracteristicas_robot[x].getcolor())
        print(lista_caracteristicas_robot[x].getlargo())
        print(lista_caracteristicas_robot[x].getancho())
        print(lista_caracteristicas_robot[x].getfuncion())
        print(lista_caracteristicas_robot[x].getposicion())
        print(lista_caracteristicas_robot[x].gethabla())
        print(lista_caracteristicas_robot[x].gettemperatura())
        print(lista_caracteristicas_robot[x].gettemporizador())
      
        
