from pprint import pprint
from ya_disk import YandexDisk
import requests

token = ""


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

        params = {disk_file_path: "https://disk.yandex.ru/client/disk/netology_file", "overwrite": "true"}
        response = requests.get(url=upload_url, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        url = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(url=url, data=open(filename, 'rb'))
        response.raise_for_sttatus()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
  ya = YandexDisk(token = "")
  ya.upload_file_to_disk("D/homework/http,requests_hw", "requests_http_hw_1.py")
