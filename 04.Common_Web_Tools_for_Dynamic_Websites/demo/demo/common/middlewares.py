def do_nothing_middleware(get_response, *args, **kwargs):
    response = get_response(*args, **kwargs)

    return response