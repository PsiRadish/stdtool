"""
Kyle Fiegener https://github.com/PsiRadish
"""

import sys
import os
import re
import wx

class Tool(object):
#{
    def __init__(self, name, modulefile):
    #{
        self.name = name
        self.errfile = None
        
        # standard-error redirection
        self.errfilepath = re.sub(r'''\.pyw?(?=["']?$)''', ".err.log", os.path.abspath(modulefile))
        self.errfile = open(self.errfilepath, 'w')
        sys.stderr = self.errfile
        # TODO?: Redirect stderror to a stream in memory and check if its empty in __del__ before copying contents to file?
        
        self.input = sys.stdin.read()
    #}
    
    def __del__(self):
    #{
        if self.errfile:
            self.errfile.close()
            
            if os.path.getsize(self.errfile.name) == 0: # if error log empty, delete it
                os.remove(self.errfile.name)
    #}
    
    def output(self, stuff):
        sys.stdout.write(stuff)
    
#}

class wxTool(Tool):
#{
    def __init__(self, name, modulefile, setparent = True, winclass = None, starts_with = True):
    #{
        self.app = None
        Tool.__init__(self, name, modulefile)
        
        self.app = wx.App()
        
        self.parent = None
    #}
#}
