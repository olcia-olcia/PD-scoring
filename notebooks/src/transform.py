import pandas as pd
from typing import List


def transform_dates(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame :
    return df



def transform_categorical(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame:
    df['term'] = df['term'].str.extract(r'(\d{2})').astype('int')

    return df


def transform_numerical(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame :
   

    return df

def transform_target(df: pd.DataFrame , columns: List[str]) -> pd.DataFrame :
    #default_columns = ['Charged Off', 'Default', 'Does not meet the credit policy. Status:Charged Off', 'Late (31-120 days)']  

    return df