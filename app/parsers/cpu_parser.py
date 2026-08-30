import re


def parse_cpu(cpu_output: str):

    usage_match = re.search(r"(\d+\.\d+)\s+us", cpu_output)
    idle_match = re.search(r"(\d+\.\d+)\s+id", cpu_output)

    usage = float(usage_match.group(1)) if usage_match else 0.0
    idle = float(idle_match.group(1)) if idle_match else 0.0

    return {
        "usage_percent": usage,
        "idle_percent": idle,
    }
