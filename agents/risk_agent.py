from utils.scoring import compute_risk_score, risk_label

def risk_agent(df):
    risk_df = df.copy()
    risk_df["risk_score"] = risk_df.apply(compute_risk_score, axis=1)
    risk_df["risk_level"] = risk_df["risk_score"].apply(risk_label)
    return risk_df
