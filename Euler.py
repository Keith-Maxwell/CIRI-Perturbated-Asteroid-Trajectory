import matplotlib.pyplot as plt
import math as m

#fonction exemple
def f(y, t):
    return -y


def euler(F, t0, tf, y0, n):
    """Données:
    F(y,t) une fonction
    t0,t1 deux réels avec t0 < t1
    y0 un réel
    n un entier
    Résultat: le tuple constitué de la liste des temps [t0,...,tn] et la liste des (n+1) réels [y_0, ...y_n]
    qui constituent une approximation de la solution y sur [t0,tf]
    de l’ED y’=F(y,t) avec la condition initiale y(t0) = y0
    """
    h = (tf - t0) / n
    y = y0
    t = t0
    Y = [y0]
    T = [t0]
    for k in range(n):  # n itérations donc n+1 points
        y = y + h * F(y, t)
        t = t + h
        Y.append(y)
        T.append(t)
    return T, Y


y0 = 1 #condition initiale
for n in [10, 100, 1000]: #on fait varier le nombre d'itérations, donc la précision
    T, Y = euler(f, 0, 10, y0, n)
    erreur1 = abs(Y[-1] - m.exp(-10)) #comparaison avec la solution analytique
    plt.plot(T, Y)
    print(erreur1)

plt.show()
