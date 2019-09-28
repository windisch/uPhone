#!/bin/bash

# Helper script that places code on microcontroller

echo "Copy base dir"
rsync -av \
   --exclude=.git \
   --exclude=uphone \
   --exclude=uphone.egg-info \
   --exclude=__pycache__ \
   .. \
   /Volumes/PYBFLASH

echo "Copy code dir"
rsync -av --delete ./uphone /Volumes/PYBFLASH/
