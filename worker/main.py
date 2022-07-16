import os
import logging
import json
import psutil
import requests
from datetime import datetime

logger = logging.getLogger("web-worker")

def get_api_url():
    api_host = os.getenv('API_HOST', '127.0.0.1')
    api_port = os.getenv('API_PORT', '80')
    return f'http://{api_host}:{api_port}/stats'

def send_request(body):    
    logger.warning(f'POST {url}, request body: {body}')
    response = requests.post(url, data=json.dumps(body))
    logger.warning(response.content)

if __name__ == '__main__':
    logger.info('Starting worker process...')
    url = get_api_url()
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    timestamp = str(datetime.now())
    req_body = {"timestamp": timestamp, "stats": {"cpu": f"{cpu}%", "ram": f"{ram}%"}}
    send_request(req_body)
    