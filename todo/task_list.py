from datetime import datetime, date, timedelta
from pprint import pprint as pp

from todo.status_enum import StatusEnum
from todo.task import Task



class TaskList:
    def __init__(self, tasks: list[Task] | None = None):
        self.tasks: list[Task] = tasks or []

    def make_all_done(self):
        for task in self.tasks:
            task.status = StatusEnum.COMPLETED

    def show_tasks_by_date(self, dt=None) -> list[Task]:
        if dt is None:
            dt = date.today()

        result = []
        for task in self.tasks:
            if task.start_dt.date() == dt:
                result.append(task)
        return result

    def find_tasks(self, txt: str) -> list[Task]:
        result = []
        txt_lower = txt.lower()

        for task in self.tasks:
            if txt_lower in task.name.lower() or txt_lower in task.description.lower():
                result.append(task)
        return result

    def shift_tasks_by_one_day(self):

        for task in self.tasks:
            task.start_dt += timedelta(days=1)

    def get_specific_tasks(self, **filters) -> list[Task]:
        if not filters:
            return self.tasks

        result = []
        for task in self.tasks:
            counter = 0
            if 'status' in filters and filters['status'] == task.status:
                counter += 1
            if 'location' in filters and filters['location'] == task.location:
                counter += 1
            if 'start_dt' in filters and filters['start_dt'] <= task.start_dt:
                counter += 1
            if 'end_dt' in filters and filters['end_dt'] >= task.start_dt:
                counter += 1
            if counter == len(filters):
                result.append(task)
        return result

    def order_by(self, key: str, ascending: bool=True) -> list[Task]:
        return sorted(self.tasks, key=lambda task: getattr(task, key), reverse=not ascending)


    def show_tasks_by_status(self, status: StatusEnum) -> list[Task]:

        result = []
        for task in self.tasks:
            if task.status == status:
                result.append(task)
        return result

    def __str__(self) -> str:
        return f'List of tasks: {self.tasks}'

    __repr__ = __str__



t1 = Task('Improve python', datetime(2025, 2, 17, 12, 39), 51, location='Home', description='Learn quickly')
t2 = Task('Learn FastApi.', datetime(2025, 3, 17, 14, 5), 60, location='Home')
t3 = Task('Learn Docker', datetime(2025, 2, 17, 10, 5), 60, location='Home')

t2.status = StatusEnum.COMPLETED

tl = TaskList([t1, t2, t3])
# tl.shift_tasks_by_one_day()


# pp(tl.tasks)
# tl.show_tasks_by_date()
# pp(tl.show_tasks_by_date(date(2025, 2, 17)))
# pp(tl.show_tasks_by_status('done'))
# pp(tl.find_tasks('learn'))
# pp(tl.get_specific_tasks(status=StatusEnum.NEW, location='Home', start_dt=datetime(2025, 1, 17, 12, 39), end_dt=datetime(2026, 3, 17, 14, 5)))
pp(tl.order_by('start_dt'))