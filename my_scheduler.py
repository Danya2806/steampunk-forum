import schedule
import time
from datetime import datetime
def job():

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"Задача выполнена! Время: {current_time}"
    print(message)
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

schedule.every().month.on(18).at("12:00").do(job)
# schedule.every(30).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)