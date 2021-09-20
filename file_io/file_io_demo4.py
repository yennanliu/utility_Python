"""
file_io_demo4

- Ref
    - https://stackoverflow.com/questions/6475328/how-can-i-read-large-text-files-in-python-line-by-line-without-loading-it-into/6475407
    - https://gist.github.com/iyvinjose/e6c1cb2821abd5f01fd1b9065cbc759d
"""

def read_lines_from_file_as_chunks(file_name, chunk_size, callback, return_whole_chunk=False):

    # same func as we use in file_io_demo3
    def read_file_in_chunks(file_obj, chunk_size=1024):

        while True:
            data = file_obj.read(chunk_size)

            if not data:
                break

            yield data

    fp = open(file_name)
    data_left_over = None

    # loop over chunks
    for chunk in read_file_in_chunks(fp):
        # if uncompleted data exists
        if data_left_over:
            print ("data_left_over found!")
            cuurent_chunk = data_left_over + chunk

        else:
            cuurent_chunk = chunk

        # split the chunk by new lines
        #lines = cuurent_chunk.splitlines()
        lines = cuurent_chunk.split('\n')

        # check if line is complete
        if cuurent_chunk.endswith('\n'):
            data_left_over = None

        else:

            data_left_over = lines.pop()

        if return_whole_chunk:
            print ('>>> return whole chunk')
            callback(data=lines, eof=False, file_name=file_name)

        else:
            print ('>>> return per line')
            for line in lines:
                callback(data=line, eof=False, file_name=file_name)
                pass

    if data_left_over:

        current_chunk = data_left_over

        if cuurent_chunk is not None:
            lines = cuurent_chunk.split('/n')

            if return_whole_chunk:
                callback(data=lines, eof=False, file_name=file_name)

            else:
                for line in lines:
                    callback(data=line, eof=False, file_name=file_name)
                    pass

    callback(data=None, eof=True, file_name=file_name)


def process_lines(data, eof, file_name):

    print ('data = ', str(data))

    # if not eof:
    #     print ('not eof')
    # else:
    #     print ('eof')

if __name__ == '__main__':
    
    chunk_size = 2048
    file_name = 'test3.txt'

    """
    NOTE : process_lines is the callback func that define the logics we process each line the loaded data
    """
    read_lines_from_file_as_chunks(
        file_name, 
        chunk_size=chunk_size, 
        callback=process_lines
    )