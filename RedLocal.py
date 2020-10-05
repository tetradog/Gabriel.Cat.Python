import socket
import String
import Scan
import ipaddress
import sys
import threading

import Serializar

class Response:
    def __init__(self,idFunc=0,data=[]):
        self.IdFunction=idFunc
        self.Data=data

    def GetBytes(self):
        serializador=Serializar.GetSerialitzer(self)
        return serializador.Serializar(self)

    @staticmethod
    def Load(emptyObj,objData):
        return Serializar.GetSerialitzer(emptyObj).Desserializar(emptyObj,objData)

class Red:

    def __init__(self):
        self.dicFunc={}
        self.dicSocket={}
        self.dicHilos={}
        self.MyIP=Red.GetMyIP()


    def Listen(self,port,function):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hilo=threading.Thread(target=self._Listen, args=(port,s), daemon=False)
        self.dicFunc[port]=function
        self.dicSocket[port]=s
        self.dicHilos[port]=hilo
        hilo.start()
        return s

    def _Listen(self,port,s):
        s.bind((self.MyIP,port))
        s.listen(1)
        while True:
            connection, client_address = s.accept()
            self.dicFunc[port](connection, client_address)

    def Stop(self,port):
        isStopit=port in self.dicHilos
        if isStopit:
            self.dicHilos[port].terminate()
            self.dicSocket[port].close()
            self.dicFunc.pop(port)
            self.dicSocket.pop(port)
            self.dicFunc.pop(port)
        return isStopit

    def StopAll(self):
        for port in self.dicFunc.keys():
            self.Stop(port)
    @staticmethod
    def Send(ip,port,data,idFunc=None):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))

        if idFunc is None:
            if data.__class__.__name__=="".__class__.__name__:
                data=data.encode()
        else:
            data=Response(idFunc,data).GetBytes()

        s.send(data)
    @staticmethod
    def GetMyIP():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def GetAllIPs(port=55557):
        ip=GetMyIP()

        if ip[-3]=='.':
            local=int(ip[-2:])
            prefijo=ip[:-3]
        elif ip[-2]=='.':
            local=int(ip[-1:])
            prefijo=ip[:-2]
        else:
            local=int(ip[-1])
            prefijo=ip[:-1]
        ips=[]
        for i in range(1,254):
            ip=prefijo+str(i)
            try:
                if i!=local and Scan.IsOpen(ip,port):
                    ips.append(ip)
            except:
                print(i)

        return ips

def PrintRespuesta(s,e):
    print("recivido",s,e)

port=99
red=Red()
print(red.Listen(port,PrintRespuesta))
Red.Send('127.0.0.1',port,"Hola")
red.Stop(port)
Red.Send(red.MyIP,port,"Hola2")