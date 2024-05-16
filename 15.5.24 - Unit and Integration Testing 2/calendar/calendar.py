class Calendar:
    @staticmethod
    def is_leap(year):
        """Checks if a given year is a leap year."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_date():
        """Prompts the user for a valid date and returns month, day, and year."""
        while True:
            month = int(input("Enter month (1-12): "))
            day = int(input("Enter day (1-31): "))
            year = int(input("Enter year: "))

            if Calendar.is_valid_date(month, day, year):
                return month, day, year
            else:
                print("Invalid date. Please try again.")

    @staticmethod
    def is_valid_date(month, day, year):
        """Checks if a given date is valid."""
        return 1 <= month <= 12 and 1 <= day <= Calendar.last_day_of_month(month, year)

    @staticmethod
    def last_day_of_month(month, year):
        """Returns the last day of a given month based on year (considering leap years)."""
        if month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            return 28 + Calendar.is_leap(year)
        else:
            return 31

    @staticmethod
    def get_digits():
        """Gets month, day, and year from the user and validates them using get_date."""
        return Calendar.get_date()

    @staticmethod
    def memorial_day(year):
        """Calculates Memorial Day (last Monday in May) for a given year."""
        from datetime import date, timedelta
        # Create a date object on May 31st
        d = date(year, 5, 31)
        # Backtrack to the last Monday (weekday 0)
        offset = (d.weekday() - 0) % 7
        last_monday = d - timedelta(days=offset)
        return last_monday.month, last_monday.day, last_monday.year

    @staticmethod
    def is_monday(month, day, year):
        """Checks if a given date is a Monday."""
        from datetime import date
        return date(year, month, day).weekday() == 0

    @staticmethod
    def friday_13th(month, day, year):
        """Checks if a given date is Friday the 13th."""
        from datetime import date
        return day == 13 and date(year, month, day).weekday() == 4

    @staticmethod
    def get_date_body():
        """Gets valid month, day, and year from the user."""
        return Calendar.get_digits()

    @staticmethod
    def main():
        month, day, year = Calendar.get_date_body()
        print(f"Date: {month}/{day}/{year}")

        if Calendar.friday_13th(month, day, year):
            print("It's Friday the 13th!")
        if Calendar.is_monday(month, day, year):
            print("It's a Monday.")

        # Example of using memorial_day
        memorial_month, memorial_day, memorial_year = Calendar.memorial_day(year)
        print(f"Memorial Day in {year} is on: {memorial_month}/{memorial_day}/{memorial_year}")


if __name__ == "__main__":
    Calendar().main()