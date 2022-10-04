# The OSS Social Analytics Framework - AWS library
This library provides a [resource](https://docs.dagster.io/concepts/resources) to interact with [AWS](https://aws.amazon.com/) cloud computing services.

It is part of the [Social Analytics Framework](https://github.com/lantrns-analytics/saf_core). ease visit the repo for more information on the framework, its mission and how to use it.

&nbsp;


# Library

# Methods
## aws_resource.initiate_aws_resource
Initialize resource to interact with AWS cloud computing services.

Configurations:
- None

Example:
```
my_aws_resource = aws_resource.initiate_aws_resource()
```

## aws_resource.get_url_to_latest_asset
Fetches the latest url for a specific aws asset.

Parameters:
- aws_asset: Which aws asset to mine. Values can either be `events`, `mentions` or `gkg`

Returns:
- latest_asset_url: URL of latest asset

Example:
```
latest_asset_url = context.resources.aws_resource.get_url_to_latest_asset(aws_asset)
```

&nbsp;

# Development of library
- Once improvements have been added to library
- Compile a new version: `python setup.py bdist_wheel`
- Commit branch and PR into new release branch
- Point projects to new release branch
