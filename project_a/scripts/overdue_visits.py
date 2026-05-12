def get_overdue_visits(df):
    df = df.copy()

    # Count incomplete visits per participant
    overdue = df[df["completed"] == "no"].drop_duplicates("visit_date")
    # print(overdue)
    overdue["visits_incomplete"] = overdue.groupby("name")["name"].transform("count")
    overdue = overdue[["id", "name", "age", "status", "visit_id", "visit_type", "completed"]]

    # Find participants with no visits
    no_visits = df[df["visit_id"].isna()]
    no_visits = no_visits[["name", "status"]]

    # Print warning: overdue
    if len(overdue) > 0:
        print(f"""
        Incomplete Visits:
        
        {overdue.groupby("name").size().reset_index(name="incomplete_count")}
        
        """)

    # Print warning: no visits
    if len(no_visits) > 0:
        
        print(f"""
        ATTENTION: The following participants have no recorded visits:

        {no_visits}

        """)
    return overdue, no_visits