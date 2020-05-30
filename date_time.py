from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

def main():
    date_now = date.today()
    day = timedelta(days = 1)
    month = relativedelta(months = 1)
    yesterday = date_now-day
    month_ago = date.today() - month

    return(month_ago.strftime('%d.%m.%Y') + '\n' +
        yesterday.strftime('%d.%m.%Y') + '\n' +
        date_now.strftime('%d.%m.%Y')
    )

if __name__ == '__main__':
    print(main())
