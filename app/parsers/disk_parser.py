import re


def parse_disk(disk_output: str) -> dict:
    """
    Parse output of:
        df -h /

    Returns:
    {
        "filesystem": "overlay",
        "size_gb": 437,
        "used_gb": 120,
        "available_gb": 294,
        "usage_percent": 29,
        "mount": "/"
    }
    """

    lines = disk_output.strip().splitlines()

    if len(lines) < 2:
        return {}

    values = re.split(r"\s+", lines[1])

    return {
        "filesystem": values[0],
        "size_gb": _convert_to_gb(values[1]),
        "used_gb": _convert_to_gb(values[2]),
        "available_gb": _convert_to_gb(values[3]),
        "usage_percent": int(values[4].replace("%", "")),
        "mount": values[5],
    }


def _convert_to_gb(value: str):

    value = value.strip()

    if value.endswith("G"):
        return float(value[:-1])

    if value.endswith("M"):
        return round(float(value[:-1]) / 1024, 2)

    if value.endswith("T"):
        return float(value[:-1]) * 1024

    return float(value)
