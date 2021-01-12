# Resource-Utlization

## An Ansible script to deploy, schedule python script to get resources utlization and Install Linux Packages on Centos Linux Servers 

> To use this Script:

1. Add your Servers IPs to inventory file.
2. Add Linux Packages in vars.json file to install them by using yum.
3. Run the command:
   > ` ansible-playbook -i inventory main.yml -e "@vars.json" `
4. You can override the values in vars.json file by running this command:   
> `ansible-playbook -i inventory main.yml -e "linux_packages="vim"" `

> Folder Structure:

```
Resources-Utilization-Task/
├── inventory
├── main.yml
│   ├── JdkInstall
│   │   └── tasks
│   │       └── main.yml
│   ├── linuxPkgs
│   │   └── tasks
│   │       └── main.yml
│   └── resources
│       ├── files
│       │   └── resources.py
│       └── tasks
│           └── main.yml
└── vars.json

```

> How it works:

1. Ansible roles added to roles Directory and be added to the main file:
    1. resources role : copy the python script to the ` /opt ` directory and create the cronjob
    2. linuxPkgs role: install the Linux packages that added to ` vars.json` or override them while running the script.
    3. JdkInstall role : install JDK 11 by using `yum`
2. Add server IPs to inventory file     


