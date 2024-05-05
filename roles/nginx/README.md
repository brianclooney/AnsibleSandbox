
### /etc/<container_name>

Purpose: The /etc/<container_name> directory contains the configuration files for the container.
This might include a main configuration file (main.conf), additional configuration files (additional.conf), and any custom configurations (custom_configs/).

### /var/log/<container_name>

Purpose: The /var/log/<container_name> directory contains log files for the container, such as access.log and error.log.
This follows the standard practice of storing logs under /var/log.

### /var/lib/<container_name>

Purpose: The /var/lib/<container_name> directory can store static files for the container, such as index.html.
Using /var/lib aligns with the typical practice of storing variable data for applications under this directory.

### Named Docker Volumes

For other persistent data that the container generates or uses, you should use named Docker volumes.
This keeps the data associated with the container but separate from the host filesystem, enhancing portability and isolation.


```
/
├── etc/
│   ├── web-gateway/
│   │   ├── nginx.conf
│   │   ├── conf.d/
│   │   │   ├── default.conf
│   │   │   ├── app1.conf
│   │   │   ├── app2.conf
│   │   ├── servers/
│   │   │   ├── app1/
│   │   │   │   ├── ssl.conf
│   │   │   │   ├── locations/
│   │   │   │   │   ├── microservice1.conf
│   │   │   │   │   ├── microservice2.conf
│   │   │   ├── app2/
│   │   │   │   ├── ssl.conf
│   │   │   │   ├── locations/
│   │   │   │   │   ├── microservice3.conf
│   │   │   │   │   ├── microservice4.conf
├── var/
│   ├── log/
│   │   ├── web-gateway/
│   │   │   ├── app1/
│   │   │   │   ├── access.log
│   │   │   │   ├── error.log
│   │   │   ├── app2/
│   │   │   │   ├── access.log
│   │   │   │   ├── error.log
│   ├── lib/
│   |   ├── web-gateway/
│   |   │   ├── app1/
│   |   │   │   ├── index.html
│   |   │   ├── app2/
│   |   │   │   ├── index.html
```