# Webstack Monitoring

## Premise
Server Monitoring involves systematically tracking the performance, health, and availability of servers to ensure optimal functioning of applications and services. Monitoring servers provides insights into resource utilization, potential bottlenecks, security vulnerabilities, and overall system stability. It enables proactive issue detection, rapid troubleshooting, and effective capacity planning. You can get information from logs if in command-line.

## Installation

###Steps
1.Sign up for data-dog

-Log in to your Ubuntu 20.04 LTS server.  
-Run the following commands in your terminal:  

'''bash
DD_API_KEY=YOUR_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
'''

Replace YOUR_API_KEY with your Datadog API key.

2.Install Datadog Agent on Your Server:
-Log in to your Ubuntu 20.04 LTS server
-Run the following commands in your terminal:
'''bash
DD_API_KEY=YOUR_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
'''

Replace YOUR_API_KEY with your Datadog API key.
