import yaml
import asyncio
import logging
import sys
from checks.docker_health import DockerHealthCheck

# Configure logging
cfg = None

def setup_logging(log_path):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler(sys.stdout)
        ]
    )

async def main(config_path):
    global cfg
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    # Initialize logging
    setup_logging(cfg['logging']['path'])
    logging.info("Starting Unraid AI Agent...")
    logging.info(f"Config loaded for node: {cfg['identifier']}")

    # Initialize checks based on cfg
    checks = []
    if cfg['checks'].get('docker_health'):
        checks.append(DockerHealthCheck(cfg))
    # ... add more checks

    # Async loop for running checks
    while True:
        for check in checks:
            try:
                await check.run()
            except Exception as e:
                logging.error(f"Error running {check.__class__.__name__}: {e}")
        await asyncio.sleep(300)

if __name__ == '__main__':
    try:
        cfg_index = sys.argv.index('--config') + 1
        cfg_file = sys.argv[cfg_index]
    except (ValueError, IndexError):
        print("Usage: agent.py --config <path>")
        sys.exit(1)
    asyncio.run(main(cfg_file))
