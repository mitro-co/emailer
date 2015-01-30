#!/bin/sh

build/venv/bin/python docker-config.py
exec build/venv/bin/python emailer.py