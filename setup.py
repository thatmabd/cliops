from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = (this_directory / "requirements.txt").read_text().strip().split('\n')

setup(
    name='cliops',
    version='4.4.4',
    author='cliops by mabd',
    author_email='iammabd@substack.com',
    description='Advanced CLI tool for structured, pattern-based prompt optimization and state management',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cliops/cliops',
    project_urls={
        'Bug Reports': 'https://github.com/cliops/cliops/issues',
        'Source': 'https://github.com/cliops/cliops',
        'Documentation': 'https://cliops.readthedocs.io',
    },
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
        ],
        'test': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'cliops=cliops.cli:main',
        ],
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Linguistic',
        'Environment :: Console',
    ],
    keywords='cli prompt optimization ai llm prompt-engineering patterns state-management',
    python_requires='>=3.8',
    zip_safe=False,
)
