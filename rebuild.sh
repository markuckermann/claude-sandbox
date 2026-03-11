docker sandbox rm test
set -e

./build_docker.sh
docker sandbox create -t claude-dev-sandbox -D --name test claude .
docker sandbox exec test bash /usr/local/bin/shell_init.sh
echo "\nNow run"
echo "docker sandbox run test"