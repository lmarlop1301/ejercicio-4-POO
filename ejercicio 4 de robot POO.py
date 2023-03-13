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

    funciona="si"
    def setfunciona(self,funciona):
        self.__funciona=funciona
    def getfunciona(self):
        return self.__funciona
    def alta(self):
        self.funciona="si"
    def baja(self):
        if self.funciona=="no":
            print ("el robot esta de baja")
        else:
            print ("el robot esta de alta")
class RobotDeCocina(Robot):  
    def __init__(self,temporizador,temperatura,nombre,ruedas,color,largo,ancho,funcion,habla,funciona):
        self.__temporizador=temporizador
        self.__temperatura=temperatura
        super().__init__(nombre,ruedas,color,largo,ancho,funcion,habla,funciona)
        self.habla=False
        self.temporizador=False
        self.temperatura=False
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
        funcion=input("su robot limpia?")
        if funcion.lower()=="si":
            posicion=input("que posicion tiene:")
            ruedas=input("cuantas ruedas quieres que tenga:")
            miRobot=RobotDeLimpieza(nombre,color,largo,ancho,funcion,posicion,ruedas)
        else:
            temporizador=input("tiene temporizador:")
            temperatura=input("tiene temperatura?:")
            miRobot=RobotDeCocina(nombre,color,largo,ancho,funcion,temporizador,temperatura)
        funciona=input("esta el robot funcionando?:")
        
        lista_caracteristicas_robot.append(miRobot)
        pregunta=input("desea introducir otro robot?")

    for x in range(0,len(lista_caracteristicas_robot)):
        print("su nombre es",lista_caracteristicas_robot[x].getnombre())
        print("tiene",lista_caracteristicas_robot[x].getruedas(), "ruedas")
        print("su color es",lista_caracteristicas_robot[x].getcolor())
        print("de largo tiene",lista_caracteristicas_robot[x].getlargo(),"cm")
        print("de ancho tiene",lista_caracteristicas_robot[x].getancho(),"cm")
        if funcion.lower()=="si":
            print("su robot limpia",lista_caracteristicas_robot[x].getfuncion())
            print("su posicion es",lista_caracteristicas_robot[x].getposicion())
        else:
            print("su robot limpia",lista_caracteristicas_robot[x].getfuncion(),"por lo que es un robot de cocina")
            print("tiene temperstura:",lista_caracteristicas_robot[x].gettemperatura())
            print("tiene temporizador",lista_caracteristicas_robot[x].gettemporizador())
        print("el robot funciona:",lista_caracteristicas_robot[x].getfunciona())
        print("tiene una posicion:",self.posicion)
        print("tiene temporizador:",self.temporizador)
        print("tiene temperatura:",self.temperatura)
      
        

