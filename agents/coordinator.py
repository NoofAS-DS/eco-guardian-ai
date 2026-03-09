from agents.collector_agent import collector_agent
from agents.analysis_agent import analysis_agent
from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent
from agents.alert_agent import alert_agent

def coordinator_run(uploaded_df=None):
    df = collector_agent(uploaded_df)
    df = analysis_agent(df)
    df = risk_agent(df)
    df = recommendation_agent(df)
    df = alert_agent(df)
    return df
