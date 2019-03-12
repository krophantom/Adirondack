import requests
import json
import configparser
import sys

from enum import Enum


class Rovers(Enum):
    SPIRIT = "spirit"
    CURIOSITY = "curiosity"
    OPPORTUNITY = "opportunity"


config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['DEFAULT']['ApiKey']

MAX_SOL = 2339


def make_api_call(url):

    try:
        r = requests.get(url, timeout=10)
    except (TimeoutError, ConnectionError):
        print("Error reaching API.")

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 403:
        print("API key missing or invalid.")
        sys.exit(0)
    else:
        print("Something is broken!")
        sys.exit(0)


def make_photos_url(rover, key, sol):

    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/{}/photos/?api_key={}&sol={}".format(
        rover, key, sol)
    return url


def make_manifests_url(rover, key):

    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}/?api_key={}".format(
        rover, key)
    return url


def get_latest_photos(api_key, local_max_sol, rover):

    manifests_url = make_manifests_url(rover, api_key)

    latest_manifest = make_api_call(manifests_url)

    max_sol = latest_manifest['photo_manifest']['max_sol']

    if max_sol > local_max_sol:

        for sol in range(local_max_sol, max_sol+1, 1):
            photos_url = make_photos_url(rover, api_key, sol)
            photos = make_api_call(photos_url)
            print("Found {} images on sol {}".format(
                len(photos['photos']), sol))

    else:
        print("Latest images for {} already added".format(rover))

# Get latest photos for date

get_latest_photos(API_KEY, MAX_SOL, Rovers.CURIOSITY.value)
