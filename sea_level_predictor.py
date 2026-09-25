import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=8)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_ext = pd.Series(range(1880, 2051))
    ax.plot(years_ext, res.intercept + res.slope * years_ext, 'r', label='fit all')
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, res2.intercept + res2.slope * years_recent, 'g', label='fit 2000+')
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    return ax
