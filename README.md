# cookiecutter-ansible-customer

Cookiecutter template for Ansible managed customer project architecture

## Default variables

```json
{
    "customer_name": "customer_name",
    "countries": "",
    "environments": ""
}
```

*countries* and *environments* are strings comma separated.

## Generated structure

Example with:
* countries: "france,spain"
* environments: "production,testing"

```
├── files
│   └── .keep
├── filter_plugins
│   └── .keep
├── .gitignore
├── inventories
│   ├── france
│   │   ├── production
│   │   │   ├── group_vars
│   │   │   │   ├── all.yml
│   │   │   │   └── .keep
│   │   │   ├── hosts
│   │   │   └── host_vars
│   │   │       └── .keep
│   │   └── testing
│   │       ├── group_vars
│   │       │   ├── all.yml
│   │       │   └── .keep
│   │       ├── hosts
│   │       └── host_vars
│   │           └── .keep
│   ├── .keep
│   └── spain
│       ├── production
│       │   ├── group_vars
│       │   │   ├── all.yml
│       │   │   └── .keep
│       │   ├── hosts
│       │   └── host_vars
│       │       └── .keep
│       └── testing
│           ├── group_vars
│           │   ├── all.yml
│           │   └── .keep
│           ├── hosts
│           └── host_vars
│               └── .keep
├── library
│   └── .keep
├── molecule
│   └── .keep
├── requirements-ansible.yml
├── requirements-python.txt
├── roles
│   ├── externals
│   │   └── .keep
│   └── internals
│       └── .keep
├── templates
│   └── .keep
├── tests
│   └── .keep
├── tox.ini
└── vars
    └── .keep
```
