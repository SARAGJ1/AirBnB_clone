#!/usr/bin/python3
import datetime
import uuid


class BaseModel:

    def __init__(self, my_number = '', name = ''):
        self.my_number = my_number
        self.name = name
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = None
        self.to_dict()

    def save(self):
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def to_dict(self):
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
        return ('[{}] ({}) {}'.format(__class__.__name__, self.id, self.__dict__))
