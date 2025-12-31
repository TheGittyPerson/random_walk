class Walk:
    """Manage random walk step behavior.

    Attributes:
        steps (int, optional):
            Number of points (steps) to generate.

        xdistances (list[int], optional):
            List of possible step distances to randomly choose from
            for movement along the x-axis.
            If None, the default x-distance list is used.

        ydistances (list[int], optional):
            List of possible step distances to randomly choose from
            for movement along the y-axis.
            If None, the default y-distance list is used.

        xdirections (list[int], optional):
            List of multipliers used to determine movement direction
            along the x-axis (e.g. [-1, 1]).
            If None, the default x-direction choices are used.

        ydirections (list[int], optional):
            List of multipliers used to determine movement direction
            along the y-axis (e.g. [-1, 1]).
            If None, the default y-direction choices are used.

    Note:
        These values are intended to be used with random selection
        when calculating each step of the walk.
            """

    def __init__(self):
        """Initialize walk behavior."""
        self.steps: int = 50_000
        self.xdistances: list[float] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.ydistances: list[float] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.xdirections: list[int] = [-1, 1]
        self.ydirections: list[int] = [-1, 1]

    def set(self,
            steps: int = None,
            xdistances: list[float] = None,
            ydistances: list[float] = None,
            xdirections: list[int] = None,
            ydirections: list[int] = None) -> None:
        """Set walk behavior.

        Arguments:
            steps (int, optional):
                Number of points (steps) to generate.

            xdistances (list[float], optional):
                List of possible step distances to randomly choose from
                for movement along the x-axis.
                If None, the default x-distance list is used.

            ydistances (list[float], optional):
                List of possible step distances to randomly choose from
                for movement along the y-axis.
                If None, the default y-distance list is used.

            xdirections (list[int], optional):
                List of multipliers used to determine movement direction
                along the x-axis (e.g. [-1, 1]).
                If None, the default x-direction choices are used.

            ydirections (list[int], optional):
                List of multipliers used to determine movement direction
                along the y-axis (e.g. [-1, 1]).
                If None, the default y-direction choices are used.

        Note:
            These values are intended to be used with random selection
            when calculating each step of the walk.
        """
        if steps is not None:
            self.steps = steps

        if xdistances is not None:
            self.xdistances = xdistances

        if ydistances is not None:
            self.ydistances = ydistances

        if xdirections is not None:
            self.xdirections = xdirections

        if ydirections is not None:
            self.ydirections = ydirections
