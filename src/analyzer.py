from utils import loaddata, plotdata, preprocess_data
from modelingeqs import fitparam
with open('data/testdata.csv') as data:
    substrate, velocity = loaddata(data)
    if preprocess_data(substrate, velocity):
        print("Data preprocessing successful.")
    else:
        print("Data preprocessing failed. Please check the input data.")
plotdata(substrate, velocity)
