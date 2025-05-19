from docker import DockerClient
from utils import send_telegram

class DockerHealthCheck:
    def __init__(self, cfg):
        self.cfg = cfg
        self.client = DockerClient()
        self.prev = {}

    async def run(self):
        for c in self.client.containers.list(all=True):
            s = c.status
            if c.name in self.prev and self.prev[c.name] != s:
                msg = f"[{self.cfg['identifier']}] {c.name}: {self.prev[c.name]}→{s}"
                send_telegram(self.cfg["telegram"], msg)
            self.prev[c.name] = s
