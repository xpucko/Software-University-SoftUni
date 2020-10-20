class MustContainAtSymbolError(Exception):
    def __init__(self):
        message = 'Email must contain @'
        super(MustContainAtSymbolError, self).__init__(message)


class NameTooShortError(Exception):
    def __init__(self):
        message = 'Name must be more than 4 characters'
        super(NameTooShortError, self).__init__(message)


class InvalidDomainError(Exception):
    def __init__(self):
        message = 'Domain must be one of the following: .com, .bg, .org, .net'
        super(InvalidDomainError, self).__init__(message)


def validate_name(email):
    username = email.split('@')[0]
    if len(username) <= 4:
        raise NameTooShortError


def validate_at_symbol(email):
    if '@' not in email:
        raise MustContainAtSymbolError


def validate_domain(email):
    valid_domains = ('com', 'net', 'bg', 'org')
    domain = email.split('.')[-1]
    if domain not in valid_domains:
        raise InvalidDomainError


while True:
    current_email = input()
    if current_email == 'End':
        break

    validate_name(current_email)
    validate_at_symbol(current_email)
    validate_domain(current_email)

    print('Email is valid')
