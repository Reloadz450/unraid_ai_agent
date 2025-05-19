#!/usr/bin/env bash
# Log entrypoint startup
mkdir -p /mnt/cache/scripts/logs
LOGFILE="/mnt/cache/scripts/logs/agent.log"
echo "[ENTRYPOINT] $(date): entrypoint.sh started" >> "$LOGFILE"

# Attempt to find Python
if [ -x "/mnt/cache/scripts/venv/bin/python3" ]; then
  PYTHON="/mnt/cache/scripts/venv/bin/python3"
elif command -v python3 &>/dev/null; then
  PYTHON=$(command -v python3)
else
  echo "Python3 not found, falling back to bash checks." >> "$LOGFILE"
  exec bash /app/checks/zfs_health.sh
fi

# Run the main agent and log output
exec "$PYTHON" /app/agent.py --config /app/config.sample.yaml
