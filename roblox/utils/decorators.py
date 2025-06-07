def make_docs(name: str, description: str):
    def decorator(func):
        setattr(func, "_IS_API", True)
        func.__doc__ = f"{name}:\n{description}"
        return func

    return decorator


def make_api_function():
    pass
