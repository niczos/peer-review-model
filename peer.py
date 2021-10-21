import numpy as np
import operator

N = 10  # liczba agentow
N_a = int(N/2)  # liczba autorow
R_max = 1  # max liczba zasobów 
alfa_R = 1  # const. współczynnik do określania Q
Q_sigma = 0.1  # odchylenie standardowe Q
Q_est_sigma = 0.01 # odchylenie standardowe estymowanej Q
N_p = 3  # liczba opublikowanych artykułów
a = 1.2  # mnoznik zasobow

list_of_scientists = []

class Scientist:
    def __init__(self, id, R, Rp):
        self.id = id
        self.R = R  # zasoby agenta
        self.R_p = Rp  # zasoby przeznaczone na publikacje
        self.pubs = []  # lista opublikowanych prac
        self.est = []  # lista zrecenzowanych prac

    def add_pub(self,p):  # dodanie pracy do autora
        self.pubs.append(p)

    def add_est(self,p):  # dodanie pracy do recenzenta
        self.est.append(p)


class Publication:
    def __init__(self, auth_id, Q, ref_id, Q_est, status, i):
        self.auth_id = auth_id  # id autora
        self.Q = Q  # jakosc publikacji
        self.ref_id = ref_id  # id recenzenta 
        self.Q_est = Q_est  # estymowana jakosc publikacji
        self.status = status  # True - opublikowana, False - nieopublikowana
        self.i = i  # numer kroku symulacji 

def set_R():  # poczatkowe zasoby agenta
    global R
    R = np.random.uniform(0,R_max)
    return R

def set_Rp(): # zasoby przeznaczone na publikacje
    Rp = R
    return Rp

def set_Q(author): # ustawienie jakosci publikacji
    global Q_mean
    Q_mean = alfa_R*author.R/(alfa_R*author.R+1)
    Q = np.random.normal(Q_mean, Q_sigma)
    return Q

def set_Q_est(referee): # ustawienie jakosci przez recenzenta
    Q_est_mean = Q_mean 
    Q_est = np.random.normal(Q_est_mean, Q_est_sigma)
    return Q_est
 
def update_R(author, publication, referee):  # Update zasobów po publikacji
    if publication.status == True:
        author.R = author.R*a
    else:
        author.R = 0  # nieopublikowana traci cale zasoby
    referee.R = 0  # recenzent poswieca cale zasoby na recenzowanie

for i in range(N):  # stworzenie agentów i ustawienie zasobów
    i = Scientist(i,set_R(),set_Rp())
    list_of_scientists.append(i)


class Simulation:
    def __init__(self,set_Q,set_Q_est,update_R):
        self.set_Q = set_Q
        self.set_Q_est = set_Q_est
        self.update_R = update_R

    def function(self,x):  # x - krok symulacji

        authors = []
        referees = []
        publications = []
        published = []
        unpublished = []

        authors.clear()
        referees.clear()
        publications.clear()

        # mieszanie agentów w celu losowego podziału na autorów i recenzentów
        np.random.shuffle(list_of_scientists)

        # Lista autorów i recenzentów
        for i in range(N_a,N):  # podział po połowie na autorów i recenzentów
            referees.append(list_of_scientists[i])
        for i in range(N_a):
            authors.append(list_of_scientists[i])
            p = Publication(authors[i].id, self.set_Q(authors[i]), referees[i].id, self.set_Q_est(referees[i]),False,x) # stworzenie publikacji
            publications.append(p)
            list_of_scientists[i].add_pub(p)  # dodanie pracy do autora
            list_of_scientists[i+N_a].add_est(p)  # dodanie pracy do recenzenta

        # Sortowanie publikacji malejąco
        sorted_pub = sorted(publications,key=operator.attrgetter('Q_est'), reverse = True)

        # Lista opublikowanych i nieopublikowanych artykułów
        for i in range(N_p):
            published.append(sorted_pub[i])
            sorted_pub[i].status = True

        for i in range(N_p,N_a):
            unpublished.append(sorted_pub[i])

        for x,y,z in zip(authors, publications, referees):
            self.update_R(x,y,z)  # update zasobów

        ############### PRINTY ###################
        print("\n AUTHORS:")
        for i in authors:
            print(vars(i))
        print("\n REFEREES:")
        for i in referees:
            print(vars(i))
        print("\n PUBLICATIONS:")
        for i in publications:
            print(vars(i))
        print("\n PUBLISHED:")
        for i in published:
            print(vars(i))
        print("\n UNPUBLISHED:")
        for i in unpublished:
            print(vars(i))
        print("\n Author's publications")
        for i in list_of_scientists:
            print(f'\n Agent {i.id}:')
            print(f'AUTHOR:')
            for p in i.pubs:
                print(vars(p))
            print(f'REFEREE:')
            for e in i.est:
                print(vars(e))
  
s = Simulation(set_Q,set_Q_est,update_R)  # obiekt symulacji (jak wykorzystujemy parametry? - tu coś chyba nie gra)

# 3 kroki symulacji
for i in range(3): 
    s.function(i+1) 

