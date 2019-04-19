
from behave import when, then, given


@given('У меня есть навык web, 3d, gamedev в профиле')
def param_get(context, random):
    pass


@given('В проекте web, 3d, gamedev указан в обязательных навыках')
def param_get_have(context, xx, yy, zz):
    pass


@given('В проекте включен Soft block')
def param_get_havent(context, x, y):
    pass


@when('Я отправляю заявку на выполнение проекта')
def param_get_semihave(context, x, y):
    pass


@then('% соответствия навыков = 100')
def param_get_crucial(context, x, y, z):
    pass


@then('Моя заявка отправлена')
def offer_sending(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page


@then('Попадает в приоритетную часть списка')
def offer_try_again(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page

#####


@given('У меня нет навыка web в профиле, но есть 3d, gamedev')
def offer_try(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@given('В проекте web, 3d, gamedev указан в обязательных навыках') ###повторяется
def offer(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@given('В проекте включен Soft block')
def post_job(context):
    pass


@when('Я пытаюсь отправить заявку на выполнение проекта')
def priority_post_job(context):
    pass


@then('% соответствия навыков = 66,6%')
def low_post_job(context):
    pass


@then('Моя заявка отправлена') #повторяется
def no_post_job(context):
    pass

@then('И попадает не в приоритетную часть списка')
def no_post_job(context):
    pass

####

@given('У меня есть навык web, 3d, gamedev в профиле') ##повторяется
def offer_try(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page

@given('В проекте web, 3d, gamedev указан в обязательных навыках') ##повторяется
def offer(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page


@given('В проекте включен Hard block') #повторяется
def post_job(context):
    pass

@when('Я отправляю заявку на выполнение проекта') #повторяется
def priority_post_job(context):
    pass

@then('% соответствия навыков = 100') #повторяется
def priority_post_job(context):
    pass


@then('Моя заявка отправлена') #повторяется
def low_post_job(context):
    pass

########

@given('У меня нет навыка web в профиле, но есть 3d, gamedev') ##повторяется
def offer_try(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page

@given('В проекте web, 3d, gamedev указан в обязательных навыках') ##повторяется
def offer(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page


@given('В проекте включен Hard block') #повторяется
def post_job(context):
    pass

@when('Я отправляю заявку на выполнение проекта') #повторяется
def priority_post_job(context):
    pass

@then('% совпадения навыков != 100')
def priority_post_job(context):
    pass


@then('Моя заявка не отправляется с сообщением "У вас не хватает навыков для этого проекта"')
def low_post_job(context):
    pass
