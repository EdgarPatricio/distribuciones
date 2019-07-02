import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns
import easygui as eg
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

print(sigma1)

sigma = float(sigma1)  

# Graficando Normal
# mu, sigma = 0, 0.2 # media y desvio estandar
normal = stats.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
print(x) # en el eje x de la gráfica

# Calculo de valores estadisticos media mediana, varianzay desviación estándar

media = str(stat.mean(x))
mediana = str(stat.median(x))
varianza = stat.pvariance(x)
desv = str(stat.pstdev(x))
a = "Media",media,"\nMediana: ",mediana, "\nVarianza Poblacional: ",varianza,"\nDesviacion Estandar: ",desv



fp = normal.pdf(x) # Función de Probabilidad
print(fp) # en el eje y de la gráfica
plt.plot(x, fp) # grafica en funcionde x e y
# leyendas para la gráfica
plt.title('Distribución Normal')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()
eg.msgbox(msg = a,
          title='Control: msgbox', 
          ok_button='Continuar',
          image=None)

# histograma
aleatorios = normal.rvs(1000) # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, 20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Normal')
plt.show()