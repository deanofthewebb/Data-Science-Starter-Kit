#!/bin/bash
set -e
. activate tf-gpu

if [ -z "$1" ]
  then
    jupyter notebook --no-browser --port=8889
elif [ "$1" == *".ipynb"* ]
  then
    jupyter notebook --no-browser --port=8889 "$1"
else
    exec "$@"
fi
