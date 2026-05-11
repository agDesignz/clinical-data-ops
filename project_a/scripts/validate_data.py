import pandas

def validate_participants(df):
    errors = []
    df = df.copy()

    # Check for duplicate IDs
    dups = df.duplicated(subset=["id"]).sum()
    if dups > 0:
        errors.append(f"WARNING: {dups} duplicate participant IDs found (Participants)")

    # Check for missing required fields
    required = ["id", "name", "status"]
    for col in required:
        missing = df[col].isna().sum()
        if missing > 0:
            errors.append(f"WARNING: {missing} missing values in '{col}' (Participants)")

    # Check age range
    if "age" in df.columns:
        invalid = df[(df["age"] < 0) | (df["age"] > 120)].shape[0]
        if invalid > 0:
            errors.append(f"WARNING: {invalid} participants with invalid age (Participants)")

    if not errors:
        print("Validation passed — no issues found. (Participants)")
    else:
        for e in errors:
            print(e)

    # return len(errors) == 0


def validate_visits(df):
    errors = []

    # No duplicate visit_id
    dups = df.duplicated(subset=["visit_id"]).sum()
    if dups > 0:
        errors.append(f"WARNING: {dups} duplicate visit IDs found (Visits)")
    
    # completed == ["yes", "no"]
    if "completed" in df.columns:
        df["completed"] = df["completed"].str.lower()
        valid_completed = ["yes", "no"]
        invalid_completed = df[~df["completed"].isin(valid_completed)].shape[0]
        # print(invalid_completed)
        if invalid_completed > 0:
            errors.append(f"WARNING: {invalid_completed} invalid entries found in COMPLETED column (Visits)")

    # Wrap it up    
    if not errors:
        print("Validation passed — no issues found. (Visits)")
    else:
        for e in errors:
            print(e)

    # return len(errors) == 0