import pandas as pd

def fix_names(u: pd.DataFrame) -> pd.DataFrame:
    u['name']=u['name'].str.capitalize()
    return u.sort_values(by='user_id')