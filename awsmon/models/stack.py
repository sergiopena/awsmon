from pydantic.dataclasses import dataclass


@dataclass
class Stack:
    StackName: str
    StackStatus: str
    StackId: str

    def cache(self, cache_service):
        cache_service.set(self.StackId, self.StackStatus)
