import os
from googleapiclient.discovery import build


class YouTubeBase:
    API_KEY = os.getenv("YT_API_KEY")
    _youtube = build('youtube', 'v3', developerKey=API_KEY)

    @classmethod
    def get_service(cls):
        return cls._youtube



