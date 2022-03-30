import pandas as pd
from scipy import stats

def chi_2(df, variable):
    
    cross_table = pd.crosstab(df['target'],df[variable])
    chi2, p, dof, ex = stats.chi2_contingency(cross_table) 
    alpha = 0.05
    

    print('chi_2 statistic: {:.2f}'.format(chi2))
    print('p_value: {:.2f}'.format(p))
    print("significant level", alpha)
    
    if p <=alpha:
        print('Reject H0, variables have dependency')
    else:
        print('Do not reject H0')