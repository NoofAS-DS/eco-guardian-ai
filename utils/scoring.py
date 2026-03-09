def compute_risk_score(row) -> int:
    score = 0

    if row["temperature"] >= 40:
        score += 35
    elif row["temperature"] >= 35:
        score += 25
    elif row["temperature"] >= 30:
        score += 15

    if row["humidity"] <= 12:
        score += 30
    elif row["humidity"] <= 20:
        score += 20
    elif row["humidity"] <= 30:
        score += 10

    if row["air_quality_index"] >= 150:
        score += 20
    elif row["air_quality_index"] >= 120:
        score += 15
    elif row["air_quality_index"] >= 80:
        score += 10

    if row["vegetation_index"] <= 0.25:
        score += 15
    elif row["vegetation_index"] <= 0.35:
        score += 10

    return min(score, 100)

def risk_label(score: int) -> str:
    if score >= 70:
        return "High"
    if score >= 40:
        return "Medium"
    return "Low"
