class Graph:
    """Manage random walk graph properties.

    Resets to default values if no arguments are provided.

    Attributes:
        type (str):
            The type of graph to create. Either "scatter" or "line".

        figsize (tuple[float, float] | None):
            Size of the matplotlib figure in inches as (width, height).
            If None, matplotlib's default figure size is used.

        dpi (int | None):
            Dots per inch (resolution) of the figure.
            If None, matplotlib's default DPI is used.

        tight_layout (bool):
            If True, margins around the graph are minimized. If False,
            default margins used.

        equal_aspect_ratio (bool):
            If True, sets the axes aspect ratio to "equal", ensuring
            equal scaling on both axes so steps appear uniform.

        style (str):
            Matplotlib style sheet name applied before plotting.

        hide_axes (bool):
            If True, the axes will be hidden.

        remove_axes (bool):
            If True, the axes will be removed from the figure.
    """

    def __init__(self):
        """Initialize graph properties."""
        self.type: str = "scatter"
        self.figsize: tuple[float, float] | None = None
        self.dpi: int | None = None
        self.tight_layout: bool = True
        self.equal_aspect_ratio: bool = True
        self.style: str = "classic"
        self.hide_axes: bool = False
        self.remove_axes: bool = False

    def set(self,
            type_: str = "scatter",
            figsize: tuple[float, float] = None,
            dpi: int = None,
            tight_layout: bool = True,
            equal_aspect_ratio: bool = True,
            style: str = "classic",
            hide_axes: bool = False,
            remove_axes: bool = False) -> None:
        """Set graph properties.

        Arguments:
            type_ (str, optional):
                The type of graph to create. Must be either "scatter"
                or "line".

            figsize (tuple[float, float] | None, optional):
                Size of the matplotlib figure in inches as
                (width, height). If None, matplotlib's default figure
                size is used.

            dpi (int | None, optional):
                Dots per inch (resolution) of the figure.
                If None, matplotlib's default DPI is used.

            tight_layout (bool):
                If True, margins around the graph are minimized. If False,
                default margins used.

            equal_aspect_ratio (bool, optional):
                If True, sets the axes aspect ratio to "equal", ensuring
                equal scaling on both axes so steps appear uniform.

            style (str, optional):
                Matplotlib style sheet name applied before plotting.

            hide_axes (bool):
                If True, the axes will be hidden.

            remove_axes (bool, optional):
                If True, the axes will be removed from the figure. This also
                removes the background color if a graph style is set.

        Raises:
            ValueError:
                If `type_` is not "scatter" or "line".

        Note:
            See matplotlib documentation for more information on
            figure and axes properties.
        """
        if type_ not in ("scatter", "line"):
            raise ValueError(
                f"Invalid graph type '{type_}'. Use 'scatter' or 'line'."
            )

        self.type = type_
        self.figsize = figsize
        self.dpi = dpi
        self.tight_layout = tight_layout
        self.equal_aspect_ratio = equal_aspect_ratio
        self.style = style
        self.hide_axes = hide_axes
        self.remove_axes = remove_axes


class Points:
    """Manage random walk point properties.

    Resets to default values if no arguments are provided.

    Attributes:
        amount (int):
            Number of points to be plotted.

        size (float):
            Marker size for all points in the walk.

        alpha (float):
            Point transparency from 0.0 (fully transparent) to
            1.0 (fully opaque).

        colorful (bool):
            If True, points are colored based on their order using
            a colormap. If False, a single default color is used.

        colormap (str | None):
            Name of the colormap applied when `colorful` is True.
            If None, no colormap is applied.

        edgecolors (str):
            Edge color of each point marker.

        diff_first_point (bool):
            If True, the first point (origin) is emphasized using
            special styling.

        first_point_color (str):
            Fill color for the first point.

        first_point_edgecolors (str):
            Edge color for the first point.

        first_point_size (float):
            Marker size for the first point.

        diff_last_point (bool):
            If True, the last point in the walk is emphasized using
            special styling.

        last_point_color (str):
            Fill color for the last point.

        last_point_edgecolors (str):
            Edge color for the last point.

        last_point_size (float):
            Marker size for the last point.
    """

    def __init__(self):
        """Initialize point properties."""
        self.amount: int = 50_000

        self.size: float = 1.0
        self.alpha: float = 1.0
        self.colorful: bool = False
        self.colormap: str | None = None
        self.edgecolors: str = "none"

        self.diff_first_point: bool = False
        self.first_point_color: str = "none"
        self.first_point_edgecolors: str = "none"
        self.first_point_size: float = 10.0

        self.diff_last_point: bool = False
        self.last_point_color: str = "none"
        self.last_point_edgecolors: str = "none"
        self.last_point_size: float = 10.0

    def set(self,
            amount: int = 50_000,
            size: float = 1.0,
            alpha: float = 1.0,
            colorful: bool = False,
            colormap: str | None = None,
            edgecolors: str = "none",
            diff_first_point: bool = False,
            first_point_color: str = "none",
            first_point_edgecolors: str = "none",
            first_point_size: float = 10.0,
            diff_last_point: bool = False,
            last_point_color: str = "none",
            last_point_edgecolors: str = "none",
            last_point_size: float = 10.0) -> None:
        """Set point properties.

        Arguments:
            amount (int, optional):
                Number of points to be plotted.

            size (float, optional):
                Marker size for all points in the walk.

            alpha (float, optional):
                Point transparency from 0.0 (fully transparent) to
                1.0 (fully opaque).

            colorful (bool, optional):
                If True, points are colored based on their order using
                a colormap. If False, a single default color is used.

            colormap (str | None, optional):
                Name of the colormap applied when `colorful` is True.
                If None, no colormap is applied.

            edgecolors (str, optional):
                Edge color of each point marker.

            diff_first_point (bool, optional):
                If True, the first point (origin) is emphasized using
                special styling.

            first_point_color (str, optional):
                Fill color for the first point.

            first_point_edgecolors (str, optional):
                Edge color for the first point.

            first_point_size (float, optional):
                Marker size for the first point.

            diff_last_point (bool, optional):
                If True, the last point in the walk is emphasized using
                special styling.

            last_point_color (str, optional):
                Fill color for the last point.

            last_point_edgecolors (str, optional):
                Edge color for the last point.

            last_point_size (float, optional):
                Marker size for the last point.

        Note:
            See matplotlib documentation for more information on
            `matplotlib.axes.Axes.scatter` parameters.
        """
        self.amount = amount

        self.size = size
        self.alpha = alpha
        self.colorful = colorful
        self.colormap = colormap
        self.edgecolors = edgecolors

        self.diff_first_point = diff_first_point
        self.first_point_color = first_point_color
        self.first_point_edgecolors = first_point_edgecolors
        self.first_point_size = first_point_size

        self.diff_last_point = diff_last_point
        self.last_point_color = last_point_color
        self.last_point_edgecolors = last_point_edgecolors
        self.last_point_size = last_point_size


class Line:
    """Manage random walk line properties.

    Resets to default values if no arguments are provided.

    Attributes:
        color (str | None):
            Line color. If None, matplotlib's default color cycle
            is used.

        linewidth (float):
            Width of the line in points.

        linestyle (str):
            Line style (e.g. "-", "--", "-.", "solid", "dashed",
            "dashdot").

        alpha (float):
            Line transparency from 0.0 (fully transparent) to
            1.0 (fully opaque).

        marker (str | None):
            Marker style for points along the line (e.g. "o", ".", "^").
            If None, no markers are drawn.

        markersize (float):
            Size of markers if `marker` is not None.
    """

    def __init__(self):
        """Initialize line properties."""
        self.color: str | None = None
        self.linewidth: float = 1.0
        self.linestyle: str = "-"
        self.alpha: float = 1.0
        self.marker: str | None = None
        self.markersize: float = 6.0

    def set(self,
            color: str = None,
            linewidth: float = 1.0,
            linestyle: str = "-",
            alpha: float = 1.0,
            marker: str = None,
            markersize: float = 6.0) -> None:
        """Set line properties.

        Arguments:
            color (str | None, optional):
                Line color. If None, matplotlib's default color cycle
                is used.

            linewidth (float, optional):
                Width of the line in points.

            linestyle (str, optional):
                Line style (e.g. "-", "--", "-.", "solid", "dashed",
                "dashdot").

            alpha (float, optional):
                Line transparency from 0.0 (fully transparent) to
                1.0 (fully opaque).

            marker (str | None, optional):
                Marker style for points along the line.
                If None, no markers are drawn.

            markersize (float, optional):
                Size of markers if `marker` is not None.

        Note:
            See matplotlib documentation for more information on
            `matplotlib.axes.Axes.plot` parameters.
        """
        self.color = color
        self.linewidth = linewidth
        self.linestyle = linestyle
        self.alpha = alpha
        self.marker = marker
        self.markersize = markersize
