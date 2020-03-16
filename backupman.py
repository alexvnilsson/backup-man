#!/usr/bin/python3

from sys import exit 
import click
from conf import profiles as Profiles

@click.group()
def cli():
  pass

@cli.group()
def profiles():
  pass

@cli.command()
@click.option("--profile", default=None, help="Profil att använda.")
def backup(profile: str = None):
  """Kör säkerhetskopiering."""

  print(f"Använd profil: {profile}")

  profile = Profiles.read_profile(profile)

  print(profile.files())

@profiles.command()
def list():
  """Visa en lista på profiler."""

  print("Lista profiler:")

  profs = Profiles.list_profiles()

  for prof in profs:
    print(prof)

@profiles.command()
@click.argument('name')
def create(name: str):
  """Skapa en ny profil."""

  prof_include = None

  try:
    prof_include = click.prompt("Ange vilka sökvägar som ska inkluderas", type=str)
  except click.Abort:
    print("Avbröt.")
    exit(1)

  Profiles.write_profile(name, [prof_include])

@profiles.command()
@click.argument('name')
@click.option("--field", default=None, help="Fältet som ska uppdateras (name, include)")
def edit(name: str, field: str):
  """Redigera ett fält i en profil."""

  if not Profiles.is_created(name):
    print(f"Profilen {name} finns inte.")
    exit(1)

  new_value = None

  if field in Profiles.CONF_FIELDS:
    print(f"Redigera profil: {name}, fält: {field}")

    if field in Profiles.CONF_FIELDS_INPUT_PROMPT:
      try:
        new_value = click.prompt("Ange vilka sökvägar som ska inkluderas", type=str)
      except click.Abort:
        print("Avbröt.")
        exit(1)

    if new_value is not None:
      print("Skriver ändringar till profilen")
      Profiles.update_profile(name, field, new_value)
    else:
      print("Skriver inga ändringar till profilen")
  else:
    print("Ange ett fält att uppdatera.")

if __name__ == '__main__':
    cli()