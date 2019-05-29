from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveController:
    def __init__(self):
        """認証."""
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)

    def fetch_fileinfo_list(self, dir):
        """dir以下のファイル一覧を取得する."""
        pass

    def delete_files(self, file_list, dir):
        """dir以下の指定したfileのidリストに該当するファイルを一括削除する."""
        pass

    def download_files(self, id_list):
        """idリストに該当するfileをダウンロードする."""
        pass

    def upload_files(self, filepath_list):
        """ローカルにあるファイルをアップロードする."""
