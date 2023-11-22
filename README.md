# Template Project
A template project to show how to set up and use automated testing in Python

![Component 1](https://github.com/memo26167/template-project/actions/workflows/tests_component1.yml/badge.svg)
![Component 2](https://github.com/memo26167/template-project/actions/workflows/tests_component2.yml/badge.svg)
![Component 3](https://github.com/memo26167/template-project/actions/workflows/tests_component3.yml/badge.svg)
![Component 4](https://github.com/memo26167/template-project/actions/workflows/tests_component4.yml/badge.svg)

```bash
├── components
│   ├── component1
│   │   ├── component1
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── pyproject.toml
│   │   └── tests
│   │       └── test_component1.py
│   ├── component2
│   │   ├── component2
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── pyproject.toml
│   │   └── tests
│   │       └── test_component2.py
│   ├── component3
│   │   ├── component3
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── pyproject.toml
│   │   └── tests
│   │       ├── conftest.py
│   │       ├── test_class_parametrization.py
│   │       ├── test_component3.py
│   │       └── test_inheritance.py
│   └── component4
│       ├── component4
│       │   ├── __init__.py
│       │   └── main.py
│       ├── pyproject.toml
│       └── tests
│           ├── conftest.py
│           └── test_component4.py
├── LICENSE
├── pyproject.toml
├── README.md
├── run_tox.sh
├── test_requirements.txt
└── tox.ini
```
To use this project, you have to:
1) Have python>=3.10
2) Have git
3) Install tox (pip install tox)
4) Download the repository
5) Config githooks with:
```bash
git config --local core.hooksPath .githooks/
```
6) Enable execution of githooks:
```bash
chmod ug+x .githooks/*
```
If you want to run tox without needing to do a commit, you can execute:
```shell
tox -c tox.ini --root components/component1/
```
