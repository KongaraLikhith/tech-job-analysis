import requests
import sqlite3
import pandas as pd

# Step 1: Connect to SQLite database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create main jobs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT,
    title TEXT,
    company TEXT,
    location TEXT,
    date_posted TEXT,
    url TEXT
)
""")

# Create tags table (normalized, 1 tag per row)
cursor.execute("""
CREATE TABLE IF NOT EXISTS job_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT,
    tag TEXT,
    FOREIGN KEY(job_id) REFERENCES jobs(job_id)
)
""")

# Step 2: Fetch data from RemoteOK API
url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
jobs = response.json()[1:]  # skip metadata

# Step 3: Parse jobs and insert into DB
for job in jobs:
    job_id = str(job.get("id"))
    title = job.get("position")
    company = job.get("company")
    location = job.get("location") if job.get("location") else "Remote"
    date_posted = job.get("date")
    url = job.get("url")

    # Insert into jobs table
    cursor.execute("""
    INSERT INTO jobs (job_id, title, company, location, date_posted, url)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (job_id, title, company, location, date_posted, url))

    # Insert each tag separately into job_tags table
    tags = job.get("tags") if job.get("tags") else []
    for tag in tags:
        cursor.execute("""
        INSERT INTO job_tags (job_id, tag)
        VALUES (?, ?)
        """, (job_id, tag))

# Commit changes
conn.commit()

# Step 4: Export to CSV (for Tableau)
df_jobs = pd.read_sql_query("SELECT * FROM jobs", conn)
df_tags = pd.read_sql_query("SELECT * FROM job_tags", conn)

df_jobs.to_csv("jobs.csv", index=False)
df_tags.to_csv("tags.csv", index=False)

# Close connection
conn.close()

print("✅ Jobs saved to jobs.db, exported as jobs.csv & tags.csv")
