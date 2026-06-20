import schedule
import time
from datetime import datetime
from django.core.management.base import BaseCommand
from forum.models import Post



def generate_report():

    posts_count = Post.objects.count()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message = f"[{current_time}] ТЕЛЕГРАФНЫЙ ОТЧЕТ: Давление в норме. Всего посланий в архиве: {posts_count}"


    print(message)


    with open("boiler_room.log", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")



class Command(BaseCommand):
    help = 'Запуск часового механизма (schedule) для отчетов форума'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Часовой механизм запущен. Ожидание назначенного времени...'))


        schedule.every().month.on(18).at("12:00").do(generate_report)


        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('\nМеханизм остановлен инженером.'))