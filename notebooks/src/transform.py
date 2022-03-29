import pandas as pd
from typing import List
from dateutil.relativedelta import relativedelta

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def transform_dates(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame :
    """ 
    Prepares calculations based on columns with dates
    
    """

    df['expected_payment_dt'] = df.apply(lambda x: x['issue_d'] + relativedelta(months=x['term']), axis =1)
    df['months_paid'] = df.apply(lambda x: diff_month(x['last_pymnt_d'],x['issue_d']), axis=1)
    df['relationship_months'] = df.apply(lambda x: diff_month(x['issue_d'],x['earliest_cr_line']), axis=1)

    return df




def transform_categorical(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame:

    """ 
    Prepares calculations based on columns categorical columns
    
    """

    df['term'] = df['term'].str.extract(r'(\d{2})').astype('int')


    return df


def transform_numerical(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame :

    """ 
    Prepares calculations based on numeric columns
    
    """

    
    # monthly income
    df['monthly_inc'] = df['annual_inc']/12 

    # Installment before multiplier by interest rate calcula
    df['pure_installment'] = df['installment']/(1+df['int_rate']/100)

    # we will compare that to annual income
    df['annual_installement'] = df['installment']*12

    #loan amount
    df['total_loan_amount'] = df['installement']*df['term']

    
    return df

def transform_target(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame :
    #default_columns = ['Charged Off', 'Default', 'Does not meet the credit policy. Status:Charged Off', 'Late (31-120 days)']  

    return df