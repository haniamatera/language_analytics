# Assignment 4

## Description of the assignment

This assignment’s task focuses on creating a command-line tool that takes a given dataset and performs simple network analysis. In particular, it will build networks based on entities appearing together in the same document. The data set used in this assignment comprises the US news articles, where the network is created based on the frequency of given entities appearing together in the text corpus. Ultimately, the created script: 
- Takes any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB", where the edgelist is 
- For any given weighted edgelist given as an input, the script creates a network visualization, which is then saved in a folder called viz.
- Creates a data frame showing the centrality measures.

The centrality measures computed in this assignment are calculated using networkx package and comprise: (1) the degree centrality, which is the simplest measure of node connectivity where the importance scores are assigned based on the number of links held by each node; (2) the betweenness centrality, which measures the number of times a node lies on the shortest path between other nodes, and (3) the eigenvector centrality, which also measures a node’s influence based on the number of links it has to other nodes in the network but also takes into account how well connected a node is, and how many links their connections have.

___Data___

Data for this assignment can be accessed and downloaded from my GitHub repository at the following [link](https://github.com/haniamatera/language_analytics/blob/main/Assignment3/data/abcnews-date-text.csv)

## The method
The main function created to perform the following assignment task takes filename and threshold as input arguments that can be specified from the command line. The filename signifies the edgelist file that one wishes to use as an input, based on which the network is constructed. The threshold argument signifies the weight between the two nodes in the network that one wishes to work with. Lowering the threshold between the nodes will yield more connections displayed in the graph. The default threshold is set to 500 and can be changed in the command line. 
Upon importing the input file and filtering out the edges below the desired threshold the network graphics displaying the nodes and their respective weights is drawn using pandas package. 
After creating all visuals, the centrality measures between the nodes are calculated and imputed into a data frame which is saved in the output folder under the name network_measures.csv.

## Results and evaluation
The graphical representation of the node network saved as a .png file can be seen in the viz folder in my GitHub repository. A .csv file with all centrality measures for each node pair can be found in the output folder.

## Repository structure and files
This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```viz``` | Contains the visual output with a graph showing the enetwork structure between the nodes.
```output``` | Contains the output with a .csv file containing the centrality measures between the nodes.
```network.py```| The script to be executed from the terminal.
```create_visual_venv.sh``` | A bash script which automatically generates a new virtual environment 'network_env', and install all the packages contained within 'requirements.txt'
```requirements.txt``` | A list of packages along with the versions that are required.
```README.md``` | This readme file.
```data```| A folder with an edgelist file 


## Usage (reproducing the results)

### Virtual environment
In order to run the script, one is required to set up the virtual environment with all necessary packages installed. Please clone the repo, navigate to the folder for this assignment, run the bash script to set up the environment, and lastly activate it. The following code should be executed from the terminal:

```bash
git clone https://github.com/haniamatera/language_analytics.git
cd Assignment4
bash ./create_visual_venv.sh
source ./sentiment_env/bin/activate
```
### Execute the script 
Now, the script can be executed:

```bash
python network.py  

```
