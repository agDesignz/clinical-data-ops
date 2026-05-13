def output_participants_clean(df):
    df = df.copy()
    # df = df[[
    #     "id",
    #     "name",
    #     "age",
    #     "status"
    # ]]
    df = df.rename(columns={
        "enrolled_date":"enrollment date",
        "age_category":"age category",
        "enroll_month":"enrollment month"
    })
    df.columns = [name.title() for name in df.columns]
    print(df)