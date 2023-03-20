from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="ktbunya",
    version="0.1.0",
    author="zktuong",
    author_email="z.tuong@uq.edu.au",
    description="Simple scripts to help create an interactive session to run jupyter notebooks using UQ's Bunya/Wiener compute.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zktuong/ktbunya/",
    packages=find_packages(),
    setup_requires=["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.0"],
    package_data={"ktbunya": ["bin/jpynb", "bin/ixcpu", "bin/ixgpu"]},
    data_files=[("bin", ["bin/jpynb", "bin/ixcpu", "bin/ixgpu"])],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
)
