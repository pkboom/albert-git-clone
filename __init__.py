from albert import *
from os import path

__title__ = "Git clone"
__version__ = "0.4.0"
__triggers__ = "clone "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

def handleQuery(query):
    items = []

    if not query.isTriggered or not query.isValid:
        return

    items.append(Item(
        id='clone',
        icon=icon,
        text='git clone ' + query.string,
        actions=[
            TermAction(text='git clone', 
                commandline=['git', 'clone',  query.string], 
                cwd='~/code')
        ],
    ))

    return items
