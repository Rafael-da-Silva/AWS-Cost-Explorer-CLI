# AWS-Cost-Explorer-CLI

This script retrieves the total costs for an AWS account during a specified period and displays the costs broken down by service.

## Prerequisites
* Python 3.x
* boto3 library installed
* AWS credentials with permissions to access AWS Cost Explorer

## Configuration
Configure the script by setting the following variables:

* start_date: The start date of the period to analyze, in datetime.datetime format.
* end_date: The end date of the period to analyze, in datetime.datetime format.
* profile_name: The name of the AWS credentials profile to use.

## Usage
Run the script by executing the following command in the terminal:

`python aws_cost_explorer.py`

The script will display the costs for each service during the specified period and the total cost for the period.

## Error handling
The script will exit with an error message if any of the following conditions are met:

* AWS credentials are not configured correctly.
* An error occurs while retrieving cost data from AWS Cost Explorer.
* No cost data is available for the specified period.

## Example Output
Enter start date for cost analysis (YYYY-MM-DD): 2023-3-01
Enter end date for cost analysis (YYYY-MM-DD): 2023-3-31
START DATE: 01/03/2023 | END DATE: 31/03/2023 | SERVICE: Amazon Elastic Compute Cloud - Compute | COST: 1024.00 USD
START DATE: 01/03/2023 | END DATE: 31/03/2023 | SERVICE: Amazon Relational Database Service     | COST: 532.50 USD
Total cost for selected period: 1556.50 USD