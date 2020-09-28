def age_assignment(*args, **kwargs):
    return {arg: kwargs[arg[0]] for arg in args}
