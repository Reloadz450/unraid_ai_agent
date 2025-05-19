#!/usr/bin/env bash
if [ -x "/mnt/cache/scripts/venv/bin/python3" ]; then
  PYTHON="/mnt/cache/scripts/venv/bin/python3"
elif command -v python3 &>/dev/null; then
  PYTHON=$(command -v python3)
else
  echo "Python3 not found, falling back to bash checks."
  exec bash /app/checks/zfs_health.sh
fi

exec "$PYTHON" /app/agent.py --config /app/config.sample.yaml
