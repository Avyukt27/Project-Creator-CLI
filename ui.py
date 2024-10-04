"""UI for Project Creator"""

import subprocess


def run_command(args):
    """Runs a command

    Args:
        args (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout


run_command("create")
