'''
    Funkcja skalująca zasoby agenta po udanej publikacji artykułu
    proporcjonalnie do aktualnych zasobów - porównanie
    zachowania funkcji dla różnych wartości parametru skalującego a.
'''

import matplotlib.pyplot as plt
import numpy as np

# porównanie dwóch parametrów
a = 0.5
b = 0.005

X = np.arange(0, 1000, 1)

# funkcje skalujące
y = X*a/(a*X+1)
z = X*b/(X*b+1)
  
plt.plot(X, y, color='r', label='a=0.5')
plt.plot(X, z, color='g', label='a=0.005')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Funkcja skalująca zasoby po udanej publikacji artykułu")

plt.legend()
plt.savefig('scale_function.pdf')
plt.show()