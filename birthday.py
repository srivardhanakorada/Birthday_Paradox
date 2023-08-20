import numpy as np
import matplotlib.pyplot as plt

def drawparadox(n):
    res = [1]*(n+1)
    for i in range(1,n+1):
        res[i] = (res[i-1]*(365-i+1))/(365)
    for i in range(1,n+1):
        res[i] = 1 - res[i]
    temp = []
    temp.extend(range(1,n+1))
    xpoints = np.array(temp)
    ypoints = np.array(res[1:])
    plt.plot(xpoints,ypoints,"X")
    plt.title("Birthday Paradox",fontsize=20)
    plt.xlabel("Group Size")
    plt.ylabel("Probability of two people in the group having same birthday")
    plt.show()

if __name__ == "__main__":
    drawparadox(50)