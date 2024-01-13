from string import ascii_lowercase

def valid_slug(slug):
    return {*slug} <= {*ascii_lowercase, '-'}

