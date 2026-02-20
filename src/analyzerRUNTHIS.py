from utils import loaddata, preprocess_data, plotdata, save_figure, save_bulk_file
import os

directory = 'data/'
for files in os.listdir(directory):
    if files.lower().endswith('.csv'): # checks for CSV files
        filepath = os.path.join(directory, files) # constructs the full file path
        substrate, velocity = loaddata(filepath) # loads the substrate and velocity data from the CSV file

        if preprocess_data(substrate, velocity): #
            print("Data preprocessing successful.")
            plotdata(substrate, velocity) # plots the substrate vs. velocity data and fits the Michaelis-Menten equation
            save_figure(f'results/{files.replace(".csv", ".png")}') # saves the plot as a PNG file in the results directory, with the same name as the CSV file
        else:
            print("Data preprocessing failed. Please check the input data.")
