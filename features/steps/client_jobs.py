
from behave import when, then, given


# @given('an order parameters')
# def param_get(context):
#     pass
#
# @when('we create a new job advertisement with name {thename}')
# def create_job(context, thename):
#     context.page = context.client.get('/client_jobs/post', follow_redirects=True) #сделаете апишку плез
#     assert context.page
#
#
# @then('service will add it to list of job offers')
# def post_job(context):
#     pass


# делаем на паре:

# у нас нет таблицы со списком работ клиента

@given('I have a set of jobs')
def step_impl(context):
    for row in context.table:
        try:
            Job.get(Job.name == row['job_title'])
        except Job.DoesNotExist:
            Job.create(job_title=row['job_title'],
                           job_description=row['job_description'],
                           job_price=row['job_price'],
                           job_pay_type=row['job_pay_type'],
                           job_category=row['job_category'],
                           req_skills=row['req_skills'],
                       job_deadline=row['job_deadline'])


@when('I create job advertisement')
def step_imp(context):
    pass

@then('The set of active jobs for my account includes')
def step_impl(context, name):
    try:
        context.result = Job.select().where(Job.name == name)
    except Job.DoesNotExist:
        context.result = None
    assert context.result is not None