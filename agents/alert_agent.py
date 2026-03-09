def alert_agent(df):
    alert_df = df.copy()
    alert_df["send_alert"] = alert_df["risk_level"].apply(lambda x: x == "High")
    return alert_df
