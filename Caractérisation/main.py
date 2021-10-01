import matplotlib.pyplot as plt
import numpy as np

import functions
color = ['#C7980A', '#F4651F', '#82D8A7', '#CC3A05', '#575E76', '#156943', '#0BD055', '#ACD338']
N=[]
x=[]
moyenne = []

file1x, file1y = functions.load_csv(filename='0A_HB5_P.csv')
file2x, file2y = functions.load_csv(filename='0B_HB5_P.csv')
file3x, file3y = functions.load_csv(filename='1A_HB5_P.csv')
file4x, file4y = functions.load_csv(filename='1B_HB5_P.csv')
# file5x, file5y = functions.load_csv(filename='2A_HB5_P.csv')
file6x, file6y = functions.load_csv(filename='2B_HB5_P.csv')

datax = [file1x, file2x,file3x,file4x,file6x]
datay = [file1y, file2y,file3y,file4y,file6y]

fig = plt.figure()
ax1 = fig.add_subplot(111)

for i in range(5):
    moyenne.append(np.mean(datax[i]))
    # plt.axvline(x=moyenne, color=color[i])
    ax1.scatter(datax[i], datay[i], s=3, label = i )

plt.ticklabel_format(axis='x',style='sci',scilimits=(-9,-9))
plt.xlabel(xlabel='secondes')
plt.legend(loc='upper left')
plt.show()



