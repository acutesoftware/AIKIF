#!/usr/bin/python3
# coding: utf-8
# handles the about page for AIKIF web interface


def get_page(dataFile=''):
    txt = ''
    txt += "This is an example framework to capture the flow of information initially "
    txt += "for personal data management, but ultimately useful for AI applications.<BR>"
    txt += dataFile + "<BR>"
    return txt
