# Send ip mqtt

This script can be used to get the external ip address and publish to a mqtt broker. 
Can be usefull if you manage remote computers with dynamic ip and don't want to use DynDNS for some reason.

## How to use
1. Schedule the script to be run once every day (or as often use like). 
2. The script will fetch the external ip address and send it to the broker
defined in the variable 
```
broker_address = 'http://<broker address goes here>'
```
