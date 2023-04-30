# This is a sample Python script.
import argparse
import datetime
import logging


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main(date):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {date}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help='YYYYMMDD')

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(args)

    if args.date is None:
        # today
        tz = datetime.timezone(datetime.timedelta(hours=9))
        dt = datetime.datetime.now(tz=tz)  # - datetime.timedelta(days=1)
    else:
        dt = datetime.datetime.strptime(args.date, '%Y%m%d')

    logging.info(dt)

    week = dt.weekday()
    if week >= 5:
        logging.error('weekend')
    else:
        logging.error('OK')
        main(dt.date())
