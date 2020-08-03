import scipy
import numpy as np
import matplotlib.pyplot as plt
import sys

print("loaded")

# Ask old Le about this. We'll use group 10 for now
GROUP_NUM = 10

# Linux
PATH = "Signal_files/enel420_grp_{}.txt"
# Windows
#PATH = "Signal_files\enel420_grp_{}.txt"

    
def readData():
    try:
        dataRaw = open(PATH.format(GROUP_NUM))
    except FileNotFoundError():
        print("Please download and unzip signal files from learn")
        sys.exit()
        
    dataRaw = dataRaw.read().split(" ")
    
    return np.array([float(num) for i, num in enumerate(dataRaw) if num != ''])    
    
    
def plotSignal(signal, figureNum):
    plt.figure(figureNum)
    plt.plot(signal)
    plt.title("Raw Signal")
    plt.xlabel("Sample (n)")
    plt.ylabel("Sampled Amplitude")
    plt.show()
    
    
def main():
    
    signalRaw = readData()
    plotSignal(signalRaw, 0)
    
    

    
if __name__ == "__main__":
    main()