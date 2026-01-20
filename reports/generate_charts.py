import pandas as pd
import matplotlib.pyplot as plt

def aws_cost_chart(csv_file):
    df = pd.read_csv(csv_file)

    plt.figure()
    plt.bar(df['Service'], df['CostUSD'])
    plt.xticks(rotation=75, ha='right')
    plt.title("AWS Cost Breakdown by Service")
    plt.tight_layout()
    plt.savefig("reports/aws_costs.png")
    plt.close()

if __name__ == "__main__":
    aws_cost_chart("aws_costs.csv")
