import re
import pandas as pd

log_file = "5g_kpi_logs.txt"
data = []

with open(log_file, "r") as f:
    for line in f:
        match = re.search(r"\[(.*?)\] gNodeB_ID=(\d+) CellID=(\d+) RRC_Conn_Success=(\d+) RRC_Conn_Attempts=(\d+) Throughput_DL=([\d.]+)Mbps Latency=(\d+)ms", line)
        if match:
            timestamp, gnb, cell, success, attempts, dl_throughput, latency = match.groups()
            success_rate = round((int(success) / int(attempts)) * 100, 2)
            data.append({
                "Time": timestamp,
                "gNodeB_ID": int(gnb),
                "CellID": int(cell),
                "Success_Rate": success_rate,
                "DL_Throughput(Mbps)": float(dl_throughput),
                "Latency(ms)": int(latency)
            })

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Optional: Save as CSV
df.to_csv("kpi_summary.csv", index=False)
