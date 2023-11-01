import boto3
import json
import os

def get_metrics_from_json_folder(json_folder_path):
    # Initialize the CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # List all JSON files in the specified folder
    for filename in os.listdir(json_folder_path):
        if filename.endswith('.json'):
            json_file_path = os.path.join(json_folder_path, filename)

            # Read the metric query from the JSON file
            with open(json_file_path, 'r') as file:
                metric_query = json.load(file)

            # Get the metric data
            response = cloudwatch.get_metric_data(MetricDataQueries=metric_query)

            # Extract and print the metric data
            if 'MetricDataResults' in response:
                for result in response['MetricDataResults']:
                    if 'Values' in result:
                        print(f"Metric Name: {result['Label']}")
                        print(f"Values: {result['Values']}")

# Specify the path to the folder containing JSON files
json_folder_path = 'jsons'  # Adjust the folder name if needed

# Call the function with the JSON folder
get_metrics_from_json_folder(json_folder_path)
