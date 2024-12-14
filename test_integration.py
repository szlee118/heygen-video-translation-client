import subprocess
import time
from client import VideoTranslationClient

def test_integration():
    # Start the server as a subprocess
    server_process = subprocess.Popen(["python3", "server.py"])
    time.sleep(2)  # Give the server some time to start

    try:
        # Use the client library
        client = VideoTranslationClient(server_url="http://127.0.0.1:5000")
        result = client.wait_for_completion()
        print(result)
    finally:
        # Clean up the server process
        server_process.terminate()

if __name__ == "__main__":
    test_integration()
