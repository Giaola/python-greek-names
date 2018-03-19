# Python Greek Names

[![PyPI version](https://badge.fury.io/py/python-greek-names.svg)](https://badge.fury.io/py/python-greek-names)


Python Boilerplate contains all the boilerplate you need to create a Python package.

* Free software: MIT license

### Installation

You can install via pypi

```
    pip install python-greek-names
```

### Usage

Create a mapper instance and use it across your code.

Mapper have the rules needed to transform the name to
the desired case and the exception to the rule.


```
    from python_greek_names.utils import GenitiveMapper
    gm = GenitiveMapper()
    gm.as_case('Αγάπιος')
```

Convert to upper case or strip accent by setting the mapper params.

```
    gm = GenitiveMapper(upper=True)
    gm = GenitiveMapper(accent=False)
```

Or provide your own exception list for names that I may have omitted ::


```
    gm = GenitiveMapper(extra_exceptions={
        'Ανακρέων': 'Ανακρέοντα'
    })

```

This package provides 2 mapper classes GenitiveMapper & VocativeMapper but feel free to implement your own mapper class
by subclassing the base Mapper class and providing your endings and exceptions.

```
    class SomeRandomMapper(Mapper):

        _ending_mappings = {
            'boo': 'foo',
            'ool': 'ewl'
        }

        _exceptions = {
            'cool': 'kewl'
        }

```

### Credits
-------

Marsel Tzatzo for Giaola


