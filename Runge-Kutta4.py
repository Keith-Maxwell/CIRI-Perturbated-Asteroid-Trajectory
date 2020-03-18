import matplotlib.pyplot as plt
import math as m


# définition de la fonction RK4
def RK4(fonction, t0, tf, y0, n):
    """
        @author: dominique lefebvre - tangentex.com
        Cette fonction intégre le système d'EDO d'ordre 2 avec les paramètres suivants:
        - fonction : désigne la fonction de définition du système
        - dom : désigne le domaine d'intégration du système
        - xini, yini : conditions initiales du système
        - h : pas d'intégration sur le domaine La fonction retourne deux listes contenant les (xi,yi)
              de la courbe intégrale
    """
    h = (tf - t0) / n
    y = y0
    t = t0
    Y = [y0]
    T = [t0]
    for i in range(n):
        k1 = h * fonction(y, t)
        k2 = h * fonction(y + k1 / 2.0, t + h / 2.0)
        k3 = h * fonction(y + k2 / 2.0, t + h / 2.0)
        k4 = h * fonction(y + k3, t + h)
        y += (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        t = t + h
        T.append(t)
        Y.append(y)
    return T, Y


def f(y, t):
    return -y


y0 = 1
for n in [10, 100, 1000]:
    T, Y = RK4(f, 0, 10, y0, n)
    erreur1 = abs(Y[-1] - m.exp(-10))
    plt.plot(T, Y)
    print(erreur1)

plt.show()
