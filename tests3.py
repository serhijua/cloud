import boto3

bucket_name = '171422-serhij'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.put_object(Key='another.txt', Body=open('test.txt', 'rb'))
