from enum import Enum


class StatusEnum(str, Enum):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    FAILED = 'Failed'


