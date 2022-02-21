"""This file has some util functions.

    Author:
        abelbcarvalho
    """
from os.path import isfile, isdir
from pathlib import Path


def project_rootdir() -> str:
    """Returns the root directory from project folder.

    Returns:
        str: the root directory (project folder)
    """
    directory = Path(__file__).absolute().parent.__str__()
    directory = list(directory)
    directory.reverse()
    for _ in range(2):
        directory = directory[directory.index('/')+1:]
    else:
        directory.reverse()
        directory = ''.join(_ for _ in directory)
    return directory


def isitfile(pathfile: str) -> bool:
    """This function checks if a filepath is valid.

    Args:
        pathfile (str): path to file and file.

    Returns:
        bool: True if it is a file.
    """
    return True if isfile(path=pathfile) else False


def isitdir(path: str) -> bool:
    """This function checks if a path is valid.

    Args:
        path (str): path to dir.

    Returns:
        bool: True if it is a path to a existing dir.
    """
    return True if isdir(path) else False


def joinpathfile(path: str, file: str) -> str:
    """This method joins a path and a file name.

    Args:
        path (str): path to file.
        file (str): filename.

    Returns:
        str: path and file joined.
    """
    if not isitdir(path=path):
        return ''
    path = path[:-1] if path[-1] == '/' else path
    file = f'/{file}' if file[0] != '/' else file
    return f'{path}{file}'


def str_is_int(number: str) -> bool:
    """String is easy changed to Integer.

    Args:
        number (str): str to checks.

    Returns:
        bool: True if int else False.
    """
    if not number:
        return False
    for i in number:
        if not 47 < ord(i) < 58:
            return False
    else:
        return True
