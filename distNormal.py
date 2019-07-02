import matplotlib.pyplot as plt #Matplotlib es una biblioteca de trazado 2D de Python
import numpy as np #Paquete de matriz N-dimensional base
from scipy import stats #SciPy es una biblioteca libre y de código abierto para Python. Se compone de herramientas y algoritmos matemáticos.
import easygui as eg #libreria para emitir mensajes
import statistics as stat #libreria para calculos estadisticos


mu = eg.integerbox(msg='Entrada de la media:',
                    title='Distribución Normal',
                    default='',
                    lowerbound=0,
                    upperbound=99,
                    image=None)

sigma1 = eg.enterbox(msg='Entrada de la desviación estandar:',
                    title='Distribución Normal',
                    default='',
                    image=None)

sigma = float(sigma1)  # transformamos e valor de nuestra caja de string a float


# Enviamos los parametros a la dist. normarl que son la media y la desviación estandar
normal = stats.norm(mu, sigma)

#Eje x para la gráfica
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
print(x) # en el eje x de la gráfica

# Calculo de valores estadisticos media mediana, varianza y desviación estándar
media = str(stat.mean(x))
mediana = str(stat.median(x))


a = "Media",media,"\nMediana: ",mediana,"\nDesviación Estandar", sigma

#Eje y para la gráfica
fp = normal.pdf(x) # Función de Probabilidad - Función densidad de probabilidad
print(fp) # en el eje y de la gráfica
plt.plot(x, fp) # grafica en funcionde x e y
# leyendas para la gráfica
plt.title('Distribución Normal')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()
eg.msgbox(msg = a,
          title='Datos estadisticos en x', 
          ok_button='Continuar',
          image=None)

