import matplotlib
import matplotlib.pyplot as plt

from rw_generator import RWGenerator
from rw_settings import Walk
from rw_graph_properties import Graph, Points, Line


class RandomWalk:
    """Plot a customizable random walk graph."""

    def __init__(self):
        """Initialize random walk graph settings and properties."""
        self.walk = Walk()

        self.graph = Graph()
        self.points = Points()
        self.line = Line()

        # Initialize with None
        self.fig = None
        self.ax = None

    def set_steps(self, amount: int) -> None:
        """Set number of points (steps) to generate."""
        self.points.amount = amount

    def build(self) -> tuple[matplotlib.pyplot.Figure, matplotlib.pyplot.Axes]:
        """Build random walk graph."""
        rwg = RWGenerator()
        rwg.set(
            self.walk.steps,
            self.walk.xdistances,
            self.walk.ydistances,
            self.walk.xdirections,
            self.walk.ydirections,
        )
        rwg.fill_walk()

        if self.graph.type.lower() not in ["scatter", "line"]:
            raise ValueError(f"Invalid graph type '{self.graph.type}'. "
                             f"Use 'scatter' or 'line'")

        # Plot points
        plt.style.use(self.graph.style)
        fig, ax = plt.subplots(figsize=self.graph.figsize, dpi=self.graph.dpi)
        point_numbers = range(rwg.steps)

        # Scatter graph
        if self.graph.type.lower() == "scatter":
            ax.scatter(
                rwg.x_values,
                rwg.y_values,
                alpha=self.points.alpha,
                c=point_numbers if self.points.colorful else None,
                cmap=self.points.colormap,
                edgecolors=self.points.edgecolors,
                s=self.points.size
            )

        # Line graph
        else:
            ax.plot(
                rwg.x_values,
                rwg.y_values,
                color=self.line.color,
                linewidth=self.line.linewidth,
                linestyle=self.line.linestyle,
                alpha=self.line.alpha,
                marker=self.line.marker,
                markersize=self.line.markersize,
            )

        # Tight layout
        if self.graph.tight_layout:
            plt.tight_layout(pad=0)

        # Set aspect ratio
        if self.graph.equal_aspect_ratio:
            ax.set_aspect("equal")

        # Hide axes
        if self.graph.hide_axes:
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

        # Remove axes
        if self.graph.remove_axes:
            plt.axis("off")

        if self.points.diff_first_point:
            # Emphasize first and last points
            ax.scatter(
                0,
                0,
                c=self.points.first_point_color,
                edgecolors=self.points.first_point_edgecolors,
                s=self.points.first_point_size,
            )
            ax.scatter(
                rwg.x_values[-1],
                rwg.y_values[-1],
                c=self.points.last_point_color,
                edgecolors=self.points.last_point_edgecolors,
                s=self.points.last_point_size,
            )

        self.fig, self.ax = (fig, ax)
        return self.fig, self.ax

    @staticmethod
    def show() -> None:
        """Show the random walk graph."""
        plt.show()

    @staticmethod
    def close() -> None:
        """Close the random walk graph."""
        plt.close()
