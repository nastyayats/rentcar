from tokens import get_token


def before_all(context):
    context.read_token = get_token('R')
    context.write_token = get_token('W')
