#!/usr/bin/env python3
"""module that creates a Flask app"""
from flask import Flask, render_template
from typing import Any
app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """
    Renders the index.html template

    Returns:
        index.html template
    """
    return render_template('0-index.html')
