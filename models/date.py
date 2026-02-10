from __future__ import annotations # Allows 'Date' to be used as a type within the class


class Date:
    def __init__(self, month: int, day: int, year: int):
        self.__year: int = 2026
        self.__month: int = 1
        self.__day: int = 1

        self.year: int = year
        self.month: int = month
        self.day: int = day

    def __to_int(self) -> int:
        return self.__year * 10000 + self.__month * 100 + self.__day

    def __is_leap_year(self, year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __get_days_in_month(self, month: int, year: int) -> int:
        days_per_month = [0,
                          31, # JAN
                          28, # FEB
                          31, # MAR
                          30, # APR
                          31, # MAY
                          30, # JUN
                          31, # JUL
                          31, # AUG
                          30, # SEP
                          31, # OCT
                          30, # NOV
                          31 # DEC
                          ]
        # If it is a leap year, February has 29 days
        if month == 2 and self.__is_leap_year(year):
            return 29

        return days_per_month[month]

    # Getters
    @property
    def month(self) -> int:
        return self.__month

    @property
    def day(self) -> int:
        return self.__day

    @property
    def year(self) -> int:
        return self.__year

    # Setters
    @month.setter
    def month(self, month: int):
        if 0 < month < 13:
            max_days = self.__get_days_in_month(month, self.__year)

            if self.__day > max_days:
                raise ValueError("Date: Invalid day. The day does not exist in this month.")

            self.__month = month
        else:
            raise ValueError("Date: Invalid month. It must be between 1 and 12.")

    @day.setter
    def day(self, day: int):
        max_days = self.__get_days_in_month(self.__month, self.__year)

        if 0 < day <= max_days:
            self.__day = day
        else:
            raise ValueError("Date: Invalid day. It must be between 1 and 31.")

    @year.setter
    def year(self, year: int):
        if 2026 <= year <= 2030:
            if self.__month == 2 and self.__day == 29 and not self.__is_leap_year(year):
                raise ValueError("Date: Invalid year. February 29 does not exist in that year.")
            self.__year = year
        else:
            raise ValueError("Date: Invalid year. It must be between 2026 and 2030.")

    # To String
    def __str__(self) -> str:
        return f"{self.__month:02d} {self.__day:02d}, {self.__year}"

    # Operator overload
    def __eq__(self, date: Date) -> bool:
        return self.__to_int() == date.__to_int()

    def __ne__(self, date: Date) -> bool:
        return not (self == date)

    def __lt__(self, date: Date) -> bool:
        return self.__to_int() < date.__to_int()

    def __le__(self, date: Date) -> bool:
        return self.__to_int() <= date.__to_int()

    def __gt__(self, date: Date) -> bool:
        return not (self <= date)

    def __ge__(self, date: Date) -> bool:
        return not (self < date)

    # Serialization
    def to_csv(self) -> str:
        return f"{self.__month},{self.__day},{self.__year}"

    @classmethod
    def from_csv(cls, csv_line: str) -> Date:
        parts = csv_line.strip().split(",")

        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        return cls(month, day, year)
