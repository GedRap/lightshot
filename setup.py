from setuptools import setup

setup(
    name='LightShot',
    version='1.0',
    long_description="Lightweight RESTful API for taking screenshots of web sites",
    packages=['lightshot'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Ghost.py', 'boto']
)