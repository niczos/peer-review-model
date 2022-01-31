# Modelowanie procesu recenzji w czasopismach naukowych
Opiekun: dr Maciej J. Mrowiński

Autor: Nika Jurczuk
#### Wymagania potrzebne do uruchomienia programu:
- ######  Python 3.9
- ###### Jupyter Notebook
- ###### Zainstalowane biblioteki:
    - numpy
    - matplotlib
    - random
    - enum
    - tqdm
    - operator
    - itertools

Niniejszy kod pozwala na zaimplementowanie modelu recenzji naukowej *peer review* oraz przeprowadzenie symulacji dotyczących zachowania tego modelu. Wyniki przedstawiono w postaci wykresów oraz histogramów. 

Kod podzielony jest na 3 pliki. 

Plik `randoms.py` przeprowadza symulację wprowadzając do układu recenzentów niewiarygodnych. Wyznaczane są zasoby agentów po jednej symulacji, a także parametry opisujące układ:
- wskaźnik Giniego,
- stronniczość oceny,
- liczba autorów, którzy nie opublikowali żadnego artykułu,
- różnica między zasobami agenta a średnią zasobów.

Plik `cheaters.py` przeprowadza identyczną symulację wprowadzając do układu recenzentów nieuczciwych.
### Parametry, testowane w trakcie testowania modelu:
- odchylenie standardowe przy przypisywaniu jakości artykułowi
- parametr skalujący *a*
- początkowe zasoby agenta *R0*
- stałe zasoby dodawane po każdym kroku każdemy agentowi *R+*
- sposób dodawania zasobów po udanej publikacji

Sposób dodawania zasobów po udanej publikacji można zmienić w funkcji `update_R()`, gdzie w miejscu dodawania zasobów pomnożonych przez parametr *m* można ustawić dowolną liczbę. Resztę powyższych parametrów można modyfikować w drugiej komórce kodu.

Plik `scale_function.py` przedstawia funkcję skalującą zasoby po udanej publikacji w zależności od parametru *a*.
