from setuptools import setup, find_packages

DESCRIPTION = 'A package for controlling with Bambu 3D printer (P1 and A1 series)'
LONG_DESCRIPTION = 'A package for controlling with Bambu 3D printer (P1 and A1 series) using MQTT protocol'

# Setting up
setup(
    name="BambuControll",
    version='0.0.1',
    author="CekLuka",
    author_email="<jaz@cekluka.com>",
    description=DESCRIPTION,
    #long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["paho-mqtt"],
    keywords=['python', 'Bambu', '3D printer', 'MQTT'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)