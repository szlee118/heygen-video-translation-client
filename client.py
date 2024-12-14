import requests
import time
import logging

logging.basicConfig(level=logging.INFO)


class VideoTranslationClient:
    def __init__(self, server_url, max_wait_time=30, initial_poll_interval=1, max_poll_interval=5):
        """
        Initialize the client.
        :param server_url: URL of the server
        :param max_wait_time: Maximum time to wait for a job to complete
        :param initial_poll_interval: Initial interval for polling
        :param max_poll_interval: Maximum interval for polling
        """
        self.server_url = server_url
        self.max_wait_time = max_wait_time
        self.initial_poll_interval = initial_poll_interval
        self.max_poll_interval = max_poll_interval

    def get_status(self):
        """Fetch the job status from the server."""
        try:
            response = requests.get(f"{self.server_url}/status")
            response.raise_for_status()
            return response.json()["result"]
        except requests.RequestException as e:
            logging.error(f"Error fetching status: {e}")
            raise

    def wait_for_completion(self):
        """Wait for the job to complete with exponential backoff."""
        start_time = time.time()
        poll_interval = self.initial_poll_interval

        while time.time() - start_time < self.max_wait_time:
            status = self.get_status()
            logging.info(f"Status: {status}")

            if status == "completed":
                return "Job completed successfully"
            elif status == "error":
                return "Job failed with error"
            
            time.sleep(poll_interval)
            poll_interval = min(poll_interval * 2, self.max_poll_interval)

        raise TimeoutError("Timed out waiting for job to complete")
