#!/usr/bin/python3
"""Headers request"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
