def create_monthly_report(df):
    df = df.copy()
    df = df.groupby(["Enrollment Month", "Site"]).size().reset_index(name="Enrollments")
    return df