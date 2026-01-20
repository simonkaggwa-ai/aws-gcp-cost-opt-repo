from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

QUERY = """
SELECT
  service.description AS service,
  SUM(cost) AS total_cost
FROM `your_project.your_dataset.gcp_billing_export_v1_*`
GROUP BY service
ORDER BY total_cost DESC
"""

def get_gcp_costs():
    query_job = client.query(QUERY)
    df = query_job.to_dataframe()
    return df

if __name__ == "__main__":
    df = get_gcp_costs()
    print("\nGCP Cost Breakdown:")
    print(df)
