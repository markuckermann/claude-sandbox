docker sandbox rm test
set -e

./build_docker.sh
docker sandbox create -t claude-dev-sandbox -D --name test claude .
echo "\nNow run"
echo "docker sandbox exec -it test bash"