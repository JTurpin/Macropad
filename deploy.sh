#!/bin/bash

# Remove all old macros
rm -rf //Volumes/CIRCUITPY/macros/*

#recursively deploy all files
cp -r * /Volumes/CIRCUITPY/

# Cleanup deploy.sh
rm /Volumes/CIRCUITPY/deploy.sh