from app.parsers.disk_parser import parse_disk


sample = """
Filesystem      Size  Used Avail Use% Mounted on
overlay         437G  120G  294G  29% /
"""

disk = parse_disk(sample)

print("\n" + "=" * 60)
print("                 Disk Parser")
print("=" * 60)

print(f"Filesystem : {disk['filesystem']}")
print(f"Mount      : {disk['mount']}")
print(f"Size       : {disk['size_gb']} GB")
print(f"Used       : {disk['used_gb']} GB")
print(f"Available  : {disk['available_gb']} GB")
print(f"Usage      : {disk['usage_percent']} %")

print("=" * 60)
