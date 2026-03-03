import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    if N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    
    us = employee["salary"].drop_duplicates()
    ss = us.sort_values(ascending=False)
    
    if N <= len(ss):
        result = ss.iloc[N - 1]
    else:
        result = None
    
    return pd.DataFrame({f"getNthHighestSalary({N})": [result]})