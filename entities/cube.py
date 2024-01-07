import numpy as np


class Cube:
    vertices = np.array([
        # Position          # Color
        -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,  # Vertex 1
        0.5, -0.5, -0.5, 0.0, 1.0, 0.0,  # Vertex 2
        0.5, 0.5, -0.5, 0.0, 0.0, 1.0,  # Vertex 3
        -0.5, 0.5, -0.5, 1.0, 1.0, 0.0,  # Vertex 4
        -0.5, -0.5, 0.5, 1.0, 0.0, 1.0,  # Vertex 5
        0.5, -0.5, 0.5, 0.0, 1.0, 1.0,  # Vertex 6
        0.5, 0.5, 0.5, 1.0, 1.0, 1.0,  # Vertex 7
        -0.5, 0.5, 0.5, 0.5, 0.5, 0.5  # Vertex 8
    ], dtype=np.float32)

    indices = np.array([
        # Front face
        0, 1, 2,
        2, 3, 0,
        # Left face
        4, 0, 3,
        3, 7, 4,
        # Back face
        5, 4, 7,
        7, 6, 5,
        # Right face
        1, 5, 6,
        6, 2, 1,
        # Top face
        3, 2, 6,
        6, 7, 3,
        # Bottom face
        4, 5, 1,
        1, 0, 4
    ], dtype=np.uint32)
