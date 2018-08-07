#just example of pandas script
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def main():    
    some = pd.read_csv("persons.csv", encoding = "ISO-8859-1")
    values = some.values        #as an array
    #print(some)
    ages = some.iloc[:,5]       #get 5th columns
    names_len = [len(item) for item in list(some.iloc[:,0])]
    surnames_len = [len(item) for item in list(some.iloc[:,1])]
    fig = plt.figure(figsize=(10, 6))
    ax = fig.gca()
    ax.set_title("Histogram example")

    df = pd.DataFrame({'age': ages, 'surnames_len': surnames_len, 'names_len': names_len})
    df.plot.hist(alpha=0.65, ax=ax)
    ax.set_xlabel("things values")
    ax.set_ylabel("number of things")
    plt.show()
    return True
    
    
if __name__ == "__main__":
    path = script_path()
    main()
    
    