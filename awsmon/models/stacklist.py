from pydantic.dataclasses import dataclass
from awsmon.models.stack import Stack


@dataclass
class StackList:
    StackSummaries: list[Stack]
