import {{ cookiecutter.repo_name }}


def test_init():
    assert isinstance({{ cookiecutter.repo_name }}.__version__, str)
