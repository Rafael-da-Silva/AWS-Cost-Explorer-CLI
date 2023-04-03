from boto3 import Session
from datetime import datetime
from decimal import Decimal
from botocore.exceptions import NoCredentialsError, ClientError

# Configure AWS credentials
try:
    session = Session(profile_name='default')
    client = session.client('ce')
except (NoCredentialsError, ClientError) as e:
    print(f"Error configuring AWS credentials: {e}")
    exit(1)

# Define analysis period
start_date = datetime(2023, 3, 1)
end_date = datetime(2023, 3, 31)

# Format date strings for display
start_date_str = f"{start_date:%d/%m/%Y}"
end_date_str = f"{end_date:%d/%m/%Y}"

# Initialize total cost variable
total_cost = Decimal('0')

# Retrieve aggregated costs by service
try:
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.strftime('%Y-%m-%d'),
            'End': end_date.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )
except Exception as e:
    print(f"Error retrieving AWS costs: {e}")
    exit(1)

# Check if there are results available for the specified period
if len(response['ResultsByTime']) == 0:
    print(f"No cost data available for the period {start_date_str} to {end_date_str}")
    exit(0)

# Display costs by service
for group in response['ResultsByTime'][0]['Groups']:
    # Extract service name and cost from the response
    service_name = group['Keys'][0]
    cost = Decimal(group['Metrics']['UnblendedCost']['Amount'])
    if cost > 0:
        # Add to total cost if cost is greater than zero and display service cost information
        total_cost += cost
        print(f"START DATE: {start_date_str} | END DATE: {end_date_str} | SERVICE: {service_name:<45} | COST: {cost:.2f} USD")

# Display total cost for the period
print(f"Total cost for selected period: {total_cost:.2f} USD")
