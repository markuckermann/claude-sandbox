## GitHub Auth

- Go to **Settings → Developer settings → Personal access tokens → Fine-grained tokens**
- Set permissions to read-only for whatever scopes you need (e.g., Contents: Read, Metadata: Read)
- add them to the .env


## Build it using 
```
docker compose build
```
```
docker sandbox run -t claude-dev-sandbox claude [PATH]
```

```
docker sandbox create -t claude-dev-sandbox -D --name test claude .
docker sandbox exec -it test bash
```