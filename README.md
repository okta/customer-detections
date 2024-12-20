[![Blog](https://img.shields.io/badge/blog-okta_security-blue)][secblog]
[![Advisories](https://img.shields.io/badge/advisories-okta_security_advisories-blue)][advisories]
[![EventTypes](https://img.shields.io/badge/docs-okta_event_types-blue)][eventtypes]

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

These events can be [browsed, searched or filtered in the admin console](https://help.okta.com/en-us/content/topics/reports/syslog-filters.htm). They can also be queried and [filtered](https://developer.okta.com/docs/reference/api/system-log/#filtering-results) programmatically via the [System Log API](https://developer.okta.com/docs/reference/api/system-log/), and can be [exported](https://support.okta.com/help/s/article/Exporting-Okta-Log-Data?language=en_US) or [streamed](https://help.okta.com/en/prod/Content/Topics/Reports/log-streaming/about-log-streams.htm) to third-party security monitoring tools. 

Okta Security recommends the use of [Log Streaming](https://help.okta.com/en-us/Content/Topics/Reports/log-streaming/about-log-streams.htm) to capture events in third-party security tools in close to real-time, and/or the use of [Event Hooks](https://developer.okta.com/docs/concepts/event-hooks/) and [Workflows](https://www.okta.com/platform/workflows/) for security orchestration opportunities.

Most events in System Log follow a similar pattern:
*user.account.password_reset*
`<domain>.<resource>.<action>`


Some of the queries listed below use the following operators to group multiple events together:

| Operator | Description |
| ------------- | ------------- |
| `eq` | Equals |
| `ne` | Not Equal to | 
| `sw` | Starts With |
| `ew` | Ends With | 
| `co` | Contains |

Okta recommends customers review these detections and run searches using those that appear to be applicable to your environment. Perform any necessary tuning or baselining to ensure they deliver high fidelity results prior to creating an alert. 

Note: Most of these detections leverage Okta system log query languages, however a subset is provided in splunk query language. A plain english description of the detection logic is provided for splunk queries to allow detection engineers to implement in their SIEM of choice.

[secblog]: https://sec.okta.com/articles
[advisories]: https://trust.okta.com/security-advisories/
[eventtypes]: https://developer.okta.com/docs/reference/api/event-types/