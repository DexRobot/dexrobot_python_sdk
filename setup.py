from setuptools import setup, find_packages

setup(
    name="dexrobot_python_sdk",
    version="0.1.0",
    description="A comprehensive SDK for robotic hand control, simulation, and manipulation",
    author="DexRobot",
    author_email="contact@dexrobot.com",
    packages=find_packages(),
    install_requires=[], 
    extras_require={
        'docs': [
            'sphinx>=8.1.3',
            'sphinx-rtd-theme>=1.3.0',
            'sphinx-autodoc-typehints',
        ],
    },
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Robotics',
    ],
)