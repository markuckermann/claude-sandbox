## GitHub Auth

- Go to **Settings → Developer settings → Personal access tokens → Fine-grained tokens**
- Set permissions to read-only for whatever scopes you need (e.g., Contents: Read, Metadata: Read)
- add to the .env


## Build the template using 
```
build_docker.sh
```
```
docker sandbox run -t claude-sandbox-image claude [PATH]
```

```
docker sandbox create -t claude-sandbox-image -D --name test claude .
docker sandbox exec -it test bash
```

## Set up sandbox
cd ~/Beeline/fw
git clone beeline-firmware-nrf beeline-firmware-nrf-sandbox

cd beeline-firmware-nrf-sandbox 
git remote rename origin upstream

docker sandbox create -t claude-sandbox-image -D --name bl-fw-nrf claude .
docker sandbox exec bl-fw-nrf bash /usr/local/bin/post_create.sh