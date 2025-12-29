import re
import json
from datetime import datetime
import logging

class Utils:
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def json_serialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return sorted(list(obj))
        else:
            return obj.__dict__

    @staticmethod
    def log(level, message):
        logging.log(level, message)