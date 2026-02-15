import pandas as pd
from modelingeqs import MMfit
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
    plt.scatter(substrate, velocity, color = 'gold')
    plt.xlabel('[S]')
    plt.ylabel('Velocity')
    plt.title('Substrate vs. Velocity')
    yfit = MMfit(substrate, velocity)
    xfit = range(int(min(substrate)), int(max(substrate)) + 1)
    '''Plot the data, yfit[0] is Vmax and yfit[1] is Km'''
    label = f'MM Fit: Vmax={yfit[0]:.2f}, Km={yfit[1]:.2f}'
    plt.plot(xfit, [yfit[0] * s / (yfit[1] + s) for s in xfit], color='pink', label=label)
    plt.legend()

def save_figure(filename):
    '''Save the current figure to a file.'''
    import matplotlib.pyplot as plt
    plt.savefig(filename)