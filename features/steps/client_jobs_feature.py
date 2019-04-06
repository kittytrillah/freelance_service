from behave import when, then, given

# @given('I have a set of jobs')
# def step_impl(context):
#     # for row in context.table:
#     #     try:
#     #         Job.get(Job.name == row['job_title'])
#     #     except Job.DoesNotExist:
#     #         Job.create(job_title=row['job_title'],
#     #                        job_description=row['job_description'],
#     #                        job_price=row['job_price'],
#     #                        job_pay_type=row['job_pay_type'],
#     #                        job_category=row['job_category'],
#     #                        req_skills=row['req_skills'],
#     #                    job_deadline=row['job_deadline'])
#     pass
#
#
# @when('I create job advertisement')
# def step_imp(context):
#     pass
#
# @then('The set of active jobs for my account includes')
# def step_impl(context, name):
#     pass


#///////////////////////UNDONE//////////////////////


@given('У меня опубликован проект {x}')
def project_submitted(context, x):
    pass


@given('Категория работы {x}')
def job_category_set(context, x):
    pass


@given('Указаны необходимые навыки {x}, {y}, {z}')
def skills_set(context, x, y, z):
    pass


@given('Краткое описание заказа без распознаваемых ключевых слов')
def job_description_null(context):
    pass


@given('Краткое описание заказа с ключевыми словами {x}, {y}, {z}')
def job_description_keywords(context, x, y, z):
    pass


@when('Я открываю список заявок от фрилансеров')
def open_freelancer_list(context):
    pass


@when('приступаю к выбору навыков')
def skills_choose(context):
    pass


@then('Заявки отсортированы таким образом, что сначала показываются работники с навыками, а затем все остальные')
def proposals_filter(context):
    pass


@then('Я получаю подсказки, основанные на категории работы и ключевых словах из краткого описания заказа')
def get_help_category_description(context):
    pass


@then('Я получаю подсказки, основанные только на категории работы')
def get_help_category(context):
    pass
