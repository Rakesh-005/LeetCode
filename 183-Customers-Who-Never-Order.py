import pandas as pd

def find_customers(c: pd.DataFrame, o: pd.DataFrame) -> pd.DataFrame:
    df=~c['id'].isin(o['customerId'])
    return c[df][['name']].rename(columns={'name':'customers'})