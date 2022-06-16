import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from datetime import datetime
from cloudlog_meta import CloudlogMeta


class CloudLog(metaclass=CloudlogMeta):

    def __init__(self, servicekey: str, filename: str):
        self.__servicekey = servicekey
        self.__filename = filename
        self.__cred = credentials.Certificate(self.__servicekey)
        firebase_admin.initialize_app(self.__cred, {
            'storageBucket': "loggerspython.appspot.com"
        })
        self.__bucket = storage.bucket()
        self.__blob = self.__bucket.blob(self.__filename)

    def success(self):
        self.write_file("No se encontro ningun error o advertencia en el codigo")
        self.upload_file(self.__filename)

    def warning(self, msg: str):
        self.write_file(f"Advertencia: {msg}")
        self.upload_file(self.__filename)

    def error(self, msg: str):
        self.write_file(f"Error: {msg}")
        self.upload_file(self.__filename)

    def write_file(self, msg: str):
        date = datetime.today()
        archive = open(self.__filename, 'a')
        archive.write('\n' + msg + f", {date}")
        archive.close()

    def upload_file(self, filename: str):
        with open(filename, 'rb') as my_file:
            self.__blob.upload_from_file(my_file)
