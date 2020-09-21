# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect product-sync.
# Copyright (c) 2019-2020 Ingram Micro. All Rights Reserved.

try:
    import warnings
    from marshmallow.warnings import ChangedInMarshmallow3Warning
    warnings.filterwarnings('ignore', category=ChangedInMarshmallow3Warning)
except ImportError:
    pass

import os

import click

from cnctcli import get_version
from cnctcli.commands.account import grp_account
from cnctcli.commands.product import grp_product
from cnctcli.config import pass_config

CCLI_VERSION = get_version()


@click.group()
@click.version_option(version=CCLI_VERSION)
@click.option('-c', '--config-dir',
              default=os.path.join(os.path.expanduser('~'), '.ccli'),
              type=click.Path(file_okay=False),
              help='set the config directory')
@pass_config
def cli(config, config_dir):
    """CloudBlue Connect Command Line Interface"""
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    config.load(config_dir)


cli.add_command(grp_account)
cli.add_command(grp_product)


def main():  # noqa
    print('')
    try:
        cli(prog_name='ccli', standalone_mode=False)  # pylint: disable=unexpected-keyword-arg,no-value-for-parameter
    except click.ClickException as ce:
        click.echo(
            click.style(f'Error: {ce.message}', fg='red')
        )
    print('')


if __name__ == '__main__':
    main()
