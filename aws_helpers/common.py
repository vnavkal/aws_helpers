def dangerous(func):
    def new_func(*args, **kwargs):
        ok_to_run = input(f'Are you sure you want to run {func.__name__}? (y/n) ')
        if ok_to_run == 'y':
            return func(*args, **kwargs)
    return new_func
