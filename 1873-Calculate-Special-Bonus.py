import pandas as pd

def calculate_special_bonus(e: pd.DataFrame) -> pd.DataFrame:
    e['bonus']=((e["employee_id"]%2==1) & (~e["name"].str.startswith("M")))*e["salary"]
    return e[['employee_id','bonus']].sort_values(by='employee_id')