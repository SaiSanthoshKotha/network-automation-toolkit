-- Create table (in SQLite)
CREATE TABLE kpi_logs (
    Time TEXT,
    gNodeB_ID INTEGER,
    CellID INTEGER,
    Success_Rate REAL,
    DL_Throughput REAL,
    Latency INTEGER
);

-- Insert sample row (you'd usually import the CSV instead)
INSERT INTO kpi_logs VALUES ('2025-06-13 10:05:23', 501, 10, 98.0, 112.5, 25);

-- 1. Average Throughput per gNodeB
SELECT gNodeB_ID, AVG(DL_Throughput) as Avg_DL_Throughput
FROM kpi_logs
GROUP BY gNodeB_ID;

-- 2. List entries with high latency
SELECT * FROM kpi_logs
WHERE Latency > 30;

-- 3. Success Rate drop below 90%
SELECT * FROM kpi_logs
WHERE Success_Rate < 90;
