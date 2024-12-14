from flask import Flask, jsonify
import threading
import time
import random
import os

app = Flask(__name__)

# Global variable to simulate job status
job_status = {"result": "pending"}

# Configurable delay settings
DEFAULT_MIN_DELAY = 5
DEFAULT_MAX_DELAY = 10

# Retrieve configurable delay from environment or fallback to default
min_delay = int(os.getenv("MIN_DELAY", DEFAULT_MIN_DELAY))
max_delay = int(os.getenv("MAX_DELAY", DEFAULT_MAX_DELAY))

def simulate_translation():
    global job_status
    delay = random.randint(min_delay, max_delay)  # Random delay within the range
    print(f"Simulating translation with a delay of {delay} seconds.")
    time.sleep(delay)
    # Randomly determine completion or error (80% success, 20% error)
    job_status["result"] = "completed" if random.random() < 0.8 else "error"

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(job_status)

if __name__ == "__main__":
    # Start the translation simulation in a separate thread
    threading.Thread(target=simulate_translation).start()
    app.run(port=5000)
