# -*- coding: utf-8 -*-

"""Console script for python_greek_names."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for python_greek_names."""
    click.echo("Replace this message by putting your code into "
               "python_greek_names.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
