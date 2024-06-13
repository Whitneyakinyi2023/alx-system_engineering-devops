### Post-Mortem Report

![Alt text](https://github.com/Whitneyakinyi2023/alx-system_engineering-devops/blob/master/0x19-postmortem/SERVER.PNG)

#### Issue Summary
**Date**: 6TH JUNE, 2024 
**Incident**: High number of failed HTTP requests on Nginx web server  
**Impact**: 943 out of 2000 HTTP requests failed during load testing with ApacheBench.

#### Actions Taken
1. **Identified the Issue**: Noted high failure rate of HTTP requests (943 failed out of 2000) when benchmarking the Nginx web server using ApacheBench.
2. **Investigated System Configuration**:
    - Confirmed the server was running
g Ubuntu 20.04 instead of the required Ubuntu 14.04.
    - Updated the system and installed Apache.
    - Checked Nginx configuration and adjusted settings in `/etc/default/nginx` to increase maximum open files limit.
3. **Modified Nginx Configuration**:
    - Increased the `max open files` limit to 4096 in `/etc/default/nginx`.
    - Restarted Nginx to apply new settings.

#### Misleading Investigation Paths
1. **Initial Focus on Nginx**: Initially assumed the issue was purely related to Nginx configuration, overlooking potential underlying OS version compatibility issues.
2. **Network Configuration**: Spent time investigating potential network issues which were not the root cause.
3. **Server Hardware Limitations**: Considered and ruled out server hardware limitations as the cause of the failures.

#### Escalation to Other Engineers
The incident was escalated to the DevOps team for further investigation and resolution. The team worked together to identify the root cause and implement the necessary configuration changes.

#### Incident Resolution
1. **Downgraded Ubuntu Version**:
    - Reinstalled the server with Ubuntu 14.04 to meet compatibility requirements.
2. **Configuration Adjustments**:
    - Updated and installed necessary software packages.
    - Adjusted Nginx settings to handle a higher number of concurrent connections.
3. **Validation and Testing**:
    - Re-ran ApacheBench tests to validate the fixes.
    - Achieved 0 failed requests in subsequent tests, confirming the issue was resolved.

#### Root Causes and Resolution
**Root Causes**:
1. **Incompatible OS Version**: The server was running Ubuntu 20.04 instead of the required 14.04, leading to compatibility issues with Nginx and system configurations.
2. **Insufficient Configuration for High Load**: The default Nginx configuration did not support the high number of concurrent requests being tested.

**Resolutions**:
1. **OS Downgrade**: Downgraded the server to Ubuntu 14.04 to ensure compatibility.
2. **Increased Resource Limits**: Modified the `max open files` setting in `/etc/default/nginx` to 4096 and restarted Nginx to apply changes.

### Detailed Logs and Commands
```shell
# Original ApacheBench Test Results
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
...
Failed requests:        943
...

# Downgrade Ubuntu Version (example command sequence)
sudo do-release-upgrade -d

# Update and Install Apache
sudo apt-get update
sudo apt-get install apache2

# Modify Nginx Configuration
echo "ulimit -n 4096" | sudo tee -a /etc/default/nginx
sudo service nginx restart

# Puppet Manifest to Apply Changes
exec {'modify max open files limit setting':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => 'usr/local/sbin:/usr/local/bin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

# Re-run ApacheBench Test to Confirm Fix
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
...
Failed requests:        0
...
```

#### Conclusion
The incident was caused by an incompatible OS version and insufficient Nginx configuration for high load. The issue was resolved by downgrading the OS and increasing resource limits in Nginx. Future steps include ensuring all system requirements are met and pre-configured for high load scenarios.