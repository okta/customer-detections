# {LOGO} Okta Security Detection Catalog
Welcome to the Okta Security Detection Catalog. This repository contains a collection of detection rules for security monitoring and detailed descriptions of log fields used for threat analysis within Okta environments. 

## File Structure
| Folder | Description |
| ------------- | ------------- |
| `detections/`  | List of YAML files for recommended security detections Okta customers can implement within their security monitoring system.   |
| `hunts/`  | Threat hunting queries useful for aiding in detection use case creation  |
| `logs/`  | CSV file with descriptions and examples of all log fields within the Okta system log  |

## Getting Started
Ensure your Okta system logs are being forwarded to a security monitoring system (see https://help.okta.com/en-us/content/topics/reports/log-streaming/about-log-streams.htm). 

Review recommended detections and run searches on ones you want to implement to determine how they fit in your environment. Perform any necessary tuning or baselining to ensure they are high fidelity prior to creating an alert. 

Note: The Okta system log query language is mostly leveraged in these detections, however some are documented in splunk query language. A plain english description of the detection logic is provided for splunk to allow detection engineers to implement in their respective SIEMs. 

## References
https://sec.okta.com/articles
https://trust.okta.com/security-advisories/
https://developer.okta.com/docs/reference/api/event-types/
