import boto3
import pandas as pd
from datetime import datetime, timedelta

client = boto3.client('ce')

def get_aws_costs():
    end = datetime.today()
    start = end - timedelta(days=30)

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    data = []
    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        cost = float(group['Metrics']['UnblendedCost']['Amount'])
        data.append([service, cost])

    df = pd.DataFrame(data, columns=['Service', 'CostUSD'])
    return df

if __name__ == "__main__":
    df = get_aws_costs()
    print("\nAWS Cost Breakdown (Last 30 Days):")
    print(df.sort_values(by='CostUSD', ascending=False))
