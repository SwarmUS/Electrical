import csv

import matplotlib.pyplot as plt
import numpy as np

with open('0A_HB5_P.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    datax = []
    datay = []
    x = []
    N = 1
    for row in reader:
        datax.append(float(row[0]))
        datay.append(float(row[1]))
        # print(row)

    moyenne = np.mean(datax)
    datay = np.convolve(datay, np.ones(N)/N, mode='valid')


    for data in datax:
        x.append(data-moyenne)

    plt.plot(x[0:1000], datay)
    plt.show()
