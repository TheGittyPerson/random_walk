from random import choice


class RWGenerator:
    """Generate random walk graph point values (locations)."""

    def __init__(self):
        """A class to generate random walks."""
        # Start walk at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

        # Customizable walk behaviour values
        self.steps = 50_000
        self.xdistances = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.ydistances = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.xdirections = [-1, 1]
        self.ydirections = [-1, 1]

    def fill_walk(self) -> None:
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.steps:

            # Decide which direction to go, and how far to go
            x_direction = choice(self.xdirections)  # Left or right
            y_direction = choice(self.ydirections)  # Up or down
            x_distance = choice(self.xdistances)
            y_distance = choice(self.ydistances)
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def set(self,
            steps: int,
            xdistances: list[float],
            ydistances: list[float],
            xdirections: list[int],
            ydirections: list[int]) -> None:
        self.steps = steps
        self.xdistances = xdistances
        self.ydistances = ydistances
        self.xdirections = xdirections
        self.ydirections = ydirections
