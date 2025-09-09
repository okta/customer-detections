## Move and Deactivate Malicious Self-Service Registration (SSR) Users

This workflow is for identifying and managing malicious self-service registration (SSR) users. The process involves moving these users to a designated group and then deactivating their accounts.

### Prerequisites
* Create a new group specifically for malicious SSR users (e.g SSR Group). Note down the ID.
* Maintain the table for bad reputation or temporary email domains

### Event Hooks workflow
This workflow is triggered by user creation events - subscribe to "User created". Its purpose is to automatically identify and manage users with specific email domains by moving them to a designated group and immediately deactivating their accounts.

### Scheduled workflow
* the parent flow looks for user status that s STAGED
* if a user's email domain is in the table list, move it to the SSR group and deactive the user
* if a user's email domain is not in the list, and the user has been in the STAGED status for more than a certain time (in the example, 35 mins), move it to the SSR group and deactive the user.

### Note
* please review the users in the SSR group
* please keep the table up-to-date
* modify the workflows to suit your use case
