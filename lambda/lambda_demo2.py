"""

https://stackoverflow.com/questions/50352545/kinesis-firehose-lambda-transformation

"""

from __future__ import print_function

import base64
#import msgpack
import json

print('Loading function')

event = {'invocationId': 'a5e305b8-7609-4ed8-aeaa-39aaa59410bd', 'deliveryStreamArn': 'arn:aws:xxxx', 'region': 'us-east-1', 'records': [{'recordId': '49643964113682774284088347762983021764602109853127671810000000', 'approximateArrivalTimestamp': 1693409404313, 'data': 'eyJDSEFOR0UiOi0wLjgyLCJQUklDRSI6NDUuOTcsIlRJQ0tFUl9TWU1CT0wiOiJXRkMiLCJTRUNUT1IiOiJGSU5BTkNJQUwifQ=='}, {'recordId': '49643964113682774284088347763384385136714167288885936130000000', 'approximateArrivalTimestamp': 1693409409425, 'data': 'eyJDSEFOR0UiOi0xLjI3LCJQUklDRSI6MjAuMDgsIlRJQ0tFUl9TWU1CT0wiOiJNTUIiLCJTRUNUT1IiOiJFTkVSR1kifQ=='}, {'recordId': '49643964113682774284088347763855866206363872941899251714000000', 'approximateArrivalTimestamp': 1693409414537, 'data': 'eyJDSEFOR0UiOjAuMTksIlBSSUNFIjo0Mi4xNiwiVElDS0VSX1NZTUJPTCI6IktGVSIsIlNFQ1RPUiI6IkVORVJHWSJ9'}, {'recordId': '49643964113682774284088347764283825946507452013342621698000000', 'approximateArrivalTimestamp': 1693409419657, 'data': 'eyJDSEFOR0UiOi05LjMzLCJQUklDRSI6OTEuNjIsIlRJQ0tFUl9TWU1CT0wiOiJORlMiLCJTRUNUT1IiOiJFTkVSR1kifQ=='}, {'recordId': '49643964113682774284088347764636832285834924075954208770000000', 'approximateArrivalTimestamp': 1693409424782, 'data': 'eyJDSEFOR0UiOjAuMjMsIlBSSUNFIjoxOS42MSwiVElDS0VSX1NZTUJPTCI6IlBMTSIsIlNFQ1RPUiI6IkZJTkFOQ0lBTCJ9'}, {'recordId': '49643964113682774284088347765038195657946981305554042882000000', 'approximateArrivalTimestamp': 1693409429895, 'data': 'eyJDSEFOR0UiOi0yLjQzLCJQUklDRSI6MzIuNDIsIlRJQ0tFUl9TWU1CT0wiOiJWVlkiLCJTRUNUT1IiOiJIRUFMVEhDQVJFIn0='}, {'recordId': '49643964113682774284088347765412962662027516762029817858000000', 'approximateArrivalTimestamp': 1693409435011, 'data': 'eyJDSEFOR0UiOjAuMDgsIlBSSUNFIjo0Ljg2LCJUSUNLRVJfU1lNQk9MIjoiSEpLIiwiU0VDVE9SIjoiVEVDSE5PTE9HWSJ9'}, {'recordId': '49643964113682774284088347765774431482092291160144871426000000', 'approximateArrivalTimestamp': 1693409440135, 'data': 'eyJDSEFOR0UiOjAuMiwiUFJJQ0UiOjguOTQsIlRJQ0tFUl9TWU1CT0wiOiJXU0IiLCJTRUNUT1IiOiJSRVRBSUwifQ=='}, {'recordId': '49643964113682774284088347766152825263631670504144764930000000', 'approximateArrivalTimestamp': 1693409445244, 'data': 'eyJDSEFOR0UiOjEuNTEsIlBSSUNFIjoxNTMuODksIlRJQ0tFUl9TWU1CT0wiOiJNSk4iLCJTRUNUT1IiOiJSRVRBSUwifQ=='}, {'recordId': '49643964113682774284088347766507040528778757195931058178000000', 'approximateArrivalTimestamp': 1693409450360, 'data': 'eyJDSEFOR0UiOjAuMTUsIlBSSUNFIjoyLjM1LCJUSUNLRVJfU1lNQk9MIjoiU0VEIiwiU0VDVE9SIjoiSEVBTFRIQ0FSRSJ9'}, {'recordId': '49643964113682774284088347766922911010726189975627366402000000', 'approximateArrivalTimestamp': 1693409455478, 'data': 'eyJDSEFOR0UiOi03LjEsIlBSSUNFIjo2OC43LCJUSUNLRVJfU1lNQk9MIjoiU0xXIiwiU0VDVE9SIjoiRU5FUkdZIn0='}, {'recordId': '49643964113682774284088347767279544127512505994482548738000000', 'approximateArrivalTimestamp': 1693409460597, 'data': 'eyJDSEFOR0UiOjMuNzcsIlBSSUNFIjoyMjIuNjgsIlRJQ0tFUl9TWU1CT0wiOiJRWFoiLCJTRUNUT1IiOiJGSU5BTkNJQUwifQ=='}]}


def lambda_handler(event, context):
  output = []

  for record in event['records']:
    #payload = msgpack.unpackb(base64.b64decode(record['data']), raw=False)

    # Do custom processing on the payload here
    output_record = {
       'recordId': record['recordId'],
       'result': 'Ok',
       #'data': base64.b64encode(json.dumps(payload).encode('utf-8') + b'\n').decode('utf-8')
       'data': 'data'
    }
    output.append(output_record)

  print('Successfully processed {} records.'.format(len(event['records'])))
  return {'records': output}


if __name__ == '__main__':
	output = lambda_handler(event, 'context')
	print (f"output = {output}")