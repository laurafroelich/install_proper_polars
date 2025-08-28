import cpuinfo
from setuptools import setup


def get_polars():
    info = cpuinfo.get_cpu_info()
    if info["arch"] == "X86_64":
        polars_package = "polars-lts-cpu"
    else:
        if {"avx2", "bmi2", "movbe"} <= set(info["flags"]):
            polars_package = "polars"
        else:
            polars_package = "polars-lts-cpu"
    print(f'determined {polars_package}')
    return polars_package



setup(
    name='install-proper-polars',
    version='0.1',
    packages=[],
    description='Empty package that will check available CPU flags, and install polars or polars-lts-cpu as appropriate.',
    url="https://github.com/michalsta/install_proper_polars",
    author="Michał Startek",
    install_requires=[get_polars()],
    )
