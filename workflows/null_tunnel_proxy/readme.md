## Prevent Authentication from Anonymizer Proxies when the Operator is Null

The Workflow prevents authentication from anonymizer proxies when the operator is null. The Workflow grabs tunnel and user id info and then checks if the tunnel attribute has a value that matches {"anonymous":true,"operator":null,"type":"PROXY"}. After checking that the tunnels attribute specifies an anonymous proxy with a null operator, the flow checks that the user is in a particular group. You'll need to enter in the desired group ID when configuring the workflow. If there is a match then the user session is cleared and the password is reset.

### Prerequisites
* The user belongs to a specific group. Note down the ID and input into workflow: list Find card -> comparison field

### Event Hooks workflow
This workflow is triggered by user mfa authentication events - subscribe to "Authentication of user via MFA". Its purpose is to automatically prevents authentication from anonymizer proxies when the operator is null. 

### Note
* how to import - refer to https://help.okta.com/wf/en-us/content/topics/workflows/build/export-import-flows.htm
* modify the workflows to suit your use case
