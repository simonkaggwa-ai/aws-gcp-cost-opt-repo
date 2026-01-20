from google.cloud import monitoring_v3
from google.cloud import compute_v1
from datetime import datetime, timedelta

CPU_THRESHOLD = 5.0

monitoring_client = monitoring_v3.MetricServiceClient()
compute_client = compute_v1.InstancesClient()
project_id = "your-gcp-project-id"

def list_instances(zone):
    return compute_client.list(project=project_id, zone=zone)

def get_average_cpu(instance_id):
    interval = monitoring_v3.TimeInterval(
        end_time=datetime.utcnow(),
        start_time=datetime.utcnow() - timedelta(days=14)
    )

    results = monitoring_client.list_time_series(
        request={
            "name": f"projects/{project_id}",
            "filter": f'metric.type="compute.googleapis.com/instance/cpu/utilization" AND resource.label.instance_id="{instance_id}"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
    )

    values = []
    for ts in results:
        for point in ts.points:
            values.append(point.value.double_value * 100)

    if not values:
        return 0.0

    return round(sum(values) / len(values), 2)
