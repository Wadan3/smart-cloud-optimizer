import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("[*] Generating Cloud Server Metrics for the last 90 days...")
start_date = datetime.now() - timedelta(days=90)
timestamps = [start_date + timedelta(hours=i) for i in range(90 * 24)]

data = []
for ts in timestamps:
    hour = ts.hour
    if 8 <= hour <= 18:
        cpu = np.random.normal(75, 10) 
        ram = np.random.normal(65, 15)
    else:
        cpu = np.random.normal(20, 5) 
        ram = np.random.normal(30, 10)

    cpu = min(max(cpu, 1), 100)
    ram = min(max(ram, 1), 100)
    cost = 0.1 + (cpu * 0.005)

    data.append({
        'timestamp': ts.strftime("%Y-%m-%d %H:%M:%S"),
        'cpu_usage_percent': round(cpu, 2),
        'ram_usage_percent': round(ram, 2),
        'hourly_cost_usd': round(cost, 3)
    })

df = pd.DataFrame(data)
df.to_csv('server_logs.csv', index=False)
print(f"[+] Dataset 'server_logs.csv' successfully generated with {len(df)} hourly records!")