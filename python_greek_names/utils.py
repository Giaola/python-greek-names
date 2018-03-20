# -*- coding: utf-8 -*-

"""Provides utility functions for working with greek names."""
from __future__ import unicode_literals

from copy import deepcopy
from six import iteritems

from python_text_utils.greek import Greek
from python_text_utils.generic import Generic


class Mapper(object):
    """
    Base class for mapping greek names to their case
    """
    _ending_mappings = {}
    _exceptions = {}

    def __init__(self, upper=False, accent=True, extra_exceptions=None):
        """

        Args:
            upper:
            accent:
            extra_exceptions:
        """
        self.upper = upper
        self.accent = accent

        assert (extra_exceptions is None or isinstance(extra_exceptions, dict))
        self.extra_exceptions = extra_exceptions
        self.__initialize()

    def __initialize(self):
        """
        Updates the exceptions with the extra exceptions given.
        """
        self.exceptions = deepcopy(self._exceptions)
        if not self.accent:
            self.exceptions = {
                Greek.strip_accent_unicode(key): Greek.strip_accent_unicode(value)
                for key, value in iteritems(self.exceptions)
            }
        if self.extra_exceptions:
            if not self.accent:
                self.extra_exceptions = {
                    Greek.strip_accent_unicode(key): Greek.strip_accent_unicode(value)
                    for key, value in iteritems(self.extra_exceptions)
                }
            self.exceptions.update(self.extra_exceptions)

    def as_case(self, name):
        """
        Args:
            name: Name to return case for
        Returns:
            str: Case of the name
        """
        # If accent is disabled remove accent from name
        if not self.accent:
            name = Greek.strip_accent_unicode(name)

        # First check if the current name is an exception to the rules
        if name in self.exceptions:
            return normalize_name(self.exceptions[name], self.upper)

        # Get the match and the collection we found the match
        for key in [name[-3:], name[-4:]]:
            if key in self._ending_mappings:
                return normalize_name(name.replace(key, self._ending_mappings[key]),
                                      self.upper)

        # Check if name ends in S, If so strip the S
        if name[-1].upper() == 'Σ':
            return normalize_name(name[:-1], self.upper)

        return normalize_name(name, self.upper)


class VocativeMapper(Mapper):
    _ending_mappings = {
        'ιος': 'ιε',
        'μπος': 'μπε',
        'λος': 'λε',
        'αος': 'αε',
        'νος': 'νε',
        'ων': 'ωνα'
    }

    _exceptions = {
        'αγαθόνικος': 'αγαθόνικε',
        'αμαρυλλίς': 'αμαρυλλίς',
        'ανακρέων': 'ανακρέοντα',
        'παύλος': 'παύλο',
        'θάνος': 'θάνο',
        'αλέξανδρος': 'αλέξανδρε',
    }


class GenitiveMapper(Mapper):

    _ending_mappings = {
        'ιος': 'ιου',
        'μπος': 'μπου',
        'κος': 'κου',
        'λος': 'λου',
        'αος': 'αου',
        'νος': 'νου',
        'τος': 'του'
    }

    _exceptions = {
        'αμαρυλλίς': 'αμαρυλλίς',
        'αλέξανδρος': 'αλέξανδρου'
    }


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
    return Generic.to_unicode(name.capitalize())
