import numpy as np
import matplotlib.pyplot as plt


files = ["001.dat","002.dat","003.dat","004.dat","005.dat"]
for file in files:
    with open(file) as f:
        text = f.readlines()
        N = int(text[0])
        scatter = text[1 : N + 1]
        data_x = []
        data_y = []
        for elem in scatter:
            x, y = (float(e) for e in elem.split())
            data_x.append(x)
            data_y.append(y)
            
        fig, ax = plt.subplots()
        ax.scatter(data_x,data_y,
                   marker = 'o',
                   c = 'magenta')
        ax.set_title("Number of points: %s" % N)
        fig.set_figwidth(8)
        fig.set_figheight(8)
        plt.show()
        
