# -*- coding: utf-8 -*-

"""Provides utility functions for working with greek names."""
from python_text_utils.greek import Greek
from python_text_utils.generic import Generic


__vocative_endings = {
    'ιος': 'ιε',
    'μπος': 'μπε',
    'λος': 'λε',
    'αος': 'αε',
    'νος': 'νε',
}

__vocative_default_exceptions = {
    'παύλος': 'παύλο',
    'θάνος': 'θάνο',
    'αλέξανδρος': 'αλέξανδρε',
    'αμαρυλλίς': 'αμαρυλλίς'
}


def as_vocative(name, upper=False, accent=True, extra_exceptions=None):
    """
    Transforms greek name to its vocative representation.

    Args:
        name(str): Nominative representation of the name.
        upper(bool): If set the name will be returned in uppercase otherwise it will be capitalized.
        accent(bool): If set to False accent will be stripped off the string.
        extra_exceptions(dict): Dictionary with extra exceptions to look for before the algorithm starts.
                                The dictionary's keys and values should both be unicode strings.

    Returns:
        str: Vocative representation of the name.
    """
    name = Generic.to_unicode(name).lower()

    if not accent:
        name = Greek.strip_accent_unicode(name)

    # First check if the current name is an exception to the rules
    if name in __vocative_default_exceptions:
        return normalize_name(__vocative_default_exceptions[name], upper)

    # Get the match and the collection we found the match
    key = [key
           for key in [name[-3], name[-4]]
           if key in __vocative_endings.keys()]

    if key:
        return normalize_name(name.replace(key, __vocative_endings[key]), upper)

    # Check if name ends in S, If so strip the S
    if name[-1].upper() == 'Σ':
        return normalize_name(name[:-1], upper)

    return name


def as_genitive(name):
    """
    Transforms greek name to its genitive representation.

    Args:
        name:

    Returns:
        str: Genitive representation of the name.

    """
    return None


def normalize_name(name, upper=False):
    """
    Normalizes case of name by setting its first letter uppercase and the rest lowercase.

    Args:
        name(str): Name to normalize

    Returns:
        str: Normalized version of the name.
    """
    name = Generic.to_unicode(name)
    if upper:
        return name.upper()
    return name.capitalize()
