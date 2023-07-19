import requests
import schedule


def greeting():
    todos_dict = {
        "08:00": "Drink coffee",
        "09:00": "English learn",
        "10:00": "Read books",
        "11:00": "Work meeting"
    }

    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f"{k} - {v}")


def main():

    # schedule.every(4).seconds.do(greeting)   # Работа скрипта каждые 4 секунды
    # schedule.every(5).minutes.do(greeting)   # Работа скрипта каждые 5  минут
    # schedule.every().hour.do(greeting)       # Работа скрипта каждый час

    schedule.every().day.at("14:44").do(greeting)   # Работа скрипта в указанное время
    # schedule.every().monday.do(greeting)   # Работа скрипта каждые в указанный день
    # schedule.every().monday.at("15:00").do(greeting)   # Работа скрипта в указанный день и заданное время

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()