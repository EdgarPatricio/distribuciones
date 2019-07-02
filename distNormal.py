import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns
import easygui as eg 

# Graficando Normal
mu, sigma = 0, 0.2 # media y desvio estandar
normal = stats.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución Normal')
plt.ylabel('probabilidad')0.89376,0.89376, 0.97957, 0.07095, 0.07849, 0.080.89376,0.89376, 0.97957, 0.07095, 0.07849, 0.08
plt.xlabel('valores')
plt.show()

# histograma
aleatorios = normal.rvs(1000) # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, 20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Normal')
plt.show()