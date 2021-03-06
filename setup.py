import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="env_canada",
    version="0.0.37",
    author="Michael Davie",
    author_email="michael.davie@gmail.com",
    description="A package to access meteorological data from Environment Canada",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaeldavie/env_canada",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['requests',
                      'geopy',
                      'imageio',
                      'numpy',
                      'python-dateutil',
                      'requests',
                      'requests_futures',
                      'ratelimit',
                      ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)