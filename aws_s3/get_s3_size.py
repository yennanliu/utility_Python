import boto3


def get_client(bucket_name):
  client = boto3.client('s3')
  bucket = boto3.resource('s3').Bucket(bucket_name)
  return client, bucket

def get_dirs(bucket_name, prefix):
  dirs = []
  result = client.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
  for o in result.get('CommonPrefixes'):
      dirs.append(o.get('Prefix'))
      return dirs

def get_size_by_date(date_time, bucket, dirs):
  total_size = 0
  file_list = []
  for dir in dirs:
      year, month, date = date_time.split("/")
      #prefix = f"{dir}2023/05/03/"
      prefix = f"{dir}{year}/{month}/{date}/"
      #print (f"prefix = {prefix}")
      for object in bucket.objects.filter(Prefix=prefix):
        if date_time in object.key:
          #print (object.key)
          file_list.append(object.key)
          total_size += object.size

  #print (file_list)
  print (total_size)
  return total_size


if __name__ == '__main__':
  my_bucket = "my_bucket"
  prefix = "prefix"
  date_time = "2021/01/01"
  client, bucket = get_client(my_bucket)
  dirs = get_dirs(my_bucket, prefix)
  data_size = get_size_by_date(date_time, my_bucket, dirs)
