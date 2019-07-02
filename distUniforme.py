import matplotlib.pyplot as plt #Matplotlib es una biblioteca de trazado 2D de Python
import numpy as np #Paquete de matriz N-dimensional base
from scipy import stats #SciPy es una biblioteca libre y de código abierto para Python. Se compone de herramientas y algoritmos matemáticos.
import easygui as eg #libreria para emitir mensajes
import statistics as stat #libreria para calculos estadisticos

# Graficando Uniforme
uniforme = stats.uniform()
x = np.linspace(uniforme.ppf(0.01),
                uniforme.ppf(0.99), 100)
fp = uniforme.pdf(x) # Función de Probabilidad
fig, ax = plt.subplots()
ax.plot(x, fp, '--')
ax.vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)
ax.set_yticks([0., 0.2, 0.4, 0.6, 0.8, 1., 1.2])
plt.title('Distribución Uniforme')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
# histograma
aleatorios = uniforme.rvs(1000) # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, 20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Uniforme')
plt.show()
mu = 5.0  
sigma = 2.0  
values = np.random.normal(mu, sigma, 10000)  
plt.hist(values, 50)  
plt.show() 