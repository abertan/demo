#### Codigo Python
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
#### Codigo R
import rpy2
print(rpy2.__version__)
import rpy2.situation
for row in rpy2.situation.iter_info():
    print(row)
import rpy2.robjects as r
from rpy2.robjects.packages import importr
base = importr('base')

r('print("¡Hola Mundo!... desde lenguaje R")')
print ('Ejemplo de suma')
r('''
suma <- 0
for (i in 1:10) {
  suma <- suma + i
}
print(suma)
''')
print ('Asignar 10 a x en R')
r.assign('x', 10)
print ('Imprimir el valor de x en R')
r('print(x)')
print ('Operar con x y recuperar el valor')
r('y <- x * 3')
r('print(y)')
y = r('y')
print(y[0])


print ('Uso de matrix desde R')
import numpy as np
from rpy2.robjects import numpy2ri
numpy2ri.activate()
    
x = r.matrix(np.array(range(9)), nrow=3, ncol=3)
r.assign('x', x)
r('print(x)')

def multi(num):
    r.assign('x', num)
    r('y <- x * 3')
    r('print(y)')
    y = r('y')
    return y.astype(int)

class AnaliticaService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def consulta(ctx, nombre, repeticiones):
        cantidad = multi(repeticiones)
        for i in range(cantidad[0]):
            yield 'Hola, %s' %nombre
consultaEvaluacion = Application([AnaliticaService],
    tns='com.ibm.mca.analitica',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(consultaEvaluacion)
    server = make_server('0.0.0.0', 8080, wsgi_app)
    server.serve_forever()
