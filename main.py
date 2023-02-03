import datetime
import time

from info_parser import get_data, get_results

RETRY_TIME = 300


def main():
    now = datetime.datetime.now()
    number_of_iterations = 0
    while number_of_iterations < 13:
        get_data()
        number_of_iterations += 1
        print("Скрипт ушёл на отдых")
        (print(number_of_iterations))
        time.sleep(RETRY_TIME)
    get_results(now)


if __name__ == "__main__":
    main()
