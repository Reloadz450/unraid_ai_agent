import yaml, asyncio
from checks.docker_health import DockerHealthCheck

async def main(config_path):
    cfg = yaml.safe_load(open(config_path))
    checks = []
    if cfg["checks"]["docker_health"]:
        checks.append(DockerHealthCheck(cfg))
    while True:
        for chk in checks:
            await chk.run()
        await asyncio.sleep(300)

if __name__=="__main__":
    import sys
    cfg = sys.argv[sys.argv.index("--config")+1]
    asyncio.run(main(cfg))
