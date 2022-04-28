import numpy as np

def double_pen(y, t, L1, L2, m1, m2):
    """
    Using initial values for y0, return the first derivatives of
    y = theta1, z1, theta2, z2.

    Parameters
    ----------
    y : :class:`numpy.ndarray`
        Array of initial values of y

    L1 : :class:`int`
        Length of pendulum rod 1 (upper arm)

    L2 : :class:`int`
        Length of pendulum rod 2 (lower arm)

    t : :class:`int`
        Used by SciPy odeint, represents the individual times steps to use in
        pendulum simulation 

    m1 : :class:`int`
        mass of pendulum rod 1 (upper arm)

    m2 : :class:`int`
        mass of pendulum rod 2 (lower arm)

    Returns
    -------
    theta1_out, z1_out, theta2_out, z2_out : :class:`numpy.ndarray`
        2D array with dimensions (n, 4) containing the angles of the pendulums (theta1_out,theta2_out)
        and z values (z1_out, z2_out)
    """
    g = 9.81

    theta1, z1, theta2, z2 = y

    cos = np.cos(theta1-theta2)
    sin = np.sin(theta1-theta2)

    # Calculate the positions of upper arm
    theta1_out = z1

    z1_out = (m2*g*np.sin(theta2)*cos - m2*sin*(L1*z1**2*cos + L2*z2**2) -
              (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*sin**2)

    # Calculate the positions of lower arm
    theta2_out = z2

    z2_out = ((m1+m2)*(L1*z1**2*sin - g*np.sin(theta2) + g*np.sin(theta1)*cos) +
              m2*L2*z2**2*sin*cos) / L2 / (m1 + m2*sin**2)

    return theta1_out, z1_out, theta2_out, z2_out