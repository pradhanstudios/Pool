import numpy as np

BALL_RADIUS = 100


class Ball:
    def __init__(self):
        self.pos = np.zeros(2, dtype=float)
        self.vel = np.zeros(2, dtype=float)

    def apply_force(self, force, time=1):
        # f = ma, v = u + at -> v = u + (f/m)*t
        self.velocity += (force / config.ball_mass) * time

    def set_velocity(self, new_velocity):
        self.velocity = np.array(new_velocity, dtype=float)

    def move_to(self, pos):
        self.pos = np.array(pos, dtype=float)

    def update(self, *args):
        self.velocity *= config.friction_coeff
        self.pos += self.velocity

        if np.hypot(*self.velocity) < config.friction_threshold:
            self.velocity = np.zeros(2)
