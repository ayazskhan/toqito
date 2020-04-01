"""Produces a Horodecki_state."""
from typing import List
import numpy as np


def horodecki(a_param: float, dim: List[int] = None) -> np.ndarray:
    r"""
    Produce a Horodecki state.

    Returns the Horodecki state in either :math:`(3 \otimes 3)`-dimensional
    space or :math:`(2 \otimes 4)`-dimensional space, depending on the
    dimensions in the 1-by-2 vector `dim`.

    The Horodecki state was introduced in [1] which serves as an example in
    :math:`\mathbb{C}^3 \otimes \mathbb{C}` or :math:`\mathbb{C}^2 \otimes
    \mathbb{C}^4` of an entangled state that is positive under partial
    transpose (PPT). The state is PPT for all :math:`a \in [0, 1]` and
    separable only for `a_param = 0` or `a_param = 1`.

    These states have the following definitions:

    .. math::

        \begin{equation}
            \rho_a^{3 \otimes 3} = \frac{1}{8a + 1}
            \begin{pmatrix}
                a & 0 & 0 & 0 & a & 0 & 0 & 0 & a \\
                0 & a & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
                0 & 0 & a & 0 & 0 & 0 & 0 & 0 & 0 \\
                0 & 0 & 0 & a & 0 & 0 & 0 & 0 & 0 \\
                0 & 0 & 0 & 0 & a & 0 & 0 & 0 & 0 \\
                0 & 0 & 0 & 0 & 0 & a & 0 & 0 & 0 \\
                0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} 
                \left( 1 + a \right) & 0 & \frac{1}{2} \sqrt{1 - a^2} \\
                0 & 0 & 0 & 0 & 0 & 0 & 0 & a & 0 \\
                0 & 0 & 0 & 0 & 0 & 0 & \frac{1}{2} \sqrt{1 - a^2} & 0 
                & \frac{1}{2} \left(1 + a \right) \\
            \end{pmatrix}
        \end{equation}

    .. math::

        \begin{equation}
            \rho_a^{2 \otimes 4} = \frac{1}{7a + 1}
            \begin{pmatrix}
                a & 0 & 0 & 0 & 0 & a & 0 & 0  \\
                0 & a & 0 & 0 & 0 & 0 & a & 0 \\
                0 & 0 & a & 0 & 0 & 0 & 0 & a  \\
                0 & 0 & 0 & a & 0 & 0 & 0 & 0  \\
                0 & 0 & 0 & 0 & \frac{1}{2} \left(1 + a\right) & 0 & 0
                & \frac{1}{2}\sqrt{1 -a^2} \\
                a & 0 & 0 & 0 & 0 & a & 0 & 0 \\
                0 & a & 0 & 0 & 0 & 0 & a & 0 \\
                0 & 0 & a & 0 & \frac{1}{2}\sqrt{1 - a^2} & 0 & 0
                & \frac{1}{2}\left(1 +a \right)
            \end{pmatrix}
        \end{equation}

    Note: Refer to [2] (specifically equations (1) and (2)) for more information
    on this state and its properties. The 3x3 Horodecki state is defined
    explicitly in Section 4.1 of [1] and the 2x4 Horodecki state is defined
    explicitly in Section 4.2 of [1].

    References:
    [1] P. Horodecki.
        Separability criterion and inseparable mixed states with positive
        partial transpose.
        arXiv: 970.3004.

    [2] K. Chruscinski.
        On the symmetry of the seminal Horodecki state.
        arXiv: 1009.4385.
    """
    if a_param < 0 or a_param > 1:
        raise ValueError("Invalid: Argument A_PARAM must be in the interval " "[0, 1].")

    if dim is None:
        dim = np.array([3, 3])

    if np.array_equal(dim, np.array([3, 3])):
        n_a_param = 1 / (8 * a_param + 1)
        b_param = (1 + a_param) / 2
        c_param = np.sqrt(1 - a_param ** 2) / 2

        horo_state = n_a_param * np.array(
            [
                [a_param, 0, 0, 0, a_param, 0, 0, 0, a_param],
                [0, a_param, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, a_param, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, a_param, 0, 0, 0, 0, 0],
                [a_param, 0, 0, 0, a_param, 0, 0, 0, a_param],
                [0, 0, 0, 0, 0, a_param, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, b_param, 0, c_param],
                [0, 0, 0, 0, 0, 0, 0, a_param, 0],
                [a_param, 0, 0, 0, a_param, 0, c_param, 0, b_param],
            ]
        )
        return horo_state

    if np.array_equal(dim, np.array([2, 4])):
        n_a_param = 1 / (7 * a_param + 1)
        b_param = (1 + a_param) / 2
        c_param = np.sqrt(1 - a_param ** 2) / 2

        horo_state = n_a_param * np.array(
            [
                [a_param, 0, 0, 0, 0, a_param, 0, 0],
                [0, a_param, 0, 0, 0, 0, a_param, 0],
                [0, 0, a_param, 0, 0, 0, 0, a_param],
                [0, 0, 0, a_param, 0, 0, 0, 0],
                [0, 0, 0, 0, b_param, 0, 0, c_param],
                [a_param, 0, 0, 0, 0, a_param, 0, 0],
                [0, a_param, 0, 0, 0, 0, a_param, 0],
                [0, 0, a_param, 0, c_param, 0, 0, b_param],
            ]
        )
        return horo_state
    raise ValueError("InvalidDim: DIM must be one of [3, 3], or [2, 4].")
