# lab4-2 REFFLECTION

## What open ports did you find, and which banners were most informative?
There were 2 open ports on scanme.nmap.org: port 2 and 80.
The banner for port 2 was "SSH-2.0-OpenSSH_7.4", which is a version from 2016. The banner for port was "Apache/2.4.6 (CentOS)", which is a version from 2013. This banner was very informative because it specified the exact Apache version and the underlying operating system (CentOS).

## Any false negatives or timeouts encountered? Why?
When probing UDP port 53 on scanme.nmap.org there's was no response. But this wasn't a false negative, the service just needed proper DNS protocol packets to respond. This shows a limitation of UDP scanning, which is the ambiguity between closed, filtered and open but silent service. 
TCP scanning was more reliable. There were no false negatives, in fact closed ports returned "connection refused" errors instead of timeouts.

## One defensive recommendation for an admin to reduce information leakage.
To reduce information leakage, admins should implement banner hiding and service hardening. For web servers, configure Apache to only display Apache without the version details. For SSH, modify it to use a generic banner.
Also it's good to update services to current versions.