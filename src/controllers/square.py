import numpy as np

class Triangle:
    def __init__(vertices,color):
        self._vertices = np.array(triangle_vertices, dtype=np.float32)
        self._colors = np.array(color*4, dtype=np.float32)

    def get_vertices(self):
        return self._vertices

    def get_colors(self):
        return self._colors
