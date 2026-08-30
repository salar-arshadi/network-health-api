from app.parsers.memory_parser import parse_memory

sample = """
               total        used        free      shared  buff/cache   available
Mem:            31Gi       4.7Gi        19Gi       752Mi       7.8Gi        26Gi
Swap:          8.0Gi          0B       8.0Gi
"""

print(parse_memory(sample))
