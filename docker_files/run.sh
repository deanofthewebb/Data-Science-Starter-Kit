#!/bin/bash
set -e
. activate tf-gpu

if [ -z "$1" ]
  then
    jupyter notebook --no-browser --port=8888 --allow-root
elif [ "$1" == *".ipynb"* ]
  then
    jupyter notebook --no-browser --port=8888 --allow-root "$1"
else
    exec "$@"
fi
