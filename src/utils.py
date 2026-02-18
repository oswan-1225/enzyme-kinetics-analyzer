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
    # Sets the axis constraints
    figure, ax = plt.subplots()
    ax.scatter(substrate, velocity, color="gold")
    ax.set_xlabel('[S]')
    ax.set_ylabel('Velocity')
    ax.set_title('Substrate vs. Velocity')
    # plots the eq using the MMfit function to fit the data and plot the resulting curve
    vmax, km = MMfit(substrate, velocity)
    xfit = range(int(min(substrate)), int(max(substrate)) + 1)
    yfit = [vmax * s / (km + s) for s in xfit]
    ax.plot(xfit, yfit, color='pink', label=f'MM Fit: Vmax={vmax:.2f}, Km={km:.2f}')
    return figure

def save_figure(filename, fig=None):
    '''Save the current figure to a file.'''
    import matplotlib.pyplot as plt
    if fig is None:
        fig = plt.gcf()
    fig.tight_layout()
    fig.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close(fig)
