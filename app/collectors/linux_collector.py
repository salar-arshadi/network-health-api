import paramiko

from app.parsers.cpu_parser import parse_cpu
from app.parsers.memory_parser import parse_memory
from app.parsers.disk_parser import parse_disk


class LinuxCollector:

    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def collect(self):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(
            hostname=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
            timeout=10,
        )

        commands = {
            "hostname": "hostname",
            "uptime": "uptime",
            "cpu": "top -bn1 | grep 'Cpu(s)'",
            "memory": "free -h",
            "disk": "df -h /",
        }

        result = {}

        for key, command in commands.items():
            stdin, stdout, stderr = client.exec_command(command)
            result[key] = stdout.read().decode().strip()

        client.close()

        return {
            "hostname": result["hostname"],
            "uptime": result["uptime"],
            "cpu": parse_cpu(result["cpu"]),
            "memory": parse_memory(result["memory"]),
            "disk": parse_disk(result["disk"]),
        }
