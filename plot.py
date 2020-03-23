# Pyplot
import matplotlib.pyplot as plt


#-------------------------------------------------------------------------------------------
# Plot Bics
#-------------------------------------------------------------------------------------------

def generate_plot_data(df,country):
    cdf = df.loc[df['province']==country]
    if cdf.shape[0]==0:
        cdf = df.loc[df['country']==country]
        cdf = cdf.sort_values('date')
        cdf = cdf.groupby('date')['count'].sum()
        cdf = cdf.sort_values()
        X = list(cdf.index)
        X = list(range(len(X)))
        Y = list(cdf)
    else:
        X = list(cdf['date'])
        X = list(range(len(X)))
        Y = list(cdf['count'])
    return X, Y

def plot_cases_by_country (df, country='France', label='Coronavirus cases for '):

    # SElect, sort and clean data 
    X, Y = generate_plot_data(df, country)
        
    # Plot the data.
    plt.plot(X,Y)
    plt.xticks(X)
    plt.title(label + country)
    plt.xlabel('Date')
    plt.ylabel('Infected')

    plt.show()

DEFAULT_COUNTRIES = ["Italy", 'US', "Spain", 'France', "United Kingdom"]
DEFAULT_LABEL  = 'Coronavirus cases for '

def plot_cases_by_countries (df, countries=DEFAULT_COUNTRIES, label=DEFAULT_LABEL):

    for country in countries:
        # SElect, sort and clean data 
        X, Y = generate_plot_data(df, country)
        # Plot the data.
        plt.plot(X,Y)
        
    plt.xticks(X)
    plt.title(label + ','.join(countries))
    plt.xlabel('Date')
    plt.ylabel('Infected')

    plt.show()

#-------------------------------------------------------------------------------------------
# End of File
#-------------------------------------------------------------------------------------------