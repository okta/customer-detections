# Workflow: Automated IP Blocking by System Log Activity

* This workflow monitors activity in your Okta tenant, based on a system log query.  Every 5 minutes, this workflow will stream all the results of a System Log query, and count the number of times each IP address has performed some action.  Then if any IP Address exceeds a specific threshold, then that IP Address is dynamically added to a Network Zone, which can then be used to block traffic.
For example, if you are under a credential stuffing attack, then the query  `eventType eq "user.session.start" AND outcome.reason eq "INVALID_CREDENTIALS"` will highlight all failed attempts.  If an IP Address then has more than 10 failures within a 1 hour period, then this ip can be blocked.
---
> [!CAUTION]
> **Risk of Admin Lockout:** Improper configuration can block your own IP address or corporate office ranges, preventing administrative access. **Ensure your "IP Allowlist" table is fully populated before enabling this workflow.**
---
### **Implementation Steps**
1. **Import the Workflow:** Download and import the workflow package into your Okta Workflows environment.
2. **Identify Known Good IPs:** Gather a list of trusted IP addresses, such as corporate office ranges, VPN gateways, and administrator IPs.
3. **Configure the "IP Allowlist" Table:** * Open the **IP Allowlist** table.
   * Paste your trusted IPs into this table. The workflow will ignore activity from these addresses.
4. **Create a Network Zone:** * In the Okta Admin Console, create a new **IP Zone** (e.g., "Failed Login Blocklist"). 
   * Record the exact name of this zone.
5. **Set the Target Zone in the Workflow:** * Open the workflow: **"Update Network Zone to Include IP"**
   * Locate the **Compose** card labeled `Network Zone Name`.
   * Paste the exact name of your new zone into this box.
6. **Set the System Log Query** * Open the workflow **"Count Activity By IP Address"**
   * Navigate to the Search System Logs Tab
   * Update the query to track the behavior you would like to block. We recommend running this query in Okta System Log to ensure the query is targetting the correct traffic
7. **Configure the Blocking Threshold:**
   * Open the workflow: **"Update Network Zone from IP Count Table."**
   * Find the **Search Rows** card.
   * Adjust the `Where` expression to set your session threshold (e.g., `login_attempts > 10`).
   * *Note: This counts total login attempts, not just failures. A higher threshold reduces false positives but allows more attack attempts before blocking.*
8. **Enable the Workflows:** Turn on all workflows within the bundle.
9.  **Enforce via Policy:** Update your **Global Session Policy** to "Deny" access for any traffic originating from the Network Zone created in Step 4.
---
### **Technical Logic**
* **Real-Time Tracking:** The **"Count Logins by IP Address"** workflow triggers on every login event, updating the **"IP Login Count"** table with the current tally for each unique IP.
* **Scheduled Enforcement:** Every 10 minutes (configurable), the **"Add IP to Network Zone"** workflow scans the table for IPs exceeding your threshold and moves them to the blocklist.
* **Capacity Limit:** Okta Workflow tables support a maximum of **500,000 rows**. Ensure you have a strategy to clear old data or monitor table growth to prevent performance degradation.
* **Allow List** An Allowlist table is provided to create a set of safe IP Addresses, to prevent blocking critical infrastructure.
