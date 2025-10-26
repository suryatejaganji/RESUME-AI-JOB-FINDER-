import pandas as pd

def load_jobs_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    jobs = df.to_dict(orient="records")
    return jobs