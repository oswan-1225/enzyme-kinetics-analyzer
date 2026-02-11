def fitparam(substrate, velocity):
    '''Fit the substrate and velocity data to the Michaelis-Menten equation to estimate Vmax and Km.'''
    import numpy as np
    from scipy import optimize
    
    def michaelis_menten(S, Vmax, Km):
        return (Vmax * S) / (Km + S)
    
    popt, _ = optimize.curve_fit(michaelis_menten, substrate, velocity, bounds=(0, np.inf))
    return popt  # Returns Vmax and Km
