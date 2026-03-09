def generate_recommendation(row) -> str:
    recommendations = []

    if row["temperature"] >= 40:
        recommendations.append("Increase monitoring during peak heat hours")
    if row["humidity"] <= 20:
        recommendations.append("Schedule irrigation during evening hours")
    if row["air_quality_index"] >= 120:
        recommendations.append("Issue air quality advisory for the site")
    if row["vegetation_index"] <= 0.30:
        recommendations.append("Inspect vegetation stress and review water allocation")

    if not recommendations:
        recommendations.append("Maintain normal monitoring schedule")

    return " | ".join(recommendations)

def recommendation_agent(df):
    rec_df = df.copy()
    rec_df["recommendation"] = rec_df.apply(generate_recommendation, axis=1)
    return rec_df
