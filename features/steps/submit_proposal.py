
from behave import when, then, given


@given('a job advertisement {random}')
def param_get(context, random):
    pass


@given('У меня есть навык {xx}, {yy}, {zz} в профиле')
def param_get_have(context, xx, yy, zz):
    pass


@given('У меня нет навыка web в профиле, но есть {x}, {y}')
def param_get_havent(context, x, y):
    pass


@given('У меня нет навыка web в профиле, но есть {x}, {y}')
def param_get_semihave(context, x, y):
    pass


@given('В проекте {x}, {y}, {z} указан в обязательных навыках')
def param_get_crucial(context, x, y, z):
    pass


@when('Я отправляю заявку на выполнение проекта')
def offer_sending(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page


@when('Я пытаюсь отправить заявку на выполнение проекта')
def offer_try_again(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@when('Я пытаюсь отправить заявку на выполнение этого проекта')
def offer_try(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@when('we offer our candidature')
def offer(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@then('service register a proposal')
def post_job(context):
    pass


@then('Моя заявка отправлена')
def priority_post_job(context):
    pass


@then('Моя отправляется (но не попадет в приоритетные)')
def low_post_job(context):
    pass


@then('Моя заявка не отправляется')
def no_post_job(context):
    pass