from albert import *
from os import path

__title__ = "Git clone"
__version__ = "0.4.0"
__triggers__ = "clone "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

def handleQuery(query):
    if not query.isTriggered or not query.isValid or not query.string:
        return

    items = []
        
    dir = query.string.strip().split('/',1)[1].split('.git')[0] 

    items.append(Item(
        id='clone',
        icon=icon,
        text='git clone ' + query.string,
        actions=[
            TermAction(
                text='git clone', 
                script='git clone {} && code {}'.format(query.string, dir), 
                cwd='/home/y/code'
            ),
        ],
    ))

    return items
