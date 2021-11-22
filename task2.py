import numpy as np
import matplotlib.pyplot as plt

file = "frames.dat"
with open(file) as f:
    text = f.readlines()
data_x = []
data_y = []
i = 0  
j = 1  #Number of frame
fig = plt.figure()
fig.set_figwidth(11)
fig.set_figheight(11)
while i < len(text):     
    data_x.append([float(e) for e in text[i].split()])
    data_y.append([float(e) for e in text[i+1].split()])
        
    ax = fig.add_subplot(3, 2, j)
    ax.scatter(data_x, data_y)  #Doesn't work with ax.plot
    ax.set_xlim(-2, 18)
    ax.set_ylim(-15, 15)
    ax.set_title("Frame: %s" % j)
    ax.grid()
    
    plt.show()
    
    data_x = []
    data_y = []    
    i += 2
    j += 1