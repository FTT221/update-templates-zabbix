# Update templates zabbix

Download Zabbix templates from the Zabbix repository (https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates?at=refs%2Fheads%2Frelease%2F7.0)

Specify the path to the templates folder in the main.py file by adding the line: TEMPLATES_DIR = '/home/user/templates'.

- #### Installation and Usage:
Specify the path to the templates folder in the main.py file.
Add your Zabbix API token and IP address to the main.py file.
Install required packages:

```
apt install python3 python-pip3
```
```
pip3 install requests pyyaml
```
Run the script:

```
python3 main.py
```
