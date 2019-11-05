from setuptools import setup

from pathlib import Path

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


setup(
    name="tfpy",
    version="1.1.0",
    author="Marius Stanca",
    author_email=["me@mariuss.me"],
    url="http://mariuss.me",
    license="MIT",
    description="Checks and apply changes",
    packages=["tfpy"],
    long_description=get_long_description(),
    include_package_data=True,
    package_data={"": ["README.md"]},
    install_requires=["click==7.0", "subprocrunner==0.15.6", "termcolor==1.1.0"],
    extras_require={"click": ["click==7.0"]},
    classifiers=[
        "Environment :: Tools Environment",
        "Intended Audience :: Operations",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.x",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points="""
        [console_scripts]
        tfpy=tfpy.main:cli
    """,
)
