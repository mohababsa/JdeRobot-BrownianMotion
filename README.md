# GSoC 2025 - JdeRobot Python Challenge: Brownian Motion

## Overview
This project implements a Brownian Motion simulation for a robot as part of the GSoC 2025 application for JdeRobot. The robot moves in a square arena, starting from the center, and rotates randomly upon collision with boundaries, mimicking Brownian motion behavior.

## Implementation Details
- **Language**: Python 3
- **Libraries**: 
  - Python Standard Library
  - NumPy (for calculations)
  - Matplotlib (for visualization)
- **Structure**: Implemented as a Python module (`brownian_motion.py`)
- **Features**:
  - Robot starts at the center of a square arena
  - Moves straight until hitting a boundary
  - Rotates randomly on collision
  - Tracks path, speed, and collision statistics
  - Visualized with styled boundaries and real-time stats

## How to Run
1. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```

2. Run the simulation:
   ```bash
   python main.py
   ```

3. Output: Generates `brownian_motion_styled.gif`

## Results
The simulation produces a GIF showing the robot's Brownian motion:
![Brownian Motion Simulation](brownian_motion_styled.gif)

## Author
**Mohamed ABABSA** - GSoC 2025 Applicant
