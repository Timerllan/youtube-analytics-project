from src.you_tube_base import YouTubeBase
import isodate


class Video(YouTubeBase):

    def __init__(self, id_video):
        try:
            self.__data = self._youtube.videos().list(id=id_video, part='snippet,statistics,contentDetails').execute()
            if self.__data['pageInfo']['totalResults'] == 0:
                raise Exception

        except Exception as e:
            self.__data = None

        self.__id_video = id_video

    @property
    def title(self):
        if self.__data:
            return self.__data['items'][0]["snippet"]["title"]
        return None

    @property
    def url(self):
        if self.__data:
            return f"https://www.youtube.com/watch?v={self.__id_video}"

    @property
    def id_video(self):
        if self.__data:
            return self.__id_video

    @property
    def count_video(self):
        if self.__data:
            return int(self.__data['items'][0]['statistics']['viewCount'])

    @property
    def like_count(self):
        if self.__data:
            return int(self.__data['items'][0]['statistics']['likeCount'])

    @property
    def duration(self):
        if self.__data:
            return isodate.parse_duration(self.__data['items'][0]['contentDetails']['duration'])

    def __str__(self):
        if self.__data:
            return self.title


class PLVideo(Video):

    def __init__(self, id_video, id_playlist):
        self.__id_playlist = id_playlist
        you_tube = self._youtube.playlistItems().list(videoId=id_video,
                                                      part='contentDetails'
                                                      , playlistId=id_playlist,
                                                      ).execute()
        if you_tube['pageInfo']['totalResults'] > 0:
            super().__init__(id_video)
        else:
            raise AssertionError('ошибка')

    @property
    def id_plv(self):
        return self.__id_playlist
