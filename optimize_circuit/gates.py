import numpy as np
from numpy import cos, sin, exp
from abc import ABC, abstractmethod


class Gate(ABC):
    """Abstract class for gates"""

    @abstractmethod
    def to_sting_notation(self):
        """:returns string version of the gate"""

    def __str__(self):
        """:returns string version of the gate"""
        return self.to_sting_notation()


class X(Gate):
    """X rotation gate:

    X(theta) = [[cos(theta/2), -1j * sin(theta/2)]
                [-1j * sin(theta/2), cos(theta/2]]

    """

    def __init__(self, qubit_index, theta):
        """Initializes an X gate with given
        parameter theta (degrees) and qubit index
        """
        th = np.deg2rad(theta) / 2
        self.arr = np.array([[cos(th), -1j * sin(th)],
                             [-1j * sin(th), cos(th)]], dtype=complex)
        self.qubit_index = qubit_index
        self.theta = theta

    def to_sting_notation(self):
        """:returns string version of the gate"""
        return f"X({self.qubit_index}, {self.theta})"


class Y(Gate):
    """Y rotation gate:

    Y(theta) = [[cos(theta/2), -sin(theta/2)]
                [sin(theta/2), cos(theta/2]]

    """

    def __init__(self, qubit_index, theta):
        """Initializes an Y gate with given parameter
        theta (degrees) and qubit index
        """
        th = np.deg2rad(theta) / 2
        self.arr = np.array([[cos(th), -sin(th)],
                             [sin(th), cos(th)]], dtype=complex)
        self.qubit_index = qubit_index
        self.theta = theta

    def to_sting_notation(self):
        return f"Y({self.qubit_index}, {self.theta})"


class Z(Gate):
    """Z rotation gate:

    Z(theta) = [[exp(-1j * theta/2), 0]
                [0, exp(1j * theta/2)]]

    """

    def __init__(self, qubit_index, theta):
        """Initializes an Z gate with given parameter
        theta (degrees) and qubit index
        """
        th = np.deg2rad(theta) / 2
        self.arr = np.array([[exp(-1j * th), 0],
                             [0, exp(1j * th)]], dtype=complex)
        self.qubit_index = qubit_index
        self.theta = theta

    def to_sting_notation(self):
        return f"Z({self.qubit_index}, {self.theta})"


class CX(Gate):
    """CX gate:

    CX(index_1, index_2);

    CX(0, 1) = [[1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0]]

    CX(1, 0) = [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]]
    """

    def __init__(self, index_1, index_2):
        """Initializes an CX gate with given gubit indexes"""
        if index_1 == 0 and index_2 == 1:
            self.arr = np.array([[1, 0, 0, 0],
                                 [0, 0, 0, 1],
                                 [0, 0, 1, 0],
                                 [0, 1, 0, 0]], dtype=complex)
        elif index_1 == 1 and index_2 == 0:
            self.arr = np.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 0, 1],
                                 [0, 0, 1, 0]], dtype=complex)
        else:
            raise NotImplementedError(
                "The index_1 and index_2 for CX gate must be given either "
                "0 or 1 and not equal to each other. It was given: "
                f"index_1 = {index_1} and index_2 = {index_2}")

        self.index_1 = index_1
        self.index_2 = index_2

    def to_sting_notation(self):
        return f"CX({self.index_1}, {self.index_2})"


class OneQubitUnitary(Gate):
    """A one qubit unitary gate

    UOne =
    [[cos(theta/2), -exp(1j * lam) * sin(theta/2)],
    [exp(1j * phi) * sin(theta/2), exp(1j * (phi + lam)) * cos(theta/2)]]
    """

    def __init__(self, index, theta, phi, lam):
        """Initializes a one qubit unitary gate

        :param index: index of the qubit
        :param theta: parameter in angles
        :param phi: parameter in angles
        :param lam: parameter in angles
        """
        th = np.deg2rad(theta) / 2
        ph = np.deg2rad(phi)
        lm = np.deg2rad(lam)
        self.arr = np.array(
            [[cos(th), -exp(1j * lm) * sin(th)],
             [exp(1j * ph) * sin(th), exp(1j * (ph + lm)) * cos(th)]],
            dtype=complex)
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.index = index

    def to_sting_notation(self):
        return f"UOne({self.index}, {self.theta}, {self.phi}, {self.lam})"


class TwoQubitUnitary(Gate):
    """A two qubit unitary gate
    Minimal Universal Two-qubit Quantum Circuits
    from "arXiv preprint quant-ph/0308033"
    """
    pass
