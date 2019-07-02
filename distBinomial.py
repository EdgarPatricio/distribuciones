import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import seaborn as sns
import easygui as eg

N = eg.integerbox(msg='Entrada de número entero mayor a 0 (N > 0):',
                    title='Distribución Binomial',
                    default='',
                    lowerbound=0,
                    upperbound=99,
                    image=None)

p1 = eg.enterbox(msg='Entrada de la probabilidad:',
                    title='Distribución Binomial',
                    default='',
                    image=None)

print(p1)

p = float(p1)        

np.random.seed(1) # replicar random

# parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

# Graficando Binomial
# parametros de forma para la distribución Binomial que es N (numeros de veces) y p(probabilida) que tiene que ser un valor entre 0 y  1

binomial = stats.binom(N, p) # Distribución

x = np.arange(binomial.ppf(0.01),
              binomial.ppf(0.99))

# Una función de probabilidad (también denominada función de masa de probabilidad) 
# es una función que asocia a cada punto de su espacio muestral X la probabilidad de que ésta lo asuma.
fmp = binomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()

# histograma
aleatorios = binomial.rvs(1000)  # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, 20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Binomial')
plt.show()