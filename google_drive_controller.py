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

    def delete_files(self, file_list):
        """指定したfileのidリストに該当するファイルを一括削除する."""
        for i in file_list:
            x = self.drive.CreateFile({'id': i})
            x.Delete()

    def download_files(self, id_list):
        """idリストに該当するfileをダウンロードする."""
        pass

    def upload_files(self, filepath_list, folder_id):
        """ローカルにあるファイルをアップロードする."""
        for p in filepath_list:
            file = self.drive.CreateFile(
                {'title': p.name, 'mimeType': f"image/{p.suffix[1:]}", 'parents': [{'kind': 'drive#fileLink', 'id': folder_id}]})
            file.SetContentFile(p)
            file.Upload()


if __name__ == "__main__":
    from pathlib import Path
    controller = GoogleDriveController()
    controller.upload_files([Path("./kakapo.jpg")], "root")
