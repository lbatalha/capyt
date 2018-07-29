import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = None
with open(os.path.join("capyt", "VERSION")) as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="capy",
    version=version,
    author="Luis Batalha",
    author_email="author@example.com",
    description="A python3 CLI utility to interface with cpy.pt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lbatalha/capyt",
    packages=setuptools.find_packages(),
	include_package_data=True
	classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
