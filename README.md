# DexRobot Python SDK

A comprehensive software development kit for robotic hand control, simulation, and manipulation. This project provides a complete stack for working with dexterous robotic hands, from low-level hardware control to high-level simulation and planning.

## Project Components

### 1. pyzlg_dexhand
Low-level hardware interface and control library for the DexHand robotic system.
- Hardware communication via USB-CAN interface
- Protocol implementation for hand control
- ROS integration examples
- Visualization tools
- Comprehensive testing suite

### 2. dexrobot_kinematics
Kinematics library for robotic hand systems.
- Forward and inverse kinematics for hand configurations
- Support for both left and right hand variants
- Utilities for transformation and visualization
- Type-safe implementation with comprehensive testing

### 3. dexrobot_isaac
Isaac Sim integration and simulation environment.
- Complex scene creation and simulation
- Integration with OpenAI Gym-style environments
- Support for various manipulation tasks
- Reinforcement learning infrastructure
- Pre-built assets and environments:
  - Robotic hand models
  - Furniture and object models
  - Scene compositions
  - Training configurations

### 4. dexrobot_urdf
URDF (Unified Robot Description Format) models and utilities.
- Complete URDF descriptions for DexHand
- Mesh files for visualization and collision
- Utilities for URDF manipulation and analysis
- Both detailed and simplified hand models
- CAD exports in STEP format

### 5. dexrobot_mujoco
MuJoCo simulation environment and utilities.
- MuJoCo XML models for the DexHand
- Scene creation tools
- Real-time visualization
- Physics-based simulation
- Integration with ROS
- Rich set of demo environments and furniture models

### 6. ros_compat
ROS compatibility layer for platform-independent development.
- Abstract interface for ROS functionality
- Logging utilities
- Time handling
- Node implementation

## Installation

Each component can be installed independently using pip:

```bash
# Install individual components
pip install ./pyzlg_dexhand
pip install ./dexrobot_kinematics
pip install ./dexrobot_isaac
pip install ./dexrobot_urdf
pip install ./dexrobot_mujoco
pip install ./ros_compat
```

## Dependencies

- Python 3.6+
- ROS (optional, for ROS integration)
- MuJoCo (for physics simulation)
- Isaac Sim (for advanced simulation)
- USB-CAN adapter (for hardware control)

## Documentation

Each component contains its own documentation in the `docs` directory. The documentation can be built using Sphinx:

```bash
cd <component_directory>
sphinx-build docs docs/_build
```

## License

Each component may have its own license. Please refer to the LICENSE file in each component directory.

## Project Structure

```
dexrobot_python_sdk/
├── pyzlg_dexhand/      # Hardware interface
├── dexrobot_kinematics/ # Kinematics library
├── dexrobot_isaac/     # Isaac Sim integration
├── dexrobot_urdf/      # Robot description files
├── dexrobot_mujoco/    # MuJoCo simulation
└── ros_compat/         # ROS compatibility layer
```

## Contributing

Please refer to individual component READMEs for specific contribution guidelines.

## Support

For issues and support:
- Hardware issues: Check pyzlg_dexhand documentation
- Simulation issues: Refer to dexrobot_isaac or dexrobot_mujoco
- Kinematics questions: See dexrobot_kinematics documentation
