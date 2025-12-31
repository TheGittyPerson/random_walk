from random_walk import RandomWalk

if __name__ == '__main__':
    rw = RandomWalk()

    rw.walk.set(
        steps=80_000,
        xdistances=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        ydistances=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    )
    rw.graph.set(
        type_='scatter',
        figsize=(10, 6),
        dpi=128,
        style='seaborn-v0_8',
        hide_axes=True,
    )
    rw.points.set(
        alpha=1,
        size=1,
        colorful=True,
        colormap='plasma',
    )
    rw.line.set(
        linewidth=0.5
    )

    while True:
        rw.build()
        rw.show()
