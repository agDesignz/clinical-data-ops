def get_overdue_visits(df):
    df = df.copy()

    # Count incomplete visits per participant
    overdue = df[df["completed"] == "no"].drop_duplicates("visit_date")
    # print(overdue)
    overdue["Incomplete Visits"] = overdue.groupby("Name")["Name"].transform("count")
    overdue = overdue[["Id", "Name", "Age", "Status", "visit_id", "visit_type", "completed"]].rename(columns={"visit_id": "Visit Id", "visit_type": "Visit Type", "completed": "Completed"})
    overdue = overdue.reset_index()

    # Find participants with no visits
    no_visits = df[df["visit_id"].isna()]
    no_visits = no_visits[["Name", "Status", "Site"]]
    no_visits = no_visits.reset_index()

    # Print warning: overdue
    if len(overdue) > 0:
        print(f"""
        Incomplete Visits:
        
        {overdue.groupby("Name").size().reset_index(name="Incomplete Count")}
        
        """)

    # Print warning: no visits
    if len(no_visits) > 0:
        
        print(f"""
        ATTENTION: The following participants have no recorded visits:

        {no_visits}

        """)
    return overdue, no_visits