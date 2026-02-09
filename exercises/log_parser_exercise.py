import re
from collections import Counter

LOG_TEXT = """\
2026-02-03T13:40:21Z INFO  GET  /api/itinerary   status=200 latency=134ms user=42
2026-02-03T13:40:22Z INFO  GET  /api/itinerary   status=200 latency=98ms user=42
2026-02-03T13:40:23Z WARN  POST /api/itinerary   status=429 latency=210ms user=42
2026-02-03T13:40:24Z INFO  GET  /api/profile     status=200 latency=55ms user=17
2026-02-03T13:40:25Z ERROR GET  /api/itinerary   status=500 latency=512ms user=42
2026-02-03T13:40:26Z INFO  GET  /health          status=200 latency=5ms
2026-02-03T13:40:27Z INFO  POST /api/login       status=401 latency=80ms
2026-02-03T13:40:28Z ERROR POST /api/login       status=500 latency=430ms
2026-02-03T13:40:29Z INFO  GET  /api/profile     status=304 latency=12ms user=17
2026-02-03T13:40:30Z WARN  GET  /api/profile     status=404 latency=40ms user=17
"""
text = LOG_TEXT

# 1) total requests = count lines that look like log lines
levels = re.findall(r"\b(INFO|WARN|ERROR)\b", text)
total_requests = len(levels)

# 2) ERROR lines
error_lines = 0
for lvl in levels:
    if lvl == "ERROR":
        error_lines += 1

# 3) paths (grab /something right after method)
paths = re.findall(R"\b(?:GET|POST|PUT|DELETE)\s+(/\S+)", text)
top_2_paths = Counter(paths).most_common(2)

# 4) status + latency pairs, then average latency where status >= 400
pairs = re.findall(r"status=(\d{3})\s+latency=(\d+)ms", text)
bad_latencies = [int(lat) for (status, lat) in pairs if int(status) >= 400]
avg_latency_bad = (sum(bad_latencies) / len(bad_latencies)) if bad_latencies else 0.0

print("Total parsed requests:", total_requests)
print("ERROR lines:", error_lines)
print("Top 2 paths:", top_2_paths)
print(f"Avg latency for status>=400: {avg_latency_bad:.2f} ms")