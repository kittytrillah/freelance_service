from behave import when, then, given


@given('У меня есть навык {x}, {y}, {z} в профиле')
def param_get(context, x, y, z):
    pass


@given('В проекте {xx}, {yy}, {zz} указан в обязательных навыках')
def param_get_have(context, xx, yy, zz):
    pass


@given('В проекте включен {block_type}')
def param_get_havent(context, block_type):
    pass


@when('Я отправляю заявку на выполнение проекта')
def param_get_semihave(context):
    pass


@then('% соответствия навыков = {skill_ratio}')
def param_get_crucial(context, skill_ratio):
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


@given('У меня нет навыка {xxx} в профиле, но есть {y}, {z}')
def offer_try(context, xxx, y, z):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@when('Я пытаюсь отправить заявку на выполнение проекта')
def priority_post_job(context):
    pass


# @then('% соответствия навыков = {66,6%}')
# def low_post_job(context):
#     pass
#


@then('И попадает не в приоритетную часть списка')
def no_post_job(context):
    pass



# @given('В проекте включен {Hard block}') #повторяется
# def post_job(context, x):
#     pass


@then('% совпадения навыков != {skill_ratio_non}')
def priority_post_job(context, skill_ratio_non):
    pass


@then('Моя заявка не отправляется с сообщением: {}')
def low_post_job(context, error_message):
    pass
