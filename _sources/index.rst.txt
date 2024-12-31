DexRobot Python SDK Documentation
==================================

A software development kit for the control and simulation of the DexRobot dexterous hands.

.. toctree::
   :maxdepth: 2
   :caption: Contents

.. toctree::
   :maxdepth: 2
   :caption: Component Documentation

   components/pyzlg_dexhand/index
   components/dexrobot_urdf/index
   components/ros_compat/index

Getting Started
----------------

1. Make sure you have Git LFS installed::

    sudo apt install git-lfs      # For Ubuntu, for example
    git lfs install

2. Clone the repository::

    git clone --recursive https://gitee.com/DexRobot/dexrobot_python_sdk.git

.. note::
   Make sure you have the ``--recursive`` flag turned on, so that all the submodules can be loaded. Alternatively, you can clone the submodules you need individually.

Project Components
-------------------

pyzlg_dexhand
~~~~~~~~~~~~~~
Low-level hardware interface and control library for the DexHand robotic system.

* Hardware communication via USB-CAN interface
* Protocol implementation for hand control
* ROS integration examples
* Visualization tools
* Comprehensive testing suite

dexrobot_kinematics
~~~~~~~~~~~~~~~~~~~
Kinematics library for robotic hand systems.

* Forward and inverse kinematics for hand configurations
* Support for both left and right hand variants
* Utilities for transformation and visualization
* Type-safe implementation with comprehensive testing

dexrobot_isaac
~~~~~~~~~~~~~~
Isaac Sim integration and simulation environment.

* Complex scene creation and simulation
* Integration with OpenAI Gym-style environments
* Support for various manipulation tasks
* Reinforcement learning infrastructure
* Pre-built assets and environments:
    * Robotic hand models
    * Furniture and object models
    * Scene compositions
    * Training configurations

dexrobot_urdf
~~~~~~~~~~~~~~
URDF (Unified Robot Description Format) models and utilities.

* Complete URDF descriptions for DexHand
* Mesh files for visualization and collision
* Utilities for URDF manipulation and analysis
* Both detailed and simplified hand models
* CAD exports in STEP format

dexrobot_mujoco
~~~~~~~~~~~~~~~~
MuJoCo simulation environment and utilities.

* MuJoCo XML models for the DexHand
* Scene creation tools
* Real-time visualization
* Physics-based simulation
* Integration with ROS
* Rich set of demo environments and furniture models

ros_compat
~~~~~~~~~~~
ROS compatibility layer for platform-independent development.

* Abstract interface for ROS functionality
* Logging utilities
* Time handling
* Node implementation

Installation
-------------

Please refer to the guides in the individual submodules.

Dependencies
-------------

* Python 3.6+
* ROS (optional, for ROS integration)
* MuJoCo (for physics simulation)
* Isaac Sim (for advanced simulation)
* USB-CAN adapter (for hardware control)

Indices and tables
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
