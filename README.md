# The OSS Social Analytics Framework - AWS library
This library provides a [resource](https://docs.dagster.io/concepts/resources) to interact with [AWS](https://aws.amazon.com/) cloud computing services.

It is part of the [Social Analytics Framework](https://github.com/lantrns-analytics/saf_core). ease visit the repo for more information on the framework, its mission and how to use it.

&nbsp;


# Configurations
This library uses the `boto3` package to interact with AWS, which requires your credentials. Those should be defined in the following file, starting at the root (~) of your project: `~/.aws/credentials`

Example:

```
[default]
aws_access_key_id="{{ env_var('AWS_ACCESS_KEY_ID') }}"
aws_secret_access_key="{{ env_var('AWS_SECRET_ACCESS_KEY') }}"
```


# Methods
## aws_resource.initiate_aws_resource
Initialize resource to interact with AWS cloud computing services.

Configurations:
- None

Example:
```
my_aws_resource = aws_resource.initiate_aws_resource()
```

## aws_resource.s3_put
Adds an object to a bucket.

Parameters:
- df_data_asset: Dataframe to add
- bucket_name: Destination bucket where to add dataframe
- file_path: Path of dataframe to be added in bucket

Returns:
- df_data_asset: Dataframe that's been added

Example:
```
latest_asset_url = context.resources.aws_resource.s3_put(df_data_asset, bucket_name, file_path)
```

## aws_resource.s3_get
Retrieves objects from Amazon S3.

Parameters:
- bucket_name: Bucket where to retrieve dataframe
- file_path: Path of dataframe to be retrieved in bucket

Returns:
- df_data_asset: Dataframe that's been retrieved

Example:
```
latest_asset_url = context.resources.aws_resource.s3_put(df_data_asset, bucket_name, file_path)
```

&nbsp;

# Development of library
- Once improvements have been added to library
- Compile a new version: `python setup.py bdist_wheel`
- Commit branch and PR into new release branch
- Point projects to new release branch
