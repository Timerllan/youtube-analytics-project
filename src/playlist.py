from datetime import datetime, timedelta

from src.video import PLVideo
from src.you_tube_base import YouTubeBase


class PlayList(YouTubeBase):

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        self.__data = self._youtube.playlists().list(part='snippet', id=self.id_playlist).execute()
        self.__video_list = self.__get_videos()

    @property
    def url(self):
        return f"https://www.youtube.com/playlist?list={self.id_playlist}"

    def __get_videos(self):
        id_youtube = self._youtube.playlistItems().list(part='contentDetails', playlistId=self.id_playlist).execute()
        return [PLVideo(video['contentDetails']['videoId'], self.id_playlist) for video in id_youtube['items']]

    @property
    def title(self):
        return self.__data['items'][0]["snippet"]["title"]

    @property
    def total_duration(self):
        return sum([video.duration for video in self.__video_list], start=timedelta(0))

    def show_best_video(self):
        if len(self.__video_list) == 0:
            return None
        best_video = self.__video_list[0]

        for video in self.__video_list:
            if best_video.like < video.like:
                best_video = video

        return best_video
