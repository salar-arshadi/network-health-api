from app.parsers.cpu_parser import parse_cpu


sample = "%Cpu(s):  3.5 us,  1.0 sy,  0.0 ni,95.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st"

result = parse_cpu(sample)

print(result)
