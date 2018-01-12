'''

ref :  http://dropbox-sdk-python.readthedocs.io/en/master/
ref :  https://www.dropbox.com/developers/documentation/python#tutorial
ref :  http://stackoverflow.com/questions/23894221/upload-file-to-my-dropbox-from-python-script

'''




import dropbox

# login 
YOUR_ACCESS_TOKEN= your_access_token
dbx = dropbox.Dropbox(YOUR_ACCESS_TOKEN)
dbx.users_get_current_account()


# check the file list 

for entry in dbx.files_list_folder('').entries:
    print(entry.name)

# upload a file 

dbx.files_upload("just a comment ", 'test.csv')

# upload a file' :


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f, file_to)

def main():
    access_token = your_access_token
    transferData = TransferData(access_token)

    file_from = '/Users/GGV/Desktop/test.csv'
    file_to = '/test.csv'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
