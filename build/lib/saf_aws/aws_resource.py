from dagster import resource, StringSource

import boto3
from urllib.request import urlopen, urlretrieve
from io import StringIO
import pandas as pd



class AWSResource:
    # AWS methods
    ######################
    def s3_put(self, df_data_asset, bucket_name, file_path):
        # Adds an object to a bucket.

        s3 = boto3.resource('s3')
        csv_buffer = StringIO()
        df_data_asset.to_csv(csv_buffer, index = False)
        s3.Object(bucket_name, file_path).put(Body=csv_buffer.getvalue())

        return df_data_asset
    

    def s3_get(self, bucket_name, file_path):
        # Retrieves objects from Amazon S3.

        s3 = boto3.resource('s3')
        obj = s3.Object(bucket_name, file_path)

        df_data_asset = pd.read_csv(StringIO(obj.get()['Body'].read().decode('utf-8')))

        return df_data_asset


@resource(
    description="A AWS resource.",
)
def initiate_aws_resource(context):
    return AWSResource()