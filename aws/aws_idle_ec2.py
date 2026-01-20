import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

CPU_THRESHOLD = 5.0  # percent

def get_running_instances():
    reservations = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )['Reservations']

    instances = []
    for r in reservations:
        for i in r['Instances']:
            instances.append(i['InstanceId'])
    return instances

def get_average_cpu(instance_id):
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=datetime.utcnow() - timedelta(days=14),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=['Average']
    )

    datapoints = response['Datapoints']
    if not datapoints:
        return 0.0

    avg = sum(d['Average'] for d in datapoints) / len(datapoints)
    return round(avg, 2)

def find_idle_instances():
    idle = []
    for instance in get_running_instances():
        avg_cpu = get_average_cpu(instance)
        if avg_cpu < CPU_THRESHOLD:
            idle.append((instance, avg_cpu))
    return idle

if __name__ == "__main__":
    idle_instances = find_idle_instances()
    print("\nIdle EC2 Instances (<5% CPU):")
    for inst, cpu in idle_instances:
        print(f"{inst} - Avg CPU: {cpu}%")
