import pandas as pd

def load_and_clean(file_path):
    df = pd.read_csv(file_path)
    print(f"Original shape: {df.shape}")
    
    df = df.drop_duplicates()
    
    df.columns = df.columns.str.strip()
    
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    
    for col in ['Salary', 'EngagementSurvey', 'EmpSatisfaction', 'Absences', 'DaysLateLast30']:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    
    df.to_csv("Output/cleaned_data.csv", index=False)
    print(f"Cleaned shape: {df.shape}")
    print("Saved to Output/cleaned_data.csv")
    return df

if __name__ == "__main__":
    load_and_clean("Data/HRDataset_v14.csv")