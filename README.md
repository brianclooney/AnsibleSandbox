# Ansible Personal Learning Sandbox

## Overview
This repository serves as my personal sandbox for learning and experimenting with Ansible. It includes a variety of Ansible playbooks and roles that I am using to explore different functionalities of Ansible and its potential use cases. This setup is designed to help me understand how Ansible works and how it can be applied to automate the deployment and management of applications and systems.

Example extra vars for Semaphore UI

```
{
    "app_name": "example-app",
    "app_domains": [
	"app.example.com"
    ],
    "certbot": {
	"email": "admin@example.com"
    },
    "my_service": {
	"db_root_password": "P@s5w0rD",
	"db_user": "user01",
	"db_password": "P@s5w0rD",
	"db_database": "my_service_db"
    }
}
```