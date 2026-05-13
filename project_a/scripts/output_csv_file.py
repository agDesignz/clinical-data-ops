import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")

def output_csv_file(df, file_name):
    # dest = f"./outputs/{file_name}.csv"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f"{file_name}.csv")
    df.to_csv(path, index=False)
    print(f"Created file: {path}.csv")