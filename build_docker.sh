#!/bin/bash
set -e

# Copy local Claude skills into build context
cp -r ~/.claude/skills docker/claude-skills

# Build the image
docker compose build

# Clean up copied files
rm -rf docker/claude-skills
