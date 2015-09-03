#!/bin/bash

export SERVER_ENV="production"

gunicorn main:app --log-file=-
