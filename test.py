from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# 承認
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


################################################################
# サンプル1
################################################################

# Hello.txtテキストを作成し中身に「Hello」と記載。
print("sample 1")
file1 = drive.CreateFile({'title': 'Hello1.txt'})
file1.SetContentString('Hello1')
# アップロード
file1.Upload()


file1_ = drive.CreateFile({'title': 'Hello1_.txt'})
file1_.SetContentString('Hello1_')
# アップロード
file1_.Upload()


################################################################
# サンプル2
################################################################
print("sample 2")
# 一覧を取得し表示
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file1 in file_list:
    print(f"title: {file1['title']}, id: {file1['id']}")


################################################################
# サンプル3
################################################################
print("sample 3")
# 指定したIDのデータを削除
file3 = drive.CreateFile({'id': file_list[0]["id"]})
file3.Delete()


################################################################
# サンプル4
################################################################
print("sample 4")
# 指定したIDのデータをダウンロード
file3 = drive.CreateFile({'id': file_list[1]["id"]})
file3.GetContentFile('hoge1.txt')


################################################################
# サンプル5
################################################################
print("sample 5")
# ローカルにあるdata.txtをアップロード
file2 = drive.CreateFile()
file2.SetContentFile('hoge1.txt')
file2.Upload()
