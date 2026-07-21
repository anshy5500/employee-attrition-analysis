import pandas as pd

def export_final(csv_path):
    df = pd.read_csv(csv_path)
    df.to_csv("Output/powerbi_ready_data.csv", index=False)
    print(f"Power BI-ready file saved: Output/powerbi_ready_data.csv ({df.shape[0]} rows)")

if __name__ == "__main__":
    export_final("Output/risk_scored_data.csv")