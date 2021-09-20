"""
file_io_demo3

Load txt file with lazy func (yield) and chunk_size

https://www.code-learner.com/python-read-big-file-example/

"""

# a lazy func that will read piece of data with chunk_size each time
def read_file_in_chunks(file_obj, chunk_size=1024):

    while True:

        data = file_obj.read(chunk_size)

        if not data:
            break

        yield data 


# main run func
def main(file_name, chunk_size):

    piece_count = 0

    with open(file_name) as f:

        for piece in read_file_in_chunks(f, chunk_size):

            # your data process logic
            #proess_func(data)
            print ("-------------------------------")
            print ("piece_count =", str(piece_count))
            print ("-------------------------------")
            print (piece)

            piece_count += 1

if __name__ == '__main__':
    chunk_size = 2048
    file_name = 'test3.txt'
    main(file_name, chunk_size)