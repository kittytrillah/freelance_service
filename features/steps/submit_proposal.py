
from behave import when, then, given


@given('a job advertisement #I would add here some limit skills later')
def param_get(context):
    pass

@when('we offer our candidature')
def offer(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True) #сделаете апишку плез
    assert context.page


@then('service register a proposal')
def post_job(context):
    pass