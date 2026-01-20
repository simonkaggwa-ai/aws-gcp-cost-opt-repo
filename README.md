# aws-gcp-cost-opt-repo
This Cloud Cost Optimization Toolkit is a Python-based solution designed to help orgs identify wasted cloud spend and generate actionable cost-saving recommendations across AWS and Google Cloud Platform (GCP).
# Cloud Cost Optimization Toolkit (AWS & GCP)

## Overview
The Cloud Cost Optimization Toolkit is a Python-based solution designed to help
SMEs, NGOs, hospitals, and schools identify wasted cloud spend and generate
actionable cost-saving recommendations across AWS and Google Cloud Platform (GCP).

The toolkit analyzes billing and usage data to uncover idle resources,
right-sizing opportunities, orphaned storage, and potential monthly savings.

---

## Key Features
- AWS and GCP cost analysis
- Idle compute and orphaned storage detection
- Right-sizing recommendations
- Monthly savings projections
- Auto-generated HTML reports
- Budget alerts via email (or Slack-ready)
- Easy to extend with FinOps automation

---

## Supported Platforms
- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)

---

## Tech Stack
- Python 3.9+
- AWS Cost Explorer API
- GCP Billing Export (BigQuery)
- Pandas
- Matplotlib
- Boto3
- Google Cloud SDK

---

## Project Structure
cloud-cost-optimizer/
├── aws/
│ └── aws_cost_analysis.py
├── gcp/
│ └── gcp_cost_analysis.py
├── reports/
│ └── generate_report.py
├── alerts/
│ └── email_alerts.py
├── notebooks/
│ └── cost_analysis.ipynb
├── requirements.txt
└── README.md
