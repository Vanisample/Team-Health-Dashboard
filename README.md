# Team Health Dashboard

An AI-powered Streamlit dashboard for monitoring and analyzing team health metrics across burnout risk, velocity, sentiment, and collaboration.

## Features

- **Burnout Risk Assessment**: Tracks focus time and after-hours communication patterns
- **Velocity Metrics**: Sprint completion rates and PR idle time analysis
- **Sentiment Tracking**: Weekly team sentiment pulse scores
- **Collaboration Insights**: Cross-department meeting frequency
- **Health Index**: Weighted team health scoring combining all metrics

## Requirements

- Python 3.8+
- streamlit
- plotly
- pandas

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vanisample/Team-Health-Dashboard.git
cd Team-Health-Dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Dashboard

### Locally
Start the Streamlit application:
```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501` in your default browser.

### Public Deployment
To deploy this app publicly and share it with anyone via a link, use **Streamlit Cloud**:

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app" and select this repository
5. Deploy and get a public shareable URL

Alternatively, for instant public access, you can use:
```bash
python public_app.py
```
*(Requires ngrok authentication token for public URLs)*

## Project Structure

- `app.py` - Main Streamlit application
- `requirements.txt` - Python package dependencies
- `README.md` - Documentation

## License

MIT
