from src.you_tube_base import YouTubeBase


class Video(YouTubeBase):

    def __init__(self, id_video):
        self.__id_video = id_video
        self.__data = self._youtube.videos().list(id=id_video, part='snippet,statistics').execute()

    @property
    def title(self):
        return self.__data['items'][0]["snippet"]["title"]

    @property
    def url(self):
        return f"https://www.youtube.com/watch?v={self.__id_video}"

    @property
    def id_video(self):
        return self.__id_video

    @property
    def count_video(self):
        return int(self.__data['items'][0]['statistics']['viewCount'])

    @property
    def like(self):
        return int(self.__data['items'][0]['statistics']['likeCount'])

    def __str__(self):
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
