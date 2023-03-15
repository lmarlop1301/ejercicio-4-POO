class Robot():
    def __init__(self,nombre,color,largo,ancho,funcion,funciona):
        self.__nombre=nombre
        self.__color=color
        self.__largo=largo
        self.__ancho=ancho
        self.__funcion=funcion
        self.__funciona=funciona
    def setnombre(self,nombre):
        self.__nombre=nombre
    def getnombre(self):
        return self.__nombre
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

    def setfunciona(self,funciona):
        self.__funciona=funciona
    def getfunciona(self):
        return self.__funciona
    
class RobotDeCocina(Robot):  
    def __init__(self,temporizador,temperatura,nombre,color,largo,ancho,funcion,funciona):
        self.__temporizador=temporizador
        self.__temperatura=temperatura
        super().__init__(nombre,color,largo,ancho,funcion,funciona)
        
    def settemporizador(self,temporizador):
        self.__temporizador=temporizador
    def gettemporizador(self):
        return self.__temporizador
    def settemperatura(self,temperatura):
        self.__temperatura=temperatura
    def gettemperatura(self):
        return self.__temperatura
    def temporizador(self):
        self.temporizador=True
    def temperatura(self):
        self.temperatura=True
    
class RobotDeLimpieza(Robot):
    def __init__(self,posicion,ruedas,nombre,color,largo,ancho,funcion,funciona):
        self.__posicion=posicion
        self.__ruedas=ruedas
        super().__init__(nombre,color,largo,ancho,funcion,funciona)
    def posicion(self):
        self.posicion=True
    def setposicion(self,posicion):
        self.__posicion=posicion
    def getposicion(self):
        return self.__posicion
    def setruedas(self,ruedas):
        self.__ruedas=ruedas
    def getruedas(self):
        return self.__ruedas
        
    
if __name__=="__main__":
    lista_caracteristicas_robot = []
    pregunta=input("desea introducir otro robot?")
    while pregunta.lower() != "no" and pregunta.lower() != "si":
        pregunta=input("desea introducir otro robot?")
        
    
    while pregunta.lower()=="si":
        nombre=input("que nombre tiene el robot:")
        color=input("de que color quieres que sea en robot:")
        largo=input("que largo quieres que tenga tu robot:")
        ancho=input("que ancho quieres que tenga el robot:")
        pregunta2=input("su robot limpia?")
        funciona=input("esta el robot funcionando?:")
        funcion="1"
        if pregunta2.lower()=="si":
            funcion="limpia"
            posicion=input("que posicion tiene:")
            ruedas=input("cuantas ruedas quieres que tenga:")
            miRobot=RobotDeLimpieza(posicion,ruedas,nombre,color,largo,ancho,funcion,funciona)
        else:
            funcion="cocina"
            temporizador=input("tiene temporizador:")
            temperatura=input("tiene temperatura?:")
            miRobot=RobotDeCocina(temporizador,temperatura,nombre,color,largo,ancho,funcion,funciona)
        
        
        lista_caracteristicas_robot.append(miRobot)
        pregunta=input("desea introducir otro robot?")

    for x in range(0,len(lista_caracteristicas_robot)):
        print("su nombre es",lista_caracteristicas_robot[x].getnombre())
        print("su color es",lista_caracteristicas_robot[x].getcolor())
        print("de largo tiene",lista_caracteristicas_robot[x].getlargo(),"cm")
        print("de ancho tiene",lista_caracteristicas_robot[x].getancho(),"cm")
        if lista_caracteristicas_robot[x].getfuncion()=="limpia":
            print("su robot",lista_caracteristicas_robot[x].getfuncion())
            print("su posicion es",lista_caracteristicas_robot[x].getposicion())
            print("tiene",lista_caracteristicas_robot[x].getruedas(), "ruedas")
        else:
            print("su robot ",lista_caracteristicas_robot[x].getfuncion())
            print("tiene temperatura:",lista_caracteristicas_robot[x].gettemperatura())
            print("tiene temporizador",lista_caracteristicas_robot[x].gettemporizador())
            print("el robot esta de alta?",lista_caracteristicas_robot[x].getfunciona())
                    

