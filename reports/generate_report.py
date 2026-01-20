import pandas as pd
from jinja2 import Template

aws_df = pd.read_csv("aws_costs.csv")
gcp_df = pd.read_csv("gcp_costs.csv")

template = Template("""
<h1>Cloud Cost Optimization Report</h1>
<h2>AWS Costs</h2>
{{ aws_table }}

<h2>GCP Costs</h2>
{{ gcp_table }}

<p><b>Estimated Savings Potential:</b> 30–45%</p>
""")

html = template.render(
    aws_table=aws_df.to_html(index=False),
    gcp_table=gcp_df.to_html(index=False)
)

with open("reports/cost_report.html", "w") as f:
    f.write(html)

print("Report generated: reports/cost_report.html")
