import pandas as pd
def loaddata(filename):
    df = pd.read_csv(filename)
    if 'substrate' not in df.columns or 'velocity' not in df.columns:
        raise ValueError("CSV file must contain 'substrate' and 'velocity' columns.")
    return df['substrate'], df['velocity'] 