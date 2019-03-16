
from behave import when, then, given


@given('an order parameters')
def param_get(context):
    pass

@when('we create a new job advertisement with name {thename}')
def create_job(context, thename):
    context.page = context.client.get('/client_jobs/post', follow_redirects=True) #сделаете апишку плез
    assert context.page


@then('service will add it to list of job offers')
def post_job(context):
    pass