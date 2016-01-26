#!/usr/bin/python3
# -*- coding: utf-8 -*-
# interface_windows_tools.py
# collection of toolbox functions to send keys to windows apps
# and capture results / screengrabs

import os
import sys

try:
    import win32gui
except:
    print('Cant import win32gui (probably CI build on linux)')

try:
    import win32con
except:
    print('Cant import win32gui (probably CI build on linux)')

try:
    import win32api
except:
    print('Cant import win32gui (probably CI build on linux)')

try:
    import win32com.client
except:
    print('Cant import win32gui (probably CI build on linux)')

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print(root_folder)

def get_window_by_caption(caption):
    """
    finds the window by caption and returns handle (int)
    """
    try:
        hwnd = win32gui.FindWindow(None, caption)
        return hwnd
    except ex as Exception:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1
    
def send_text(hwnd, txt):
    """
    sends the text 'txt' to the window handle hwnd using SendMessage
    """
    try:
        for c in txt:
            if c == '\n':
                win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
            else:
                win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)            
    except ex as Exception:
        print('error calling SendMessage ' + str(ex))
                
def launch_app(app_path, params):
    """
    start an app
    """
    pass
    
def app_activate(caption):
    """
    use shell to bring the application with caption to front
    """
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate(caption)
    except ex as Exception:
        print('error calling win32com.client.Dispatch (AppActivate)')
        
def close_app(caption):
    """
    close an app
    """
    pass
              
def send_keys(key_string):
    """
    sends the text or keys to the active application using shell
    Note, that the imp module shows deprecation warning.
    Examples:
        shell.SendKeys("^a") # CTRL+A 
        shell.SendKeys("{DELETE}") # Delete key
        shell.SendKeys("hello this is a lot of text with a //") 
    """
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(key_string)
    except ex as Exception:
        print('error calling win32com.client.Dispatch (SendKeys)')

