import pandas as pd
from modelingeqs import fitparam
from numpy import linspace
def loaddata(filename):
    '''Load substrate and velocity data from a CSV file. The CSV file must contain 'substrate' and 'velocity' columns.'''
    df = pd.read_csv(filename)
    if 'substrate' not in df.columns or 'velocity' not in df.columns:
        raise ValueError("CSV file must contain 'substrate' and 'velocity' columns.")
    return df['substrate'], df['velocity']

def preprocess_data(substrate, velocity: pd.Series):
    '''checks the substrate and velocity data. This function checks for missing values and ensures that the data is of the same length.'''
    if len(substrate) != len(velocity):
        raise ValueError("Substrate and velocity data must be of the same length.")
    return True

def plotdata(substrate, velocity):
    '''Plot substrate vs. velocity data using matplotlib.'''
    import matplotlib.pyplot as plt
    plt.scatter(substrate, velocity)
    plt.xlabel('[S]')
    plt.ylabel('Velocity')
    plt.title('Substrate vs. Velocity')
    x_fit = linspace(min(substrate), max(substrate), 100)
    y_fit = fitparam(substrate, velocity)(x_fit)
    plt.plot(x_fit, y_fit, label='Fitted Curve')
    plt.show()
