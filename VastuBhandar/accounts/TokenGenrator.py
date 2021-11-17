"""
    creating email verification token , and validating
"""

import datetime
import jwt


def token_create(user):
    """creating email verification token
        :param user
        :return token
    """
    payload = {
        'email': user.email,
        'id': str(user.id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
    }
    token = jwt.encode(payload, 'vandematram', algorithm="HS256")
    return token


def token_validator(token):
    """validating Token
    :param token
    :return payload
    """
    try:
        payload = jwt.decode(token, 'vandematram', algorithm="HS256")
        return payload
    except:
        return None
