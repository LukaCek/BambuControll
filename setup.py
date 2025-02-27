from setuptools import setup, find_packages

DESCRIPTION = 'Python package for controlling Bambu Lab 3D printers (P1 and A1 series) via MQTT'
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="BambuControll",
    version='0.0.2',
    author="CekLuka",
    author_email="jaz@cekluka.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["paho-mqtt"],
    keywords=['python', 'Bambu', '3D printer', 'MQTT', 'Printer avtomation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)