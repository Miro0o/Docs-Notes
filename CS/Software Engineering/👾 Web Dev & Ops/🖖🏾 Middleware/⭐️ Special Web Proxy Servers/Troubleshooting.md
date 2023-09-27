# Troubleshooting

[TOC]



## 👉 Nginx Failed to Start
#nginx 

Most of the case this is due to port block or other web server is running. 
TO eliminate fault reasons: 
1. check out port 80, 8080, 8888, 443, etc.
2. check out other web server is runnin or not (e.g. apache2)
3. check out `systemctl status nginx`
4. check out `nginx -t`
5. `/var/log/nginx/error.log`
6. `/var/log/syslog`
7. 

[nginx.service failed because the control process exited]: https://stackoverflow.com/questions/35868976/nginx-service-failed-because-the-control-process-exited
