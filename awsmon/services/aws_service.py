import boto3


class AwsService:
    def __init__(self, service_type):
        if service_type == "cloudformation":
            self.get_items = self._cloudformation_get_items
            self.cache_items = self._cloudformation_cache_items
            self.monitor = self._cloudformation_monitor

    @staticmethod
    def _cloudformation_get_items():
        from awsmon.models import StackList
        from pydantic.tools import parse_obj_as
        client = boto3.client('cloudformation')
        paginator = client.get_paginator('list_stacks')
        for page in paginator.paginate():
            item_list = parse_obj_as(StackList, page)
            for item in item_list.StackSummaries:
                yield item

    def _cloudformation_cache_items(self, cache_service):
        for item in self.get_items():
            item.cache(cache_service)

    def _cloudformation_monitor(self, notifier, cache_service, expression: str = ".*", interval=30):
        from time import sleep
        import re
        for item in self.get_items():
            if re.search(expression, item.StackName):
                if cache_service.get(item.StackId) != item.StackStatus:
                    notifier.notify(item.StackName, f"{cache_service.get(item.StackId)} >>> {item.StackStatus}")
                    print(f"Found status change for {item.StackName} from state {cache_service.get(item.StackId)} to state {item.StackStatus}")
                cache_service.set(item.StackId, item.StackStatus)
        sleep(interval)
