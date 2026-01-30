import subprocess
import time
from pyngrok import ngrok

# Start Streamlit in the background
print("Starting Streamlit app...")
streamlit_process = subprocess.Popen(
    ["streamlit", "run", "app.py", "--server.headless", "true"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for Streamlit to start
time.sleep(3)

# Create ngrok tunnel
print("Creating public tunnel...")
public_url = ngrok.connect(8501)
print(f"\n✅ PUBLIC URL: {public_url}")
print(f"Share this link with anyone to access the dashboard!")
print(f"\nStreamlit is running on http://localhost:8501")

# Keep the process running
try:
    streamlit_process.wait()
except KeyboardInterrupt:
    print("\nShutting down...")
    streamlit_process.terminate()
    ngrok.kill()
