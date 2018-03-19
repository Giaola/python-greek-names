#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_greek_names` package."""
from __future__ import unicode_literals

from python_text_utils.generic import Generic
from python_greek_names.utils import (
    normalize_name,
    VocativeMapper,
    GenitiveMapper
)


def test_normalize():
    assert normalize_name('ΜΑΡΣΕΛ') == Generic.to_unicode('Μαρσελ')
    assert normalize_name('Μαρσέλ') == Generic.to_unicode('Μαρσέλ')
    assert normalize_name('ΜΑΡΣΈΛ') == Generic.to_unicode('Μαρσέλ')
    assert normalize_name('Μαρσελ', upper=True) == Generic.to_unicode('ΜΑΡΣΕΛ')
    assert normalize_name('Μαρσέλ', upper=True) == Generic.to_unicode('ΜΑΡΣΈΛ')


def test_vocative_mapper():
    vm = VocativeMapper()

    # Testing basic usage
    assert vm.as_case('Marsel') == Generic.to_unicode('Marsel')
    assert vm.as_case('Μαρσέλ') == Generic.to_unicode('Μαρσέλ')

    # Upper
    vm_upper = VocativeMapper(upper=True)
    assert vm_upper.as_case('Μαρσέλ') == Generic.to_unicode('ΜΑΡΣΈΛ')

    # Unaccented
    vm_accent = VocativeMapper(accent=False)
    assert vm_accent.as_case('Μαρσέλ') == Generic.to_unicode('Μαρσελ')

    # Testing vocative transformations
    # Exceptions
    assert vm.as_case('παύλος') == Generic.to_unicode('Παύλο')

    # Testing endings
    assert vm.as_case('Αγάπιος') == Generic.to_unicode('Αγάπιε')
    assert vm.as_case('Χαράλαμπος') == Generic.to_unicode('Χαράλαμπε')
    assert vm.as_case('Πάτροκλος') == Generic.to_unicode('Πάτροκλε')
    assert vm.as_case('Αγισίλαος') == Generic.to_unicode('Αγισίλαε')
    assert vm.as_case('Αντίγονος') == Generic.to_unicode('Αντίγονε')
    assert vm.as_case('Γιάννης') == Generic.to_unicode('Γιάννη')

    # Testing extra exceptions
    # Test error input
    try:
        VocativeMapper(extra_exceptions=123)
    except Exception as ex:
        assert isinstance(ex, AssertionError)

    vm_exc = VocativeMapper(extra_exceptions={
        'Ανακρέων': 'Ανακρέων'
    })
    assert vm_exc.as_case('Ανακρέων') == Generic.to_unicode('Ανακρέων')

    vm_exc_upper_accent = VocativeMapper(extra_exceptions={
        'Ανακρέων': 'Ανακρέων'
    }, upper=True, accent=False)
    assert vm_exc_upper_accent.as_case('Ανακρέων') == Generic.to_unicode('ΑΝΑΚΡΕΩΝ')


def test_genitive_mapper():
    gm = GenitiveMapper()

    # Testing basic usage
    assert gm.as_case('Marsel') == Generic.to_unicode('Marsel')
    assert gm.as_case('Μαρσέλ') == Generic.to_unicode('Μαρσέλ')

    # Upper
    gm_upper = GenitiveMapper(upper=True)
    assert gm_upper.as_case('Μαρσέλ') == Generic.to_unicode('ΜΑΡΣΈΛ')

    # Unaccented
    gm_accent = GenitiveMapper(accent=False)
    assert gm_accent.as_case('Μαρσέλ') == Generic.to_unicode('Μαρσελ')

    # Testing vocative transformations
    # Exceptions
    assert gm.as_case('Φώτης') == Generic.to_unicode('Φώτη')

    # Testing endings
    assert gm.as_case('Αγάπιος') == Generic.to_unicode('Αγάπιου')
    assert gm.as_case('Χαράλαμπος') == Generic.to_unicode('Χαράλαμπου')
    assert gm.as_case('Πάτροκλος') == Generic.to_unicode('Πάτροκλου')
    assert gm.as_case('Αγισίλαος') == Generic.to_unicode('Αγισίλαου')
    assert gm.as_case('Αντίγονος') == Generic.to_unicode('Αντίγονου')
    assert gm.as_case('Μίλτος') == Generic.to_unicode('Μίλτου')
    assert gm.as_case('Νίκος') == Generic.to_unicode('Νίκου')

    # Testing extra exceptions
    # Test error input
    try:
        GenitiveMapper(extra_exceptions=123)
    except Exception as ex:
        assert isinstance(ex, AssertionError)

    gm_exc = GenitiveMapper(extra_exceptions={
        'Ανακρέων': 'Ανακρέοντα'
    })
    assert gm_exc.as_case('Ανακρέων') == Generic.to_unicode('Ανακρέοντα')

    gm_exc_upper_accent = GenitiveMapper(extra_exceptions={
        'Ανακρέων': 'Ανακρέοντα'
    }, upper=True, accent=False)
    assert gm_exc_upper_accent.as_case('Ανακρέων') == Generic.to_unicode('ΑΝΑΚΡΕΟΝΤΑ')
