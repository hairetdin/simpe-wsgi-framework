#!/usr/bin/env python
# -*- coding: utf-8 -*-

from template import read_tempate


def index(environ):
    """
    Index page
    """
    html = read_tempate('templates/index.html')

    type_response = "response_ok"
    response = (type_response, html)
    return response

def page_2(environ):
    """
    Page 2
    """
    html = read_tempate('templates/page.html')
    type_response = "response_ok"
    response = (type_response, html)
    return response

def city_rm(environ):
    """
    Redirect page
    """
    #do something
    #then redirect
    type_response = "redirect"
    redirect_url = '/page-2/'
    response = (type_response, redirect_url)
    return response


def not_found():
    """
    Not found page 404
    """
    response = ["<h1>404 Page not found</h1>"]
    return response
