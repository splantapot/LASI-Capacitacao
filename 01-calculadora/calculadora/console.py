import subprocess, os

def cls():
    """Limpar o console."""
    subprocess.run("cls", shell=True)
    # Para linux:
    # subprocess.run("clear", shell=True)

def prRed(s): print("\033[91m {}\033[00m".format(s))
def prGreen(s): print("\033[92m {}\033[00m".format(s))
def prYellow(s): print("\033[93m {}\033[00m".format(s))
def prLightPurple(s): print("\033[94m {}\033[00m".format(s))
def prPurple(s): print("\033[95m {}\033[00m".format(s))
def prCyan(s): print("\033[96m {}\033[00m".format(s))
def prLightGray(s): print("\033[97m {}\033[00m".format(s))
def prBlack(s): print("\033[90m {}\033[00m".format(s))  # Corrected from 98 to 90 (standard ANSI)