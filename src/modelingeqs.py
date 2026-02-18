def MMfit(substrate, velocity):
    '''Fits the Michaelis-Menten equation to the substrate and velocity data.'''
    from scipy.optimize import curve_fit
    def MM(substrate, Vmax, Km):
        return (Vmax * substrate) / (Km + substrate)
    param, _ = curve_fit(MM, substrate, velocity)
    return param