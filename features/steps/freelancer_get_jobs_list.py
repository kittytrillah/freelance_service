
from behave import when, then, given


@given('filter parameters')
def param_get(context):
    pass

@when('we open jobs list')
def open_job_list(context, thename):
    context.page = context.client.get('/client_jobs/get', follow_redirects=True) #сделаете апишку плез
    assert context.page


@then('service will show every job on it')
def show_job_list(context):
    pass