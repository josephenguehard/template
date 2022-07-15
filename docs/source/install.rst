========================================
Installation
========================================


PIP
========================================

{{ cookiecutter.project_name }} can be installed with pip:

.. code-block:: console

    pip install {{ cookiecutter.project_name }}


From source
========================================

Conda
----------------------------------------

.. code-block:: console

    git clone git@github.com:babylonhealth/{{ cookiecutter.project_name }}.git
    cd {{ cookiecutter.project_name }}
    conda env create
    source activate {{ cookiecutter.repo_name }}
    pip install --no-deps .


Pip
----------------------------------------

.. code-block:: console

    git clone git@github.com:babylonhealth/{{ cookiecutter.project_name }}.git
    cd {{ cookiecutter.project_name }}
    pip install .


Docker
----------------------------------------

.. code-block:: console

    git clone git@github.com:babylonhealth/{{ cookiecutter.project_name }}.git
    cd {{ cookiecutter.project_name }}
    docker build -t {your_image} .
    docker push {your_image}