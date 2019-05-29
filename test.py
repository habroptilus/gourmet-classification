from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

test_folder_id = "1sXEc0k3KwYpU5_rdyb9dq60De4uLzqQJ"
root_folder_id = "root"
gourmet_folder_id = "1bjbFGHOKPt_krVyewjoeLwRYLTKuwkMK"
model_folder_id = "1fbDIiefwMon8wF7VlOFUY15oTIufF6_Y"

# 承認

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


################################################################
# サンプル1
################################################################

# Hello.txtテキストを作成し中身に「Hello」と記載。
print("sample 1")
# file1 = drive.CreateFile({'title': 'Hello1.txt'})
# file1.SetContentString('Hello1')
# アップロード
# file1.Upload()


# file1_ = drive.CreateFile({'title': 'Hello1_.txt'})
# file1_.SetContentString('Hello1_')
# アップロード
# file1_.Upload()


################################################################
# サンプル2
################################################################
print("sample 2")
# 一覧を取得し表示

query = f"'{root_folder_id}' in parents and trashed=false"
file_list = drive.ListFile({'q': query}).GetList()
# print(file_list)
for file in file_list:
    print(f"title: {file['title']}, id: {file['id']}")


################################################################
# サンプル3
################################################################
print("sample 3")
# 指定したIDのデータを削除
for file in file_list:
    x = drive.CreateFile({'id': file['id']})
    print(f"delete : { file['title']} ({file['id']})")
    x.Delete()


################################################################
# サンプル4
################################################################
print("sample 4")
# 指定したIDのデータをダウンロード
# file3 = drive.CreateFile({'id': "1bjbFGHOKPt_krVyewjoeLwRYLTKuwkMK"})
# file3.GetContentFile('disney.jpg')


################################################################
# サンプル5
################################################################
print("sample 5")
# ローカルにあるdata.txtをアップロード
# file2 = drive.CreateFile(
#    {'title': "hoge.jpg", 'mimeType': 'image/jpeg', 'parents': [{'kind': 'drive#fileLink', 'id': test_folder_id}]})
# file2.SetContentFile('kakapo.jpg')
# file2.Upload()
