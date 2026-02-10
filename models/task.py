from __future__ import annotations
from date import Date


class Task:
    def __init__(self, title: str, date: Date):
        self.__title: str = ""
        self.__date: Date = Date(1,1,2026)

        self.title = title
        self.date = date

    # Getters
    @property
    def title(self) -> str:
        return self.__title

    @property
    def date(self) -> Date:
        return self.__date

    # Setters
    @title.setter
    def title(self, title: str):
        if len(title.strip()) > 0:
            self.__title = title
        else:
            raise ValueError("Task: Title cannot be empty")

    @date.setter
    def date(self, date: Date):
        if isinstance(date, Date):
            self.__date = date
        else:
            raise ValueError("Task: Invalid date format")

    # To String
    def __str__(self) -> str:
        return f"{self.title}\n---\n{self.date}"

    # Operator overload
    def __eq__(self, task: Task) -> bool:
        return self.title == task.title and self.date == task.date

    def __ne__(self, task: Task) -> bool:
        return not (self == task)

    def __lt__(self, task: Task) -> bool:
        if self.date != task.date:
            return self.date < task.date
        return self.title < task.title

    def __le__(self, task: Task) -> bool:
        return self <= task or self == task

    def __gt__(self, task: Task) -> bool:
        return not (self <= task)

    def __ge__(self, task: Task) -> bool:
        return not (self < task)

    # Serialization
    def to_csv(self) -> str:
        return f"{self.__title},{self.__date.to_csv()}"

    @classmethod
    def from_csv(cls, csv_line: str) -> Task:
        parts = csv_line.strip().split(",")

        if len(parts) < 4:
            raise ValueError("Task: Invalid csv format")

        title = parts[0]
        month = int(parts[1])
        day = int(parts[2])
        year = int(parts[3])
        date = Date(month, day, year)

        return cls(title, date)
