import requests
from configs import HEALTHCHECK_ID


def ping_healthchecks():
    requests.get(f'https://hc-ping.com/{HEALTHCHECK_ID}', timeout=10)
