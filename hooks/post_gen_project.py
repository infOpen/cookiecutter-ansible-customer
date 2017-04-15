import os
import sys

from jinja2 import Template


def manage_country(country):
    """Create country layout

    :param country: country name
    :type country: str or unicode

    """

    country_path = 'inventories/{}'.format(country)
    environments = '{{ cookiecutter.environments }}'.split(',')

    if not os.path.exists(country_path):
        os.makedirs(country_path)

    for environment in environments:
        manage_environment(country, environment)


def manage_environment(country, environment):
    """Create environment layout

    :param country: country name
    :type country: str or unicode
    :param environment: environment name
    :type environment: str or unicode

    """

    environment_layout = [
        'group_vars',
        'host_vars',
    ]

    for item in environment_layout:
        item_path = 'inventories/{}/{}/{}'.format(country, environment, item)
        if not os.path.exists(item_path):
            os.makedirs(item_path)

        # Manage .keep file for git repository
        open(item_path + '/.keep', 'a').close()

    # Manage environment hosts file
    manage_hosts_file(country, environment)
    manage_group_vars_all_file(country, environment)


def manage_hosts_file(country, environment):
    """Create environment layout

    :param country: country name
    :type country: str or unicode
    :param environment: environment name
    :type environment: str or unicode

    """

    CONTENT = """
{% raw %}
# {{ country | capitalize }} {{ environment }} inventory
#==============================================================================

# Common inventory vars and environment group
#------------------------------------------------------------------------------
[all:vars]
{% endraw %}"""

    hosts_path = 'inventories/{}/{}/hosts'.format(country, environment)
    template = Template(CONTENT)
    template.stream(country=country, environment=environment).dump(hosts_path)


def manage_group_vars_all_file(country, environment):
    """Create environment group_vars all.yml file

    :param country: country name
    :type country: str or unicode
    :param environment: environment name
    :type environment: str or unicode

    """

    CONTENT = """
{% raw %}
# {{ country | capitalize }} {{ environment }} default vars
#==============================================================================

# General
#------------------------------------------------------------------------------
dep_country: "{{ country }}"
dep_environment: "{{ environment }}"
{% endraw %}"""

    vars_file_path = 'inventories/{}/{}/group_vars/all.yml'.format(
        country, environment)
    template = Template(CONTENT)
    template.stream(
        country=country, environment=environment).dump(vars_file_path)


def main():
    """Hook entry point"""

    try:
        countries = '{{ cookiecutter.countries }}'.split(',')
        for country in countries:
            manage_country(country)
    except:
        print('Countries or environments create errors !')
        sys.exit(1)

main()
