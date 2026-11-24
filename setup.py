from setuptools import find_packages, setup

# optionally depends on pybase64

setup(
    name="sipyco",
    version="1.11",
    author="M-Labs",
    url="https://m-labs.hk/artiq",
    description="Simple Python communications",
    license="LGPLv3+",
    install_requires=[
        "numpy",
        "msgpack",
        "msgpack-numpy",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sipyco_rpctool = sipyco.sipyco_rpctool:main",
        ]
    },
)
