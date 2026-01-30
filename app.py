import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Dummy Data (Last 4 Weeks)
# -----------------------------
data = {
    "Week": ["Wk1", "Wk2", "Wk3", "Wk4"],
    "FocusTime": [5.2, 4.8, 5.5, 4.2],
    "AfterHoursPings": [4.1, 6.3, 3.7, 7.5],
    "SprintCompletion": [82, 76, 88, 70],
    "PRIdleTime": [36, 42, 28, 50],
    "Sentiment": [7.4, 6.8, 8.1, 6.2],
    "CollaborationMeetings": [6, 5, 7, 4]
}
df = pd.DataFrame(data)

# -----------------------------
# Weighted Team Health Index
# -----------------------------
def team_health_index(row):
    # Normalize Burnout Risk: higher focus time + fewer pings = better
    B = (row["FocusTime"]/6 * 50) + ((10-row["AfterHoursPings"])/10 * 50)
    # Velocity: sprint completion + inverse PR idle time
    V = (row["SprintCompletion"]) * 0.6 + (100 - row["PRIdleTime"]) * 0.4
    # Sentiment scaled to 0–100
    S = row["Sentiment"] * 10
    # Collaboration scaled to 0–100
    C = row["CollaborationMeetings"]/10 * 100
    return 0.30*B + 0.30*V + 0.25*S + 0.15*C

df["HealthIndex"] = df.apply(team_health_index, axis=1)

# -----------------------------
# Streamlit Layout
# -----------------------------
st.set_page_config(page_title="Team Health Dashboard", layout="wide")
st.title("🚀 AI-Powered Team Health Dashboard")

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Burnout Risk (Focus hrs)", round(df.iloc[-1]["FocusTime"],1))
col2.metric("After-Hours Pings", df.iloc[-1]["AfterHoursPings"])
col3.metric("Velocity (Sprint %)", f"{df.iloc[-1]['SprintCompletion']}%")
col4.metric("Sentiment Score", df.iloc[-1]["Sentiment"])
col5.metric("Team Health Index", round(df.iloc[-1]["HealthIndex"],1))

st.markdown("---")

# Burnout Risk Visualization
fig_burnout = px.scatter(df, x="FocusTime", y="AfterHoursPings", color="Week",
                         size="AfterHoursPings", title="Burnout Risk Heatmap")
st.plotly_chart(fig_burnout, use_container_width=True)

# Velocity & Flow
colA, colB = st.columns(2)
fig_velocity = px.bar(df, x="Week", y="SprintCompletion", title="Sprint Completion Rate")
colA.plotly_chart(fig_velocity, use_container_width=True)

fig_pr_idle = px.line(df, x="Week", y="PRIdleTime", markers=True, title="PR Idle Time Trend")
colB.plotly_chart(fig_pr_idle, use_container_width=True)

# Sentiment
fig_sentiment = px.line(df, x="Week", y="Sentiment", markers=True,
                        title="Sentiment Trend (Pulse Scores)")
st.plotly_chart(fig_sentiment, use_container_width=True)

# Collaboration
fig_collab = px.bar(df, x="Week", y="CollaborationMeetings", title="Cross-Department Meetings")
st.plotly_chart(fig_collab, use_container_width=True)

# Team Health Index Trend
fig_health = px.line(df, x="Week", y="HealthIndex", markers=True,
                     title="Team Health Index Trend")
st.plotly_chart(fig_health, use_container_width=True)
