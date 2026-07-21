import pandas as pd
import sqlite3

def run_sql_analysis(csv_path):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(":memory:")
    df.to_sql("employees", conn, index=False, if_exists="replace")
    
    queries = {
        "attrition_by_department": """
            SELECT Department, 
                   COUNT(*) as total,
                   SUM(Termd) as terminated,
                   ROUND(100.0 * SUM(Termd) / COUNT(*), 2) as attrition_pct
            FROM employees GROUP BY Department
        """,
        "avg_salary_by_department": """
            SELECT Department, ROUND(AVG(Salary), 2) as avg_salary
            FROM employees GROUP BY Department
        """,
        "performance_score_distribution": """
            SELECT PerformanceScore, COUNT(*) as total
            FROM employees GROUP BY PerformanceScore
        """,
        "attrition_by_recruitment_source": """
            SELECT RecruitmentSource, COUNT(*) as total,
                   SUM(Termd) as terminated
            FROM employees GROUP BY RecruitmentSource
        """,
        "avg_satisfaction_by_department": """
            SELECT Department, ROUND(AVG(EmpSatisfaction), 2) as avg_satisfaction,
                   ROUND(AVG(EngagementSurvey), 2) as avg_engagement
            FROM employees GROUP BY Department
        """
    }
    
    for name, query in queries.items():
        result = pd.read_sql(query, conn)
        result.to_csv(f"Output/sql_{name}.csv", index=False)
        print(f"\n--- {name} ---")
        print(result)
    
    conn.close()

if __name__ == "__main__":
    run_sql_analysis("Output/cleaned_data.csv")