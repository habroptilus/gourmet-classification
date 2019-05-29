from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

test_folder_id = "1sXEc0k3KwYpU5_rdyb9dq60De4uLzqQJ"
root_folder_id = "root"
gourmet_id = "1bjbFGHOKPt_krVyewjoeLwRYLTKuwkMK"

# 承認

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


################################################################
# サンプル1
################################################################

# Hello.txtテキストを作成し中身に「Hello」と記載。
print("sample 1")
#file1 = drive.CreateFile({'title': 'Hello1.txt'})
# file1.SetContentString('Hello1')
# アップロード
# file1.Upload()


#file1_ = drive.CreateFile({'title': 'Hello1_.txt'})
# file1_.SetContentString('Hello1_')
# アップロード
# file1_.Upload()


################################################################
# サンプル2
################################################################
print("sample 2")
# 一覧を取得し表示

query = f"'{test_folder_id}' in parents and trashed=false"
file_list = drive.ListFile({'q': query}).GetList()
print(file_list)
for file in file_list:
    print(f"title: {file['title']}, id: {file['id']}")


################################################################
# サンプル3
################################################################
print("sample 3")
# 指定したIDのデータを削除
# for file in file_list:
#   x = drive.CreateFile({'id': file['id']})
#  print(f"delete : { file['title'] }")
# x.Delete()


################################################################
# サンプル4
################################################################
print("sample 4")
# 指定したIDのデータをダウンロード
#file3 = drive.CreateFile({'id': file_list[1]["id"]})
# file3.GetContentFile('hoge1.txt')


################################################################
# サンプル5
################################################################
print("sample 5")
# ローカルにあるdata.txtをアップロード
#file2 = drive.CreateFile()
# file2.SetContentFile('hoge1.txt')
# file2.Upload()
