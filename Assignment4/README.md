## INSTRUCTIONS 

In order to run the script, please navigate outside the 'Assignment 4' folder and download the whole repository as a .zip file. You can then either upload it to the JupyterHub or run locally on your computer. To do that you should :

1. Open the terminal and navigate to the assignment folder (```cd 'your path'```) 
2. Create the virtual environment by typing: ```bash create_lang_venv.sh``` (this command will create a new virtual envirinamnet with all packages specified in the requirements.txt file)
3. Run the python script by typing: python network.py -p "filename" -t 'your_number' (this command enables you to run the script and to specify parameters such as: the edge list you wnat to use and the threshld (-t) which specifies the cut-off point for the data being used. Selecting the threshold of, e.g. 200 will result in subsetting the data to only containing the pairs of nodes which weight os larger than 200. If you wish to run the code on the data saved in the data folder, simply type : ```python network.py -p "edges_df.csv" -t 'e.g. 200' ```
4. The graph with the created network will be saved in the 'vis' folder and the .csv file with centrality measures will be saved in the output folder. ;) 
