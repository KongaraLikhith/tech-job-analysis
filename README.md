# RemoteOK Job Scraper & Tableau Dashboard

This project collects job postings from the [RemoteOK API](https://remoteok.com/api), stores them in a SQLite database, exports them into CSVs, and visualizes insights with **Tableau**.

## Features
- Fetches latest remote job postings from RemoteOK API
- Stores data in a normalized SQLite database:
  - `jobs` → job details (title, company, location, date, url)
  - `job_tags` → one tag per row linked to jobs
- Exports clean CSV files (`jobs.csv`, `tags.csv`)
- Ready-to-use Tableau dashboard for interactive insights

## Visualizations
Some insights you can explore in Tableau:
-  Job postings by **location**
-  Top hiring **companies**
-  Most in-demand **skills/tags**
-  Skills by Company
-  Top 15 technologies

You can access to the dashboard via this link - https://public.tableau.com/app/profile/likhith.kongara/viz/TechJobMarketAnalysis/Dashboard1
And the Story here - https://public.tableau.com/app/profile/likhith.kongara/viz/TechJobMarketAnalysis/Story1
## Project Structure
Analysis
 - saved tableau package
data
 - raw
    - jobs.db
 - csv files
    - jobs.csv
    - tags.csv
src
 - main.py
README.md
requirements.txt
