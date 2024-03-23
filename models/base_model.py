#!/usr/bin/python3
"""This script is the base model"""


import datetime
import uuid


class BaseModel:
    """class that defines all common attributes/methods for other classes"""

    def __init__(self, my_number = '', name = ''):
        """define Public instance attributes"""

        self.my_number = my_number
        self.name = name
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = None
        self.to_dict()

    def save(self):
        """Update the date of modification"""

        self.updated_at = datetime.datetime.now()
        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()

    def to_dict(self):
        """create a dic"""

        if self.updated_at == None:
            self.updated_at = self.created_at

        self.__dict__ = {
                'my_number': self.my_number,
                'name': self.name,
                'updated_at': self.updated_at,
                'id': str(self.id),
                'created_at': self.created_at
                }
        return self.__dict__

    def __str__(self):
        """return the folowing format"""

        return ('[{}] ({}) {}'.format(__class__.__name__, self.id, self.__dict__))
