#!/bin/bash

if [ ! -f ~/.sandbox_post_create_done ]; then

  # This ensures that claude authenticates using oauth
  echo '{"hasCompletedOnboarding": true, "bypassPermissionsModeAccepted": true}' > ~/.claude.json
  claude upgrade
  claude plugin marketplace add anthropics/claude-plugins-official
  claude plugin install superpowers
  
  touch ~/.sandbox_post_create_done
fi
