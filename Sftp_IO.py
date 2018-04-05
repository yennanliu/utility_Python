# python 3 

# ref 
#  http://pysftp.readthedocs.io/en/release_0.2.8/cookbook.html
#  http://pysftp.readthedocs.io/en/release_0.2.8/pysftp.html
import pandas as pd
from ftplib import FTP
import pysftp
import os





# help function 
# -------------------

def connect_to_sftp(file_path,host,username,private_key):

    srv = pysftp.Connection(host=host, username=username, private_key=private_key)
    # get current directory
    print ('--- get current directory ---')
    print (srv)
    print (srv.listdir())
    print (srv.pwd)
    # move to demo directory 
    print ('--- move to demo directory  ---')
    srv.chdir('demo')
    print (srv.pwd)
    # close the connection 
    # srv.close()
    return srv



def upload_to_sftp(connection,localpath):
    # put(localpath, remotepath=None, callback=None, confirm=True, preserve_mtime=False)
    try :
        connection.put(localpath=localpath, remotepath=None, callback=None, confirm=True, preserve_mtime=False)
        print ('dump file to SFTP success')
    except Exception as e:
        print ('dump job failed')
        print ('e')
    connection.close()
    pass



# -------------------




