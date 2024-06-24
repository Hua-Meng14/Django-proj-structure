if IN_DOCKER:  # noqa F821
    # print('Running in Docker mode....')
    assert MIDDLEWARE[:1] == ['django.middleware.security.SecurityMiddleware']  # noqa F821
