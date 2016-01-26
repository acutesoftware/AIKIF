#!/usr/bin/python3
# -*- coding: utf-8 -*-
# interface_windows_tools.py
# collection of toolbox functions to send keys to windows apps
# and capture results / screengrabs

import os
import sys
import win32gui
import win32con
import win32api
import win32com.client

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print(root_folder)

def get_window_by_caption(caption):
    """
    finds the window by caption and returns handle (int)
    """
    hwnd = win32gui.FindWindow(None, caption)
    return hwnd
    
def send_text(hwnd, txt):
    """
    sends the text 'txt' to the window handle hwnd using SendMessage
    """
    for c in txt:
        if c == '\n':
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)            

def launch_app(app_path, params):
    """
    start an app
    """
    pass
    
def app_activate(caption):
    """
    use shell to bring the application with caption to front
    """
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate(caption)
   
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
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys(key_string)

