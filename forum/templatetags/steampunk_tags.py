from django import template

register = template.Library()

@register.filter
def steampunk_rank(user):
    post_count = user.post_set.count()
    if post_count > 100:
        return "Главный Инженер Воздушного Флота"
    elif post_count > 50:
        return "Часовщик-Испытатель"
    elif post_count > 10:
        return "Авиатор-Вольнослушатель"
    return "Подмастерье у котла"