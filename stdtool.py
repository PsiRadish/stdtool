"""
Kyle Fiegener https://github.com/PsiRadish
"""

import sys
import os
import re
import wx

# import win32gui
# import winspy

# import win32pipe
# import pywintypes, msvcrt
# # only works on Windows and requires pywin32
# def pipe_empty(pipe):
# #{
#     fd = pipe.fileno()
#     osf = msvcrt.get_osfhandle(fd)
    
#     try:
#         data, avail, _ = win32pipe.PeekNamedPipe(osf, 0)
#     except pywintypes.error:  # Pipe closed
#         return True
        
#     return not avail
# #}


class Tool(object):
#{
    def __init__(self, name, modulefile):
    #{
        self.name = name
        self.errfile = None
        
        # if pipe_empty(sys.stdin): # No data in stdin; quit
        #     sys.exit(0)
        # if sys.stdin.isatty(): # stdin coming directly from terminal
        #     sys.exit(0)
        
        # standard-error redirection
        self.errfilepath = re.sub(r'''\.pyw?(?=["']?$)''', ".err.log", os.path.abspath(modulefile))
        self.errfile = open(self.errfilepath, 'w')
        sys.stderr = self.errfile
        
        self.input = sys.stdin.read()
    #}
    
    def __del__(self):
    #{
        if self.errfile:
            # sys.stderr.write("%s : called Tool.__del__" % self.name) # TEMP DEBUG
            
            # sys.stderr.write("%s : Error file path = %s" % (self.name, self.errfile.name)) # TEMP DEBUG
            
            self.errfile.close()
            
            if os.path.getsize(self.errfile.name) == 0: # if error log empty, delete it
                os.remove(self.errfile.name)
    #}
    
    @property
    def output(self):
        pass
    
    @output.setter
    def output(self, value):
        sys.stdout.write(value)
    
#}

class wxTool(Tool):
#{
    def __init__(self, name, modulefile, setparent = True, winclass = None, starts_with = True):
    #{
        self.app = None
        Tool.__init__(self, name, modulefile) # ! will call sys.exit(0) if stdin is empty
        
        self.app = wx.App() # wx.PySimpleApp()
        
        # == Find window to use as parent window for dialogs ==
        # if setparent:
        #     hwnd_to_use = None
        #   
        #     activewin = win32gui.GetForegroundWindow()
        #     print("activewin", activewin)
        #     if winclass:
        #         print("gonna try to match", winclass)
        #         if (starts_with and winspy.getclassname(activewin).startswith(winclass)) or (not starts_with and winspy.getclassname(activewin) == winclass):
        #             hwnd_to_use = activewin
        #         else:  # find the first window that meets criteria
        #             hwnd_to_use = winspy.findwindow(findclass=winclass, starts_with=starts_with)
        #     else:   # just use active window
        #         print("sticking with active window")
        #         hwnd_to_use = activewin
        #
        #     if hwnd_to_use:
        #         self.parent = wx.Window_FromHWND(None, hwnd_to_use) # parent window set ++ Apparently this function isn't implemented in Phoenix
        #
        # else:
        #     self.parent = None
        self.parent = None
    #}
    
    #def __del__(self):
    ##{  
    #    if self.app:
    #        self.app.MainLoop() # Needs to be called SOMEWHERE?
    #    
    #    Tool.__del__(self)
    ##}
#}
