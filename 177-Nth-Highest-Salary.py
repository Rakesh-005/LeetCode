import pandas as pd

def nth_highest_salary(e: pd.DataFrame, N: int) -> pd.DataFrame:
    df=e['salary'].drop_duplicates()
    df=df.sort_values(ascending=False)
    if N>len(df) or N<=0:
        return pd.DataFrame({f'getNthHighestsalary({N})':[None]})
    nth=df.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})':[nth]})