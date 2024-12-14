# Heygen Video Translation Client Library

## Overview
This is a Python client library to query the status of video translation jobs on a simulated server.

## Features
- Exponential backoff for optimized polling
- Handles transient errors and retries
- Logs key events for debugging
- Configurable polling intervals and timeout

## How to Use

### Install Dependencies
```bash
pip install flask requests
