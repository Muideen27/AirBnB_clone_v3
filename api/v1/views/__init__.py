#!/usr/bin/python3
"""
module that uses blueprint to generate app view
"""

from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1/')
