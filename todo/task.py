from datetime import datetime, timedelta

from todo.status_enum import StatusEnum


class Task:
    def __init__(self, name: str, start_dt: datetime, duration: int, description: str = '',
                 location: str | None = None):
        self.name = name
        self.location = location
        self.start_dt = start_dt
        self.duration = duration
        self.description = description
        self.status: StatusEnum = StatusEnum.NEW

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name.strip()) == 0:
            raise ValueError('Task name cannot be empty')

        if len(new_name.strip()) <= 3:
            raise ValueError('Task name must be longer than 3 characters')

        self._name = new_name.strip()

    @property
    def start_dt(self):
        return self._start_dt

    @start_dt.setter
    def start_dt(self, new_start_dt):
        if not isinstance(new_start_dt, datetime):
            raise TypeError('Task start must be datetime.')

        if datetime.now() + timedelta(minutes=15) >= new_start_dt:
            raise ValueError('Date must be in the future')

        self._start_dt = new_start_dt

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if new_duration < 15:
            raise ValueError('Task must be longer than 15 minutes')

        self._duration = new_duration

    def toggle_status(self):
        if self.status == StatusEnum.COMPLETED:
            self.status = StatusEnum.IN_PROGRESS
        else:
            self.status = StatusEnum.COMPLETED

    @staticmethod
    def _time_until(dt: datetime) -> tuple[int, int]:
        current_date = datetime.now()

        if dt <= current_date:
            return 0, 0

        delta: timedelta = dt - current_date
        days = delta.days
        hours = delta.seconds // 3600
        return days, hours

    def __str__(self) -> str:
        days, hours = self._time_until(self.start_dt)

        return (f'Task: {self.name}, ⏰️ {days} days and {hours} hours left,'
                f' {self.status.value}')

    __repr__ = __str__

# t1 = Task('Improve python', datetime(2025, 2, 17, 12,39 ), 51,location='Home')
# t2 = Task('Learn FastApi.', datetime(2025, 2, 5, 10, 5), 60,location='Home')
# t1.toggle_status()
#
#
# # print(t1.name)
# print(t1)
# print(t2)

# if __name__ == '__main__':
#     while True:
#         name = input('Enter task name or type exit: ')
#         if name == 'exit':
#             break
#         try:
#             t = Task(name, '', '', '', '')
#             print('Your task is ', t)
#             break
#         except ValueError as e:
#             print(e)
