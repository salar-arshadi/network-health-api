from app.collectors.linux_collector import LinuxCollector


def print_report(data):

    print("\n" + "=" * 60)
    print("              DataCenter Monitoring")
    print("=" * 60)

    print(f"\nHostname : {data['hostname']}")
    print(f"Uptime   : {data['uptime']}")

    print("\nMemory")
    print("-" * 60)

    memory = data["memory"]

    print(f"Total       : {memory['total_gb']} GB")
    print(f"Used        : {memory['used_gb']} GB")
    print(f"Free        : {memory['free_gb']} GB")
    print(f"Available   : {memory['available_gb']} GB")
    print(f"Cache       : {memory['cache_gb']} GB")

    print("\nDisk")
    print("-" * 60)

    disk = data["disk"]

    print(f"Filesystem : {disk['filesystem']}")
    print(f"Mount      : {disk['mount']}")
    print(f"Size       : {disk['size_gb']} GB")
    print(f"Used       : {disk['used_gb']} GB")
    print(f"Available  : {disk['available_gb']} GB")
    print(f"Usage      : {disk['usage_percent']} %")

    print("\n" + "=" * 60)


collector = LinuxCollector(
    host="test-linux-server",
    username="monitor",
    password="monitor123",
)

result = collector.collect()

print_report(result)
