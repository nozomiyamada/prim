import numpy as np
import pandas as pd
import scipy as sp
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

person = input("person (a-h): " )

with open(f"duration_{person}.csv") as f1:
    d = list(csv.reader(f1))
with open(f"formant_{person}.csv") as f2:
    f = list(csv.reader(f2))

new = []
for i in f:
    new.append(i[1:3])
temp = []
for i in d:
    temp += i[:3]
for i, val in enumerate(temp):
    new[i].append(val)
new = np.array(new,dtype="float64")


fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")

# English: 0 - 35, 4 categories
lang = input("language e or t: ")
vowel = input("vowel i or u: ")

color_list = ["red","blue"]
if vowel == "i":
    if lang == "e":
        labels = ["/ɪ/", "/i/"]
    else:
        labels = ["/i/", "/i:/"]
else:
    if lang == "e":
        labels = ["/Ʊ/", "/u/"]
    else:
        labels = ["/u/", "/u:/"]
markers = ["o", "x"]

for i in range(2):
    if lang == "e":
        if vowel == "i":
            s = i * 9
        else:
            s = i * 9 + 18
    else:
        if vowel == "i":
            s = i * 9 + 36
        else:
            s = i * 9 + 54
    
    f1 = new[s:s+9,0]
    f2 = new[s:s+9:,1]
    du = new[s:s+9,2] * 1000

    ax.scatter(f2,f1,du,marker=markers[i], color=color_list[i], label=labels[i])
    ax.legend()
    ax.set_xlabel("F2")
    ax.set_ylabel("F1")
    ax.set_zlabel("duration [msec]")
    if vowel == "i":
        ax.set_xlim(1.2, 2.0)  # F2
        ax.set_ylim(0.5, 1.0)  # F1
    else:
        ax.set_xlim(0.3, 1.0)  # F2
        ax.set_ylim(0.5, 1.0)  # F1
    #ax.set_zlim(30, 180)
    if lang == "e":
        plt.title(f"Vowel Space and Duration of {person}")
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.view_init(elev=20, azim=-80)

fig.show()