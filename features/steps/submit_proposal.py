from behave import when, then, given
from models import proposal as proposal_m
import fuzzywuzzy



@given('У меня есть навык {x} в профиле')
def param_get(context, x):
    context.ready = 0 #readiness status
    proposal_m.Proposal.StatusChange(0, 1)
    context.error_messages = []
    context.current_skills = x
    pass


@given('В проекте {xx} указан в обязательных навыках')
def param_get_have(context, xx):
    pass


@given('В проекте включен {block_type}')
def param_get_havent(context, block_type):
    if block_type == "Soft block":
        print("///Soft block")
    elif block_type == "Hard block":
        print("///Hard block")
    context.block_type = block_type


@when('Я отправляю заявку на выполнение проекта с id = {job_hash}')
def param_get_semihave(context, job_hash):
    context.job_hash = job_hash
    context.job_demanded_score = proposal_m.Proposal.get_proposal_score(context.job_hash)
    context.current_ratio = proposal_m.Proposal.proposal_score(context.job_hash, context.current_skills)
    #context.proposal_score = proposal_m.Proposal.proposal_score(context.current_skills, context.job_demanded_score)
    pass


@then('% соответствия навыков = {skill_ratio}')
def param_get_crucial(context, skill_ratio):
    if context.block_type == "Hard block":
        if context.current_ratio >= 95:
            context.ready = 1
            print("///Hard block accepted///")
        else:
            context.error_messages.append("skills not matching")
            proposal_m.Proposal.ShowError()
        print("///Hard block chosen///")
    elif context.block_type == "Soft block":
        if context.current_ratio >= context.job_demanded_score:
            context.ready = 1
            print("///Soft block accepted///")
        else:
            context.error_messages.append("skills not matching")
            proposal_m.Proposal.ShowError()


@then('Моя заявка отправлена')
def offer_sending(context):
    proposal_m.STATUSES = 2
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page


@then('Попадает в приоритетную часть списка')
def offer_try_again(context):
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page



@given('У меня нет навыка {xxx} в профиле, но есть {z}')
def offer_try(context, xxx, z):
    context.current_skills = z
    context.ready = 0  # readiness status
    proposal_m.STATUSES = 1
    context.error_messages = []
    context.page = context.client.get('/proposals/post', follow_redirects=True)
    assert context.page




@then('И попадает не в приоритетную часть списка')
def no_post_job(context):
    pass



@then('% совпадения навыков != {skill_ratio_non}')
def priority_post_job(context, skill_ratio_non):
    pass


@then('Моя заявка не отправляется с сообщением: {}')
def low_post_job(context, error_message):
    print(error_message)
