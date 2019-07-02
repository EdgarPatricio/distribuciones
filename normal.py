import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns 
import statistics as stat #libreria para calculos estadisticos
import easygui as eg


np.random.seed(2016) # replicar random

# parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
# Graficando histograma
mu, sigma = 5, 0.2 # media y desvio estandar

# histograma de distribución normal.
cuenta, cajas, ignorar = plt.hist(datos, 20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')
plt.show()


