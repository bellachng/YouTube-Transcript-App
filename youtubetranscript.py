import tkinter as tk
from tkinter import scrolledtext
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# get_video_id(url): Input a YouTube URL and extract the video ID
def get_video_id(url):
    # Parse the input URL
    query = urlparse(url)

    if query.hostname == 'youtu.be': # Check if hostname is youtu.be
        return query.path[1:]
    
    if query.hostname in ('www.youtube.com', 'youtube.com'): # Check if hostname is www.youtube.com or youtube.com
        # Check if path is '/watch'
        if query.path == '/watch':
            # Then extract the video ID from the query parameters
            return parse_qs(query.query)['v'][0]
        # Check if path is '/embed/'
        if query.path[:7] == '/embed/':
            # Then return the 3rd component of the path
            return query.path.split('/')[2]
        # Check if path is '/v/'
        if query.path[:3] == '/v/':
            # Then return the 3rd component of the path
            return query.path.split('/')[2]
    return None

# fetch_transcript(video_url): Given a YouTube URL, get the transcript using the API
def fetch_transcript(video_url):
    # Verify a video_id was retrieved
    video_id = get_video_id(video_url)

    if video_id:
        try:
            # Fetch transcript using youtube_transcript_api
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return transcript
        except Exception as e:
            # No transcript found
            return None
    else:
        return None
