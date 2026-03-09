import streamlit as st
import pandas as pd
import plotly.express as px

from agents.coordinator import coordinator_run
from utils.n8n_utils import send_to_n8n
st.set_page_config(page_title="EcoGuardian AI", layout="wide")

st.title("🌍 EcoGuardian AI")
st.subheader("AI Multi-Agent Sustainability Monitoring Dashboard")

uploaded_file = st.file_uploader("Upload environmental CSV file", type=["csv"])

uploaded_df = None
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)

if st.button("Run Multi-Agent Analysis"):
    result_df = coordinator_run(uploaded_df)

    st.success("Analysis completed successfully")

    col1, col2, col3 = st.columns(3)
    col1.metric("Sites", len(result_df))
    col2.metric("High Risk Sites", int((result_df["risk_level"] == "High").sum()))
    col3.metric("Average Risk Score", round(result_df["risk_score"].mean(), 1))

    st.markdown("## Results Table")
    st.dataframe(result_df, use_container_width=True)

    st.markdown("## Risk by Site")
    fig = px.bar(result_df, x="site", y="risk_score", color="risk_level")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## Recommendations")
    for _, row in result_df.iterrows():
        st.markdown(f"### {row['site']}")
        st.write(f"**Risk Level:** {row['risk_level']}")
        st.write(f"**Summary:** {row['analysis_summary']}")
        st.write(f"**Recommendation:** {row['recommendation']}")
        if row["send_alert"]:
            st.warning("Alert should be sent for this site")
