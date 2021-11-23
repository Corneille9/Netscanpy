"""Fichier d'installation du programme"""
from cx_Freeze import setup, Executable

base = "Win32GUI"

target = Executable(
    script="Netscanpy.py",
    icon="Code.ico",
    base=base,
)

setup(
    name="Netscanpy",
    version="1.0",
    author="Corneille",
    description="Ce programme vous permet de scanner tous les addresse ip sur un réseaux",
    executables=[target]
)