from dagster import resource

from urllib.request import urlopen, urlretrieve
import zipfile
import pandas as pd



class AWSResource:
    # AWS methods
    ######################
    def get_url_to_latest_asset(self, aws_asset):
        # Fetches the latest url of aws asset

        latest_updates_url = 'http://data.awsproject.org/awsv2/lastupdate.txt'
        latest_updates_text = str(urlopen(latest_updates_url).read())

        if aws_asset == "events": 
            latest_asset_url = latest_updates_text.split('\\n')[0].split(' ')[2]
        elif aws_asset == "mentions":
            latest_asset_url = latest_updates_text.split('\\n')[1].split(' ')[2]

        return latest_asset_url


@resource(
    description="A AWS resource.",
)
def initiate_aws_resource(context):
    return AWSResource()