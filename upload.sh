#!/bin/bash

git add .
git commit -a -m "new deploy"
git push -f heroku master
