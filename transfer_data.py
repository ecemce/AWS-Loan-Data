import boto3
import pandas as pd

aws_access_key_id= "AKIAS2U7TRLJDWNHXDFJ"
aws_secret = "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"

aws = boto3.client("firehose",region_name = "eu-central-1",
                  aws_access_key_id = aws_access_key_id,
                  aws_secret_access_key = aws_secret)


s3 = boto3.resource('s3')
bucket = s3.Bucket('loans3bucket')
obj = bucket.Object(key='yourFile.extension')
response = obj.get()
lines = response[u'Body'].read().split('\n')

def lines(file_path: str) -> int:
    return sum(1 for _ in open(file_path))

def to_csv(row) -> str: return ','.join(row) + '\n'
num_lines = lines("loan.csv")

records = []
with open("loan.csv", 'r') as csv_file:
        loan_data_reader = csv.reader(csv_file)

        record_count = 0
        sum_record = 0

        for loan_row in loan_data_reader:
            records.append({"Data": to_csv(loan_row)})
            print(records)
            exit()
            record_count += 1
            sum_record += 1
            if record_count == 500:
                aws.put_record_batch(
                        DeliveryStreamName="loan_stream",
                        Records=records)

                print('[INFO] Transferred: %d, Percentage: %%%.3f' % (sum_record, 100 * sum_record / num_lines))
                records.clear()
                record_count = 0
