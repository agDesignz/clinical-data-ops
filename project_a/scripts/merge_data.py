import pandas as pd

def merge_data(p, v, a):
    p = p.copy()
    v = v.copy().rename(columns={"date": "visit_date"})
    a = a.copy().rename(columns={"date": "assessment_date"})

    df = pd.merge(p, v, left_on="id", right_on="participant_id", how="left")
    df = pd.merge(df, a, left_on="id", right_on="participant_id", how="left")
    return df