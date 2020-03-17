#!/usr/bin/env python3

from sys import exit
from typing import List
import glob
import click
from backupman.config import paths
from backupman.config import rules as Rules


@click.group()
def cli():
    pass


@cli.group()
def conf():
    pass


@cli.group()
def rules():
    pass

from datetime import datetime
from backupman.backup import tar

@cli.command()
@click.option("--rule", default=None, help="Regler att använda.")
@click.option("--output-dir", default=None, help="Var arkivet ska sparas.")
def backup(rule: str, output_dir: str):
    """Kör säkerhetskopiering."""

    if output_dir is None:
        output_dir = str(paths.get_root())

    print(f"Använd regler: {rule} (output: {output_dir})")

    r = Rules.read(rule)

    if not 'include' in r:
        raise Exception(f"'include' finns inte i konf. {rule}")

    ri = r['include']

    files = glob.glob(ri)

    now = datetime.now()
    archive_date = now.strftime("%Y%m%d-%H%M%S")
    archive_dir = output_dir
    archive_name = f"{rule}_{archive_date}"

    tar.archive(archive_name, archive_dir, files)


@rules.command('list')
def rule_list():
    """Visa en lista på regler."""

    print("Lista regler:")

    r = Rules.list()

    for rule in r:
        print(rule)

@rules.command('print')
@click.argument('name')
def rule_print(name: str):
    try:
        r = Rules.read(name)
    except:
        print(f"Kunde inte läsa regeln {name}.")

    print(r)

@rules.command('make')
@click.argument('name')
def rule_make(name: str):
    """Skapa en ny profil."""

    r_include = None

    try:
        r_include = click.prompt(
            "Ange vilka sökvägar som ska inkluderas", type=str)
    except click.Abort:
        print("Avbröt.")
        exit(1)

    Rules.write(name, [r_include])

@rules.command('rm')
@click.argument('name')
def rule_rm(name: str):
    remove_confirmed = click.confirm(f"Vill du verkligen ta bort regeln {name}?", default=False)

    if remove_confirmed:
        print(f"Tar bort regeln {name}...")
        Rules.remove(name)

@rules.command('change')
@click.argument('name')
@click.argument('field')
def rule_change(name: str, field: str):
    """Redigera ett fält i en regel."""

    if not Rules.is_created(name):
        print(f"Regeln {name} finns inte.")
        exit(1)

    new_value = None

    if field in Rules.CONF_FIELDS:
        print(f"Redigera regel: {name}, fält: {field}")

        if field in Rules.CONF_FIELDS_INPUT_PROMPT:
            try:
                new_value = click.prompt(
                    "Ange vilka sökvägar som ska inkluderas", type=str)
            except click.Abort:
                print("Avbröt.")
                exit(1)

        if new_value is not None:
            print("Skriver ändringar till regeln")
            Rules.update(name, field, new_value)
        else:
            print("Skriver inga ändringar till regeln")
    else:
        print("Ange ett fält att uppdatera.")


@conf.command('make')
@click.option("--user", is_flag=True)
def conf_make(user: bool):
    """Skapa en konfig."""

    if user:
        print("Skapar användar-konfig...")
        paths.make_userconfig()
    else:
        print("Inte implementerat.")

if __name__ == '__main__':
    cli()
