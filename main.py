from clean_data import load_and_clean
from sql_analysis import run_sql_analysis
from train_model import train_attrition_model
from export_for_powerbi import export_final

if __name__ == "__main__":
    load_and_clean("Data/HRDataset_v14.csv")
    run_sql_analysis("Output/cleaned_data.csv")
    train_attrition_model("Output/cleaned_data.csv")
    export_final("Output/risk_scored_data.csv")
    print("\nPipeline complete! Open Output/powerbi_ready_data.csv in Power BI.")