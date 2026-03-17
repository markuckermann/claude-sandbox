#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Create a Claude sandbox")
    parser.add_argument("name", help="Sandbox name")
    parser.add_argument("workspace_path", help="Workspace path to mount")
    parser.add_argument("extra_path", nargs="?", help="Optional extra path to mount")
    parser.add_argument("--ro", action="store_true", help="Mount extra_path as read-only")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    workspace_path = os.path.realpath(args.workspace_path)

    if args.extra_path:
        extra_path = os.path.realpath(args.extra_path)
        mount = f"{extra_path}:ro" if args.ro else extra_path
        ro_label = " (read-only)" if args.ro else ""
        print(f"Creating sandbox '{args.name}' with workspace '{workspace_path}' and extra path '{extra_path}'{ro_label}")
    else:
        extra_path = None
        mount = None
        print(f"Creating sandbox '{args.name}' with workspace '{workspace_path}'")

    print(f"Running from {script_dir}")
    os.chdir(script_dir)

    subprocess.run(["./build_docker.sh"], check=True)

    os.makedirs(args.workspace_path, exist_ok=True)

    cmd = ["docker", "sandbox", "create", "-t", "claude-sandbox-image", "-D",
           "--name", args.name, "claude", workspace_path]
    if mount:
        cmd.append(mount)
    subprocess.run(cmd, check=True)

    subprocess.run(
        ["docker", "sandbox", "exec", args.name, "bash", "/usr/local/bin/post_create.sh"],
        check=True,
    )

    print()
    print("Now run")
    print(f"docker sandbox exec -it {args.name} bash")
    print("or")
    print(f"docker sandbox run {args.name}")
    print()


if __name__ == "__main__":
    main()
