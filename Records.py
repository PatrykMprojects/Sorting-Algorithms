import random
import numpy as np


def create():
    distance = []
    time = []
    r = {}
    rec0 = {}
    rec1 = {}
    rec2 = {}
    rec3 = {}
    rec4 = {}
    rec5 = {}
    rec6 = {}
    rec7 = {}
    rec8 = {}
    d = []
    stop = 'S'
    fin = 'F'

    x = np.random.randint(200, 500, size=(9,))
    while sum(x) != 3000:
        x = np.random.randint(200, 500, size=(9,))
    y = np.random.randint(80, 220, size=(9,))
    while sum(y) < 980:
        y = np.random.randint(80, 220, size=(9,))

    distance.append(x)
    time.append(y)

    for i in distance:
        for j in time:
            rec0[i[0]] = j[0]
            rec1[i[1]] = j[1]
            rec2[i[2]] = j[2]
            rec3[i[3]] = j[3]
            rec4[i[4]] = j[4]
            rec5[i[5]] = j[5]
            rec6[i[6]] = j[6]
            rec7[i[7]] = j[7]
            rec8[i[8]] = j[8]
            d.append(rec0)
            d.append(stop)
            d.append(rec1)
            d.append(stop)
            d.append(rec2)
            d.append(stop)
            d.append(rec3)
            d.append(stop)
            d.append(rec4)
            d.append(stop)
            d.append(rec5)
            d.append(stop)
            d.append(rec6)
            d.append(stop)
            d.append(rec7)
            d.append(stop)
            d.append(rec8)
            d.append(fin)

    return d


def numb():
    participants = {}

    k = 'p'
    for i in range(100):
        create()
        participants[k + str(i + 1)] = create()

    return participants


numb()
