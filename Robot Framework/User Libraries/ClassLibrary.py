from robot.api import logger

class ClassLibrary:
    def __init__(self, name):
        self.name = name

    def my_name_is(self, surname=None):
        if surname:
            message = f"Got name={self.name}, surname={surname}"
            logger.info(message)
            return f"My name is {surname}, {self.name} {surname}"
        else:
            message = f"Got name={self.name}, surname="
            logger.info(message)
            return f"My name is {self.name}"