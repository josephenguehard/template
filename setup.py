from setuptools import setup, find_packages


version = {}
with open(
        "{name}/__version__.py".format(name={{ cookiecutter.repo_name }})
) as fp:
    exec(fp.read(), version)


with open("README.md") as f:
    readme = f.read()


setup(
    name={{ cookiecutter.project_name }},
    version=version["__version__"],
    description={{ cookiecutter.project_name }},
    long_description=readme,
    author={{ cookiecutter.author_name }},
    author_email={{ cookiecutter.author_email }},
    url="https://github.com/babylonhealth/{name}".format(
        name={{ cookiecutter.project_name }}
    ),
    python_requires=">=3.7, <3.11",
    install_requires=[
        "torch==1.12.0",
        "numpy",
        "pandas",
        "scikit-learn",
    ],
    dependency_links=[],
    include_package_data=True,
    packages=find_packages(exclude=("tests", "docs")),
)
