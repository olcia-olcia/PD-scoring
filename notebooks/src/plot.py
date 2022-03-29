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
    sns.displot(data=df,x=variable,kind="kde" , **kwargs)
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


def plot_box(df: pd.DataFrame, variable: str, **kwargs):
    """
    Plots  boxplot with split using target variable     
        
    Returns:
        prints boxplot
    
    """
    plt.figure(figsize = (9,3))
    sns.boxplot(data=df,y=variable, x='target')
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} ".format(variable))
    plt.show()

    return(plt)