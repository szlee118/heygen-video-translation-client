# **Heygen Video Translation Client Library**

## **Overview**
This project includes a Python client library and a simulated server to query the status of video translation jobs. The server simulates delays and job states (`pending`, `completed`, or `error`) as a video translation backend, while the client library provides an optimized interface for polling the server.

---

## **Features**
### **Server**
- Simulates a video translation backend with:
  - Configurable random delay for job completion.
  - Randomized job result (`completed` or `error`).
- Easy configuration via environment variables.

### **Client Library**
- **Exponential Backoff**: Optimized polling intervals to minimize server load and latency.
- **Error Handling**: Automatically retries transient errors with logging for debugging.
- **Configurable**:
  - Polling intervals (`initial_poll_interval`, `max_poll_interval`).
  - Maximum wait time for the job (`max_wait_time`).
- **Logs Key Events**: Helps users debug and understand job progress.
- Lightweight and easy to integrate into third-party applications.

---

## **How to Use**

### **1. Install Dependencies**
Ensure you have Python installed (preferably 3.8+). Install the required dependencies:

```bash
pip install flask requests
```


### **2. Run the Server**
Start the server to simulate the video translation backend:

```bash
export MIN_DELAY=5
export MAX_DELAY=15
python server/server.py
```
- MIN_DELAY: Minimum random delay (default: 5 seconds).
- MAX_DELAY: Maximum random delay (default: 10 seconds).


### **3. Run Integration Tests**
You can use the provided integration test to verify the interaction between the client library and the server:

```bash
python test_integration.py
```
This will:

- Start the server.
- Use the client library to query the server's status.
- Log the results to the console.

