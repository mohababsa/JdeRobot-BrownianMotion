# brownian_motion.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

class BrownianRobot:
    def __init__(self, arena_size=10.0, speed=0.1, dt=0.1):
        """Initialize robot with parameters"""
        self.arena_size = arena_size
        self.speed = speed
        self.dt = dt
        
        self.x = arena_size / 2
        self.y = arena_size / 2
        self.angle = random.uniform(0, 2 * np.pi)
        
        self.x_history = [self.x]
        self.y_history = [self.y]
        self.speed_history = [speed]
        
    def move(self):
        """Move with rotation only on boundary collision"""
        speed_variation = np.random.normal(1, 0.1) * self.speed
        current_speed = max(0.05, min(self.speed * 2, speed_variation))
        
        dx = current_speed * np.cos(self.angle) * self.dt
        dy = current_speed * np.sin(self.angle) * self.dt
        new_x = self.x + dx
        new_y = self.y + dy
        
        collision = False
        if new_x <= 0 or new_x >= self.arena_size:
            self.angle = random.uniform(0, 2 * np.pi)
            collision = True
        if new_y <= 0 or new_y >= self.arena_size:
            self.angle = random.uniform(0, 2 * np.pi)
            collision = True
            
        if collision:
            self.x = np.clip(new_x, 0, self.arena_size)
            self.y = np.clip(new_y, 0, self.arena_size)
        else:
            self.x = new_x
            self.y = new_y
        
        self.x_history.append(self.x)
        self.y_history.append(self.y)
        self.speed_history.append(current_speed)

    def get_position(self):
        """Return current position"""
        return self.x, self.y

    def get_stats(self):
        """Return movement statistics"""
        total_distance = sum(
            np.sqrt((self.x_history[i+1] - self.x_history[i])**2 + 
                   (self.y_history[i+1] - self.y_history[i])**2)
            for i in range(len(self.x_history)-1)
        )
        return {
            'total_distance': total_distance,
            'avg_speed': np.mean(self.speed_history),
            'collisions': sum(1 for i in range(len(self.x_history))
                            if (self.x_history[i] <= 0 or 
                                self.x_history[i] >= self.arena_size or
                                self.y_history[i] <= 0 or 
                                self.y_history[i] >= self.arena_size))
        }

def simulate_brownian_motion(steps=1000, filename="brownian_motion_styled.gif"):
    """Simulation with styled boundaries"""
    robot = BrownianRobot()
    
    fig = plt.figure(figsize=(10, 8), facecolor='#f0f0f0')
    gs = fig.add_gridspec(2, 2, height_ratios=[3, 1])
    
    ax = fig.add_subplot(gs[0, :])
    ax.set_xlim(-0.5, robot.arena_size + 0.5)
    ax.set_ylim(-0.5, robot.arena_size + 0.5)
    ax.set_aspect('equal')
    ax.set_title("Brownian Motion Simulation", 
                 fontsize=16, 
                 fontweight='bold', 
                 pad=15, 
                 color='#333333')
    ax.set_xlabel("X Position", fontsize=12, labelpad=10)
    ax.set_ylabel("Y Position", fontsize=12, labelpad=10)
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#fafafa')
    
    # Add bold colored boundaries
    boundary_color = '#00008B'  # Dark blue
    boundary_width = 2.5
    ax.plot([0, robot.arena_size], [0, 0], color=boundary_color, 
            lw=boundary_width, solid_capstyle='round')  # Bottom
    ax.plot([0, robot.arena_size], [robot.arena_size, robot.arena_size], 
            color=boundary_color, lw=boundary_width, solid_capstyle='round')  # Top
    ax.plot([0, 0], [0, robot.arena_size], color=boundary_color, 
            lw=boundary_width, solid_capstyle='round')  # Left
    ax.plot([robot.arena_size, robot.arena_size], [0, robot.arena_size], 
            color=boundary_color, lw=boundary_width, solid_capstyle='round')  # Right
    
    ax_speed = fig.add_subplot(gs[1, :])
    ax_speed.set_xlim(0, steps)
    ax_speed.set_ylim(0, robot.speed * 2.5)
    ax_speed.set_title("Speed Over Time", 
                      fontsize=14, 
                      fontweight='bold', 
                      pad=15, 
                      color='#333333')
    ax_speed.set_xlabel("Time Step", fontsize=12, labelpad=10)
    ax_speed.set_ylabel("Speed", fontsize=12, labelpad=10)
    ax_speed.set_facecolor('#fafafa')
    ax_speed.grid(True, alpha=0.3)
    
    line, = ax.plot([], [], 'b-', lw=1.5, alpha=0.6, label='Path')
    point, = ax.plot([], [], 'ro', markersize=8, label='Robot')
    speed_line, = ax_speed.plot([], [], 'g-', lw=1, label='Speed')
    
    ax.legend(loc='upper right', 
             fontsize=10, 
             frameon=True, 
             facecolor='white', 
             edgecolor='black')
    
    stats_text = ax.text(0.02, 0.95, '', 
                        transform=ax.transAxes,
                        fontsize=11,
                        fontfamily='monospace',
                        bbox=dict(facecolor='white', 
                                edgecolor='black', 
                                alpha=0.9, 
                                boxstyle='round,pad=0.5'),
                        verticalalignment='top')
    
    def update(frame):
        robot.move()
        x, y = robot.get_position()
        
        line.set_data(robot.x_history, robot.y_history)
        point.set_data([x], [y])
        speed_line.set_data(range(len(robot.speed_history)), robot.speed_history)
        
        stats = robot.get_stats()
        stats_text.set_text(
            f'Distance: {stats["total_distance"]:.2f}\n'
            f'Avg Speed: {stats["avg_speed"]:.3f}\n'
            f'Collisions: {stats["collisions"]}'
        )
        
        return line, point, speed_line, stats_text
    
    anim = FuncAnimation(fig, update, frames=steps,
                        init_func=lambda: [line, point, speed_line, stats_text],
                        interval=20, blit=True)
    
    anim.save(filename, writer='pillow', fps=30, dpi=100)
    plt.close()
    
    return robot