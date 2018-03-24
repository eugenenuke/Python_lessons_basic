#!/bin/bash

if [[ ! $PATH =~ "/venv/" ]]; then
	echo "Activate 'venv' first"
	exit 0
fi

pip3 install requests
