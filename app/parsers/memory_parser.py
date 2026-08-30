import re


def parse_memory(memory_output: str) -> dict:
    """
    Parse output of:
        free -h

    Returns:
    {
        "total_gb": 31.0,
        "used_gb": 4.7,
        "free_gb": 19.0,
        "cache_gb": 7.8,
        "available_gb": 26.0
    }
    """

    lines = memory_output.strip().splitlines()

    if len(lines) < 2:
        return {}

    values = re.split(r"\s+", lines[1])

    return {
        "total_gb": _convert_to_gb(values[1]),
        "used_gb": _convert_to_gb(values[2]),
        "free_gb": _convert_to_gb(values[3]),
        "cache_gb": _convert_to_gb(values[5]),
        "available_gb": _convert_to_gb(values[6]),
    }


def _convert_to_gb(value: str) -> float:

    value = value.strip()

    if value.endswith("Gi"):
        return float(value[:-2])

    if value.endswith("Mi"):
        return round(float(value[:-2]) / 1024, 2)

    if value.endswith("Ki"):
        return round(float(value[:-2]) / (1024 * 1024), 4)

    return float(value)
