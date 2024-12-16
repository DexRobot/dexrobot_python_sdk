from setuptools import setup, find_packages

setup(
    name="dexrobot_python_sdk",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
)
