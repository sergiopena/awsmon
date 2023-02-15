from awsmon.services.notifier import Notifier
from awsmon.services.argument_parser import parse_args
from awsmon.services.cache import CacheService
from awsmon.services.aws_service import AwsService

arguments = parse_args()
notifier = Notifier("cloudformation")
cache_service = CacheService()
aws_service = AwsService('cloudformation')

aws_service.cache_items(cache_service)

notifier.notify("Startup", f"Monitoring {arguments.stack}")

while True:
    aws_service.monitor(expression=arguments.stack,
                        interval=arguments.interval,
                        notifier=notifier,
                        cache_service=cache_service)


