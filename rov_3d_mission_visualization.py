import numpy as np
import plotly.graph_objects as go

points = 200

x = np.cumsum(np.random.normal(0.5, 0.2, points))
y = np.cumsum(np.random.normal(0.5, 0.2, points))
depth = np.abs(np.cumsum(np.random.normal(0.3, 0.1, points)))

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=-depth,
    mode='lines',
    line=dict(width=6, color=depth, colorscale='Viridis')
))

fig.update_layout(
    title="ROV Mission 3D Trajectory",
    scene=dict(
        xaxis_title="East-West Position",
        yaxis_title="North-South Position",
        zaxis_title="Depth (m)"
    )
)

fig.show()
