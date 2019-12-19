# -*- coding: utf-8 -*-
from configparser import ConfigParser
import os


def make_dir(path):
    """
    Makes directory based on path.
    :param path:
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)


def get_pars_from_ini(filename='../config/config.ini'):
    """
    Returns dictionary with data loaded from configuration file.
    :param filename: .ini file name
    :type filename: str
    :return:
    """
    parser = ConfigParser()
    parser.read(filename)

    dt_pars = {}

    zones = parser.sections()

    for zone in zones:
        db = {}
        params = parser.items(zone)

        for param in params:
            try:
                db[param[0]] = eval(param[1])

            except ValueError:
                db[param[0]] = param[1].strip()

            except NameError:
                db[param[0]] = param[1].strip()

            except SyntaxError:
                db[param[0]] = param[1].strip()

        dt_pars[zone] = db

    return dt_pars


if __name__ == '__main__':
    pass
