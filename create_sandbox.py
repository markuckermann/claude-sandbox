#!/usr/bin/env python3
import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent


@dataclass
class MountPath:
    path: Path
    readonly: bool

    @classmethod
    def parse(cls, p: str) -> "MountPath":
        if p.endswith(":readonly") or p.endswith(":ro"):
            raw = p.rsplit(":", 1)[0]
            return cls(path=Path(raw).resolve(), readonly=True)
        return cls(path=Path(p).resolve(), readonly=False)

    def __str__(self) -> str:
        return f"{self.path}:ro" if self.readonly else str(self.path)


def create_sandbox(name: str, workspace_paths: list[str]) -> None:
    mounts = [MountPath.parse(p) for p in workspace_paths]
    print(f"Creating sandbox '{name}' with paths: {mounts}")
    print(f"Running from {REPO_DIR}")
    subprocess.run(["./build_docker.sh"], cwd=REPO_DIR, check=True)
    mounts[0].path.mkdir(parents=True, exist_ok=True)
    cmd = ["docker", "sandbox", "create", "--template", "claude-sandbox-image", "--debug",
           "--name", name, "claude"] + [str(m) for m in mounts]
    
    print(f"Running command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    print("Running post-creation setup script inside the sandbox...")
    subprocess.run(
        ["docker", "sandbox", "exec", name, "bash", "/usr/local/bin/post_create.sh"],
        check=True,
    )


def main():
    parser = argparse.ArgumentParser(description="Create a Claude sandbox")
    parser.add_argument("name", help="Sandbox name")
    parser.add_argument("workspace_paths", nargs="+", help="Paths to mount (append :ro or :readonly for read-only)")
    args = parser.parse_args()
    create_sandbox(args.name, args.workspace_paths)
    print()
    print("Now run")
    print(f"docker sandbox exec -it {args.name} bash")
    print("or")
    print(f"docker sandbox run {args.name}")
    print()


if __name__ == "__main__":
    main()
