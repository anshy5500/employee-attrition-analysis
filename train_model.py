import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

def train_attrition_model(csv_path):
    df = pd.read_csv(csv_path)
    
    features = ['Salary', 'EngagementSurvey', 'EmpSatisfaction', 'Absences',
                'DaysLateLast30', 'PerformanceScore', 'Department', 'RecruitmentSource']
    features = [f for f in features if f in df.columns]
    
    X = df[features].copy()
    
    for col in X.select_dtypes(include='object').columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
    
    y = df['Termd']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    probs = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, probs)
    print(f"ROC-AUC Score: {auc:.2f}")
    
    df['risk_score'] = model.predict_proba(X)[:, 1]
    df['risk_tier'] = pd.cut(df['risk_score'], bins=[0, 0.33, 0.66, 1], labels=['Low', 'Medium', 'High'])
    
    df.to_csv("Output/risk_scored_data.csv", index=False)
    print("Risk-scored data saved to Output/risk_scored_data.csv")
    print("\n--- ATTRITION RISK SUMMARY ---")
    tier_counts = df['risk_tier'].value_counts()
    for tier in ['Low', 'Medium', 'High']:
        count = tier_counts.get(tier, 0)
        print(f"{tier} Risk: {count} employees")
    
    total = len(df)
    high_risk_pct = (tier_counts.get('High', 0) / total) * 100
    print(f"\nOut of {total} employees:")
    print(f"  → Likely to STAY (Low Risk): {tier_counts.get('Low', 0)}")
    print(f"  → Uncertain (Medium Risk): {tier_counts.get('Medium', 0)}")
    print(f"  → Likely to LEAVE (High Risk): {tier_counts.get('High', 0)} ({high_risk_pct:.1f}%)")
    return auc

if __name__ == "__main__":
    train_attrition_model("Output/cleaned_data.csv")