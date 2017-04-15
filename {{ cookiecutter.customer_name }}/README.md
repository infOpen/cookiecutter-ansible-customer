# Ansible deployment for {{ cookiecutter.customer_name }}

## Prepare environment

- Create a virtual env for the project
- Install Python dependencies
```
pip install -r requirements-python.txt
```
- Install Ansible dependencies
```
ansible-galaxy install -r requirements-ansible.yml
```

## Testing

Test are managed via [Molecule](https://github.com/metacloud/molecule/) v2,
to be able to use scenario.

Today, we need to link manually country and environment specific vars to the
scenario to test it:
```
rm -rf $PWD/molecule/<scenario>/.molecule/group_vars \
&& ln -s "$PWD/inventories/<country>/<environment>/group_vars" $PWD/molecule/<scenario>/.molecule/group_vars \
&& molecule test
```
