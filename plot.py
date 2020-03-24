import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------
# Plot a single country
#-------------------------------------------------------------------------------------------

def generate_plot_data(df,country, col='cases'):
    cdf = df.loc[df['province']==country]
    if cdf.shape[0]==0:
        cdf = df.loc[df['country']==country]
        cdf = cdf.sort_values('date')
        cdf = cdf.groupby('date')[col].sum()
        cdf = cdf.sort_values()
        X = list(cdf.index)
        X = list(range(len(X)))
        Y = list(cdf)
    else:
        X = list(cdf['date'])
        X = list(range(len(X)))
        Y = list(cdf[col])
        X = [X[i] for i in range(len(X)) if i%2==0]
        Y = [Y[i] for i in range(len(Y)) if i%2==0]
    return X, Y

#-------------------------------------------------------------------------------------------
# Plot a single country
#-------------------------------------------------------------------------------------------

def plot_cases_by_country (df, country='France', col='cases'):

    # Select, sort and clean data 
    X, Y = generate_plot_data(df, country)
        
    # Plot the data.
    plt.plot(X,Y)
    plt.xticks(X)
    plt.title('Coronavirus ' + col + ' for ' + country)
    plt.xlabel('Date')
    plt.ylabel(col)

    # Display
    plt.show()

    
#-------------------------------------------------------------------------------------------
# Plot multiple countries
#-------------------------------------------------------------------------------------------

COUNTRIES = ["Italy", 'US', "Spain", 'Germany', 'France', "United Kingdom"]

# Col values should be one of: cases, recovered or deaths

def plot_cases_by_countries (df, countries=COUNTRIES, col='cases'):

    fig,a =  plt.subplots(1,1)
    p = fig
    for country in countries:
        # SElect, sort and clean data 
        X, Y = generate_plot_data(df, country, col)
        # Plot the data.
        a.plot(X,Y)
        # Set the inline labels
        plt.text(X[-1], Y[-1],country)
        
    plt.xticks(X)
    plt.title('Coronavirus '  + col + 'for ' + ','.join(countries))
    plt.xlabel('Date')
    plt.ylabel(col)
    a.yaxis.grid(True)
    plt.show()

#-------------------------------------------------------------------------------------------
# End of File
#-------------------------------------------------------------------------------------------
