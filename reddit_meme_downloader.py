#!/usr/bin/env python3

import pprint
import time
import argparse
import sys
import os

import praw
import requests

# This is for convinience while developing
def _object_attributes(object):
    pprint.pprint(vars(object))

def download_meme(meme_item, save_dir):
    # TODO: Figure out image file extensions/names based on URL
    image_url = meme_item.url
    filename = meme_item.id

    with open(save_dir + "/" + filename, "wb") as download:
        response = requests.get(image_url)
        download.write(response.content)
    
BANNER_ART = """                                                                             
,------.           ,--.   ,--.,--.  ,--.      ,--.   ,--.                         
|  .--. ' ,---.  ,-|  | ,-|  |`--',-'  '-.    |   `.'   | ,---. ,--,--,--. ,---.  
|  '--'.'| .-. :' .-. |' .-. |,--.'-.  .-'    |  |'.'|  || .-. :|        || .-. : 
|  |\  \ \   --.\ `-' |\ `-' ||  |  |  |      |  |   |  |\   --.|  |  |  |\   --. 
`--' '--' `----' `---'  `---' `--'  `--'      `--'   `--' `----'`--`--`--' `----' 
,------.                            ,--.                  ,--.                    
|  .-.  \  ,---. ,--.   ,--.,--,--, |  | ,---.  ,--,--. ,-|  | ,---. ,--.--.      
|  |  \  :| .-. ||  |.'.|  ||      \|  || .-. |' ,-.  |' .-. || .-. :|  .--'      
|  '--'  /' '-' '|   .'.   ||  ||  ||  |' '-' '\ '-'  |\ `-' |\   --.|  |         
`-------'  `---' '--'   '--'`--''--'`--' `---'  `--`--' `---'  `----'`--'         
                                                                                  
"""

if __name__ == "__main__":
    print(BANNER_ART)

    if len(sys.argv) < 2:
        print("Incorrect usage.\nUse \'reddit_meme_downloader.py -h\' for help.")
        sys.exit()

    arg_parser = argparse.ArgumentParser(description="A little script to download saved memes from Reddit!")
    arg_parser.add_argument("-s", action="store", dest="savedir", help="Specify the directory to save memes to.")
    arg_parser.add_argument("--save-dir", action="store", dest="savedir", help="Specify the directory to save memes to.")
    parsed = arg_parser.parse_args()

    if not parsed.savedir:
        print("Incorrect usage.\nUse \'reddit_meme_downloader.py -h\' for help.")
        sys.exit()

    reddit = praw.Reddit(site_name="user", user_agent="Reddit Meme Downloader")

    os.mkdir(parsed.savedir)

    # TODO: Add download time and number of items downloaded
    print("Downloading memes...")
    for item in reddit.user.me().saved():
        print("Downloading " + item.id + ".")
        download_meme(item, parsed.savedir)
        time.sleep(10)
