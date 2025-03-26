# main.py
from brownian_motion import simulate_brownian_motion

def main():
    # Run simulation with default parameters
    robot = simulate_brownian_motion(
        steps=2000,
        filename="brownian_motion_sample.gif"
    )
    
    # Print some statistics
    print(f"Start position: ({robot.arena_size/2}, {robot.arena_size/2})")
    print(f"Final position: {robot.get_position()}")
    print(f"Total steps: {len(robot.x_history)}")
    print("GIF animation saved as 'brownian_motion_sample.gif'")

if __name__ == "__main__":
    main()