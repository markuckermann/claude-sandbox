#!/bin/bash

set -e
if [ $# -ne 2 ]; then
    echo "Usage: $0 <name> <workspace_path>"
    exit 1
fi

./build_docker.sh

mkdir -p "$2"
docker sandbox create -t claude-dev-sandbox -D --name "$1" claude "$2"
docker sandbox exec "$1" bash /usr/local/bin/shell_init.sh

echo ""
echo "Now run"
echo "docker sandbox exec -it $1 bash"
echo "or"
echo "docker sandbox run $1"