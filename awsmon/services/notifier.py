from subprocess import Popen


def notify_cloudformation(title: str, message: str):
    notification = 'display notification "' + message + '" with title "' + title + '" sound name "Crystal"'
    Popen(['osascript', '-e', notification])


class Notifier(object):
    def __init__(self, type):
        self.type: str

        if type == "cloudformation":
            self.notify = notify_cloudformation

