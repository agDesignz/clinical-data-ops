def create_monthly_report(df):
    df = df.copy()
    df = df.groupby(["enroll_month", "site"]).size().reset_index(name="enrollments")
    # df =df.rename(columns={"enrolled_month"})
    return df