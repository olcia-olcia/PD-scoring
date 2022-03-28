import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_histogram(df: pd.DataFrame, variable: str, **kwargs):
    """
    Plots histogram         
        
    Returns:
        prints histogram 
    
    """
    plt.figure(figsize = (9,3))
    sns.displot(data=df,x=variable,kind="kde" ,kde=True, **kwargs)
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{}".format(variable))
    plt.show()

    return(plt)

def plot_cnt(df: pd.DataFrame, variable: str, **kwargs):
    """
    Plots histogram         
        
    Returns:
        prints histogram 
    
    """
    plt.figure(figsize = (9,3))
    sns.countplot(data=df,x=variable, **kwargs)
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} ".format(variable))
    plt.show()

    return(plt)