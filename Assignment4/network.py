

___________#ASSIGNMENT 4____________



#I am starting off with importing necessary packages 
import os
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm
import spacy
nlp = spacy.load("en_core_web_sm")
import argparse


# and importing packages for drawing
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)



#command line pop-up information & getting the file 
def getting_file():
    ap = argparse.ArgumentParser(description = "Creating a network")
    #argument -p for getting the file
    ap.add_argument("-p","--filename",required = True, type = str, help ="please, provide a name of your weighted-edgelist document. Type '-p' in front of your filename")
    #argument -f for getting the weight threshold
    ap.add_argument("-t","--threshold",required = False, type = int, default= 500, help = "please, provide a weight threshold you want to use. Type '-t' in front of the number. The default value is 500.")
    
    args = vars(ap.parse_args())
    filename = args['filename']
    threshold = args['threshold']

    return(filename,threshold)
    
#defining main function 

def main():
    
    #printing the info about the file and specified thereshold 
    filename, threshold = getting_file()
    print(f"this is the file you are using : {filename}, and your threshold is {threshold}")
    
    #creating a data frame from the file
    filepath = os.path.join("data",filename)
    data = pd.read_csv(filepath)
    
    
    #filtering based on the specified threshold
    filtered = data[data["weight"] > int(threshold)]
    print("it works")
    
    #creating the network graphic with nodes and their respective weights 
    G = nx.from_pandas_edgelist(filtered, 'nodeA', 'nodeB', ["weight"])
    
    #specifying the output path where the graph is saved
    outpath_viz = os.path.join('viz',' network.png')
    
    # Plotting and saving the plot in the output folder 
    nx.draw_shell(G, with_labels = True, font_weight = 'bold') 
    plt.savefig(outpath_viz, dpi = 300, bbox_inches ="tight")
    
    #creating a data frame with centrality measures:
    #eigenvector
    ev = nx.eigenvector_centrality(G) #extracting measures
    eigenvector = pd.DataFrame(ev.items())  #saving as a data frame
    eigenvector.columns = ["name","ev_centrality"]
    
    #betweenness
    bc = nx.betweenness_centrality(G) #extracting measures
    betweenness = pd.DataFrame(bc.items())  #saving as a data frame
    betweenness.columns = ["name","betweenness"]
    
    #degree
    dg = nx.degree(G)  #extracting measures
    degree = pd.DataFrame(dg)  #saving as a data frame
    degree.columns = ["name","degree"]
    
    #merging by the 'name' column:
    network_measures = pd.merge(eigenvector,betweenness,on = "name")
    network_measures = pd.merge(network_measures,degree,on = "name")

    #saving as .csv file in the output value 
    network_measures.to_csv("output/network_measures.csv")


if __name__=="__main__":
    main()