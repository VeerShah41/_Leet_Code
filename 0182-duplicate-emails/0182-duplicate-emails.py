import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    x = person[person.duplicated(subset="email", keep=False)]
    y = x[["email"]].drop_duplicates()
    return y