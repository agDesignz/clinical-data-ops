import pandas as pd

def merge_data(p, v, a):
    p = p.copy()
    v = v.copy().rename(columns={"date": "visit_date", "participant_id": "visitor_id"})
    a = a.copy().rename(columns={"date": "assessment_date", "participant_id": "assessed_id"})

    df = pd.merge(p, v, left_on="Id", right_on="visitor_id", how="left")
    df = pd.merge(df, a, left_on="Id", right_on="assessed_id", how="left")
    return df