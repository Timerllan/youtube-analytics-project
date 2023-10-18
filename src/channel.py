from src.you_tube_base import YouTubeBase
import json


class Channel(YouTubeBase):

    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__data = self._youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__data, indent=2, ensure_ascii=False))

    @property
    def title(self):
        return self.__data['items'][0]["snippet"]["title"]



    @property
    def video_count(self):
        return self.__data['items'][0]["statistics"]["videoCount"]

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.channel_id}"

    def to_json(self, file_json):
        with open(file_json, 'w', encoding='utf-8') as file:
            json.dump({
                'id': self.channel_id,
                "url": self.url,
                "title": self.title,
                'video_count': self.video_count,
            }, file, indent=2, ensure_ascii=False)

    @property
    def channel_id(self):
        return self.__channel_id

    def __str__(self):
        return f'{self.title} ({self.channel_id})'

    @property
    def subscriber_count(self):
        return int(self.__data['items'][0]["statistics"]["subscriberCount"])

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

