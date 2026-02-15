from utils import loaddata, preprocess_data, plotdata, save_figure
import os
directory = 'data/'
for files in os.listdir(directory):
    if files.endswith('csv'):
         with open(os.path.join(directory, files)) as data:
            substrate, velocity = loaddata(data)
            if preprocess_data(substrate, velocity):
                print("Data preprocessing successful.")
                plotdata(substrate, velocity,)
                save_figure(f'results/{files.replace(".csv", ".png")}')
            else:
                print("Data preprocessing failed. Please check the input data.")
