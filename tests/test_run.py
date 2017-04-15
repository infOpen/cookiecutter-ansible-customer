import json
import pytest

# Functions
# ==============================================================================


# Common checks
def common_tests(data, result):

    # General assert
    assert result.exit_code == 0
    assert result.exception is None

    # Structure assert
    assert_root_directory(data, result)
    assert_directories(result)


# Check root project
def assert_root_directory(data, result):
    assert result.project.basename == data.get('customer_name')
    assert result.project.isdir()


# Check directories
def assert_directories(result):

    # Root directories
    project_directories = [
        'files',
        'filter_plugins',
        'inventories',
        'library',
        'molecule',
        'roles',
        'roles/externals',
        'roles/internals',
        'tasks',
        'templates',
        'vars'
    ]

    # Check project directories
    for directory in project_directories:
        assert result.project.join(directory).isdir()


# Check README file
def assert_readme_file(data, result):

    readme_file = result.project.join('README.md')
    readme_lines = readme_file.readlines(cr=False)

    assert readme_file.isfile()
    assert 'Install %s package.' % data.get('ansible_role_name') \
        in readme_lines


# Tests
# ==============================================================================

# Template test
@pytest.mark.parametrize('data_filename, customer_name', [
    ('./cookiecutter.json', 'customer_name'),
    ('./tests/test_01.json', 'test_01'),
])
def test_json_values(cookies, data_filename, customer_name):

    # Load data file
    with open(data_filename) as data_file:
        data = json.load(data_file)

    # Create project
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('customer_name') == customer_name
    common_tests(data, result)
