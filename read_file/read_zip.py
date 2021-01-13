import zipfile
import filetype
import os


def read_file(file_path):
    # 先判斷是否為資料夾
    if os.path.isdir(file_path):
        print('It is a folder.')
    elif os.path.isfile(file_path):
        print('It is a file.')
        # 判斷檔案類型
        file_type = filetype.guess(file_path)
        if file_type == 'application/zip':
            # 進入壓縮檔並讀取，也要確認裡面偶沒有壓縮檔
            zip_file = zipfile.ZipFile(file_path, 'r')
            # 
