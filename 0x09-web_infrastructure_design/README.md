This project focuses on building a strong understanding of web infrastructure and its core components.

Learning Objectives:

By the end of this project, you should be able to:

Explain the web stack: You'll be able to draw and explain a diagram showcasing the web stack you built, highlighting the role of each component.
Understand system redundancy: You'll gain insights into mechanisms that ensure system functionality even during failures (e.g., high availability clusters).
Acronyms: You'll become familiar with commonly used acronyms in web infrastructure, including LAMP, SPOF, and QPS.
Copyright Notice

Plagiarism is strictly prohibited. You are expected to complete the tasks independently,  avoiding any copy-pasting of solutions. Refrain from publishing any project content as well.

Requirements

A README.md file at the project's root directory is mandatory.
Whiteboard each task (diagrams) and take screenshots for submission.
Upload screenshots to an image hosting service (like Imgur).
Push your answer file with image links to GitHub.
Be prepared to whiteboard tasks during a session (no notes or computers allowed).
Focus:

Concentrate on the core requirements mentioned. Avoid unnecessary details unless instructed otherwise.

Resources

Network basics concepts
Server concepts
Web server concepts
DNS concepts
Load balancer concepts
Monitoring concepts
What is a database?
Difference between web server and app server
DNS record types
Single point of failure (SPOF)
Avoiding downtime during deployments
High availability clusters (active-active/active-passive)
What is HTTPS?
What is a firewall?
Tasks

Simple Web Stack (Mandatory): Design a single-server web infrastructure using LAMP stack (Linux, Apache, MySQL, PHP) to  host the website www.foobar.com [invalid URL removed]. Explain the roles of server, domain name, DNS records, web server, application server, database, and communication protocols. Additionally,  discuss limitations like SPOF, downtime during maintenance, and scalability issues.

Distributed Web Infrastructure (Mandatory):  Design a three-server web infrastructure for www.foobar.com [invalid URL removed]. Introduce components like a load balancer (HAproxy) and a database cluster (primary-replica) to enhance scalability and redundancy. Explain the purpose of each element, load balancing algorithms, active-active vs. active-passive setups, and how the database cluster functions. Identify remaining SPOFs and security concerns (missing firewalls and HTTPS).

Secured and Monitored Web Infrastructure (Mandatory): Design a secure and monitored three-server infrastructure for www.foobar.com [invalid URL removed] with features like firewalls, HTTPS, and monitoring. Explain the roles of firewalls, HTTPS encryption, monitoring tools (data collection), and how to monitor web server QPS.  Discuss potential issues like terminating SSL at the load balancer, single writable MySQL server, and having servers with all components (web, application, database).

Scale Up (Advanced):  This advanced task involves adding a load balancer cluster and splitting components (web server, application server, database)  across separate servers to enhance scalability. Explain the purpose of each addition.
