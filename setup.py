#!env python3
import setuptools, os

with open("README.md", "r") as fd:
    long_description = fd.read()

version = None
with open(os.path.join("capyt", "VERSION")) as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="capyt",
    version=version,
    author="Luis Batalha",
    author_email="author@example.com",
    description="A python3 CLI utility to interface with cpy.pt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lbatalha/capyt",
    packages=setuptools.find_packages(),
	include_package_data=True,
	license="MIT",
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Natural Language :: English",
		"Topic :: Utilities",
    ],
	install_requires=[
		"requests"
	],
	entry_points = {
		'console_scripts': [
			'capyt=capyt.capyt:main',
		],
	},

)
