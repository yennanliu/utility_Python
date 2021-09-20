
# https://www.code-learner.com/python-read-big-file-example/

# https://stackoverflow.com/questions/6475328/how-can-i-read-large-text-files-in-python-line-by-line-without-loading-it-into/6475407
# https://gist.github.com/iyvinjose/e6c1cb2821abd5f01fd1b9065cbc759d


"""
a lazy func that will read piece of data with chunk_size each time
"""
def read_file_in_chunks(file_obj, chunk_size=1024)

    while True:

        data = file_obj.read(chunk_size)

        if not data:
            break

        yield data 


def main(file_name):

    with open(file_name) as f:

        for piece in read_file_in_chunks(f):

            # your data process logic
            #proess_func(data)
            print (piece)

if __name__ == '__main__':
    file_name = 'test3.txt'
    main()