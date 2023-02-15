## AWSMON
Monitor AWS Cloudformation stacks based on a regex pattern. Will use macos notifications when any status change is detected.

It has been developed using factory pattern so it potentially could be used to monitor and notify status changes in other AWS resources.

## Prereqs
Setup your profiles using the aws cli

```sh
aws configure --profile PROFILE_NAME
```

You can also leave out the `--profile PROFILE_NAME` param to set your `default` credentials

Refer to this doc for more information
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

## Setup

### pip
```
pip install awsmon
```
### source
 ```
 git clone git@github.com:sergiopena/awsmon.git
 cd awsmon
 python setup.py install
 ```

## Tests
No test at the moment... SHAME!

## How to use?
* An exported env var named AWS_PROFILE is required, as this is the profile that will be used to retrieve running ec2 instances
* Profile must include the region, currently we only support one region.
* Run `awsmon -h` for help
* Run `awsmon -s stack_name` to monitor changes on any stack name /.*stack_name.*/
* Run `awsmon -s stack_name -i 60` to monitor changes on any stack name /.*stack_name.*/ and check every 60 seconds, try to avoid throttling by AWS.

It will show notifications when a stack status changes and changes will also be logged to the console.
```
awsmon -s application
Found status change for application-private-lambda-iac from state None to state CREATE_IN_PROGRESS
Found status change for application-private-lambda-iac from state CREATE_IN_PROGRESS to state CREATE_COMPLETE
```

## Contribute
Contributions are more than welcomed! 

## Distribute
```
python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
```

## Credits
Inspired by bored me developing infrastructure.

## License
BSD
