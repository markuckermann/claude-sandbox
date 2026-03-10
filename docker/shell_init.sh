#!/bin/bash

if [ ! -f ~/.sandbox_init_done ]; then

  # This ensures that claude authenticates using oauth
  echo '{"hasCompletedOnboarding": true, "bypassPermissionsModeAccepted": true}' > ~/.claude.json
  
  claude plugin marketplace add anthropics/claude-plugins-official
  claude plugin install superpowers
  
  touch ~/.sandbox_init_done
fi
