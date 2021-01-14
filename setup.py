from setuptools import setup, find_packages


setup(
    name="Wicked Flicks",
    author="Yves Thommes",
    description="Wicked Video Library",
    long_description=open("README.md").read(),
    author_email="me@wickeddoc.com",
    provides=['wickedflicks'],
    include_package_data=True,
    install_requires=[
        'Django',
        'psycopg2-binary',
        'django-extensions',
        'django-admin-tools',
        'django-admin-list-filter-dropdown',
        'django-multiselectfield',
        'django-versatileimagefield',
        'python-dateutil',
        'requests',
    ],
    extras_require={
        'doc': [
            'sphinx',
            'sphinx-rtd-theme',
        ],
        'dev': [
            'django-debug-toolbar',
            'sqlparse',
            'Werkzeug',
        ],
        'test': [
            'pylint',
            'pylint-django',
            'flake8',
            'faker',
            'pytest',
            'pytest-django',
            'pytest-coverage',
            'pytest-xdist',
            'mock',
            'pylint-plugin-utils',
        ]
    },
    entry_points={
        'console_scripts': [
            'manage=wickedflicks.manage:main'
        ]
    },
    packages=find_packages(exclude=["tests.*", "tests", "docs"]),
)
