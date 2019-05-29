from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveController:
    def __init__(self):
        """認証."""
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)

    def fetch_fileinfo_list(self, folder_id):
        """dir以下のファイル一覧を取得する."""
        query = f"'{folder_id}' in parents and trashed=false"
        file_list = self.drive.ListFile({'q': query}).GetList()
        return file_list

    def delete_files(self, file_list):
        """指定したfileのidリストに該当するファイルを一括削除する."""
        for i in file_list:
            x = self.drive.CreateFile({'id': i})
            x.Delete()

    def download_files(self, file_list, dir_name):
        """idリストに該当するfileをdir_name以下にダウンロードする."""
        for file in file_list:
            x = self.drive.CreateFile({'id': file['id']})
            x.GetContentFile(f"{dir_name}/{file['title']}")

    def upload_files(self, filepath_list, folder_id):
        """ローカルにあるファイルをアップロードする."""
        for p in filepath_list:
            file = self.drive.CreateFile(
                {'title': p.name, 'mimeType': f"image/{p.suffix[1:]}", 'parents': [{'kind': 'drive#fileLink', 'id': folder_id}]})
            file.SetContentFile(p)
            file.Upload()


if __name__ == "__main__":
    #from pathlib import Path
    test_folder_id = "1sXEc0k3KwYpU5_rdyb9dq60De4uLzqQJ"
    root_folder_id = "root"
    gourmet_folder_id = "1bjbFGHOKPt_krVyewjoeLwRYLTKuwkMK"
    model_folder_id = "1fbDIiefwMon8wF7VlOFUY15oTIufF6_Y"
    photo_2019 = "19pyC-1HplZa0Aby2DtMarozjhA"

    controller = GoogleDriveController()
    file_list = controller.fetch_fileinfo_list(photo_2019)
    #controller.download_files(file_list, dir_name="images")
    print(len(file_list))
