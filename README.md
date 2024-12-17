# Okta Security Detection Catalog
Welcome to the Okta Security Detection Catalog. This repository contains a collection of detection rules for security monitoring and detailed descriptions of log fields used for threat analysis within Okta environments. 

## File Structure
| Folder | Description |
| ------------- | ------------- |
| `detections/`  | List of YAML files for recommended security detections Okta customers can implement within their security monitoring system.   |
| `hunts/`  | Threat hunting queries useful for aiding in detection use case creation  |
| `logs/`  | CSV file with descriptions and examples of all log fields within the Okta system log  |

## Getting Started
The System Log provides a detailed log of user, admin and support events relevant to use of the Okta Workforce Identity Cloud.

These events can be [browsed, searched or filtered in the admin console](https://help.okta.com/en-us/content/topics/reports/syslog-filters.htm). They can also be queried and filtered programmatically via the System Log API, and can be exported or streamed to third-party security monitoring tools. 

Okta Security recommends the use of Log Streaming to capture events in third-party security tools in close to real-time, and/or the use of Event Hooks and Workflows for security orchestration opportunities.

Most events in System Log follow a similar pattern:
user.account.password_reset
`<domain>.<resource>. <action>`


Some of the queries listed below use the following operators to group multiple events together:

Review recommended detections and run searches on ones you want to implement to determine how they fit in your environment. Perform any necessary tuning or baselining to ensure they are high fidelity prior to creating an alert. 

Note: The Okta system log query language is mostly leveraged in these detections, however some are documented in splunk query language. A plain english description of the detection logic is provided for splunk to allow detection engineers to implement in their respective SIEMs. 

## References
https://sec.okta.com/articles
https://trust.okta.com/security-advisories/
https://developer.okta.com/docs/reference/api/event-types/
