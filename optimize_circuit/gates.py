import numpy as np
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
        """Initializes an X gate with given parameter theta and qubit index"""
        self.arr = np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                             [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex)
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
        """Initializes an Y gate with given parameter theta and qubit index"""
        self.arr = np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                             [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex)
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
        """Initializes an Z gate with given parameter theta and qubit index"""
        self.arr = np.array([[np.exp(-1j * theta/2), 0],
                             [0, np.exp(1j * theta/2)]], dtype=complex)
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
            raise NotImplemented("The index_1 and index_2 for CX gate must be given either 0 or 1"
                                 f"and not equal to each other. It was given: index_1 = {index_1} "
                                 f"and index_2 = {index_2}")

        self.index_1 = index_1
        self.index_2 = index_2

    def to_sting_notation(self):
        return f"CX({self.index_1}, {self.index_2})"


class OneQubitUnitary(Gate):
    """A one qubit unitary gate

    UOne = [[cos(theta/2), -exp(1j * lam) * sin(theta/2)],
            [exp(1j * phi) * sin(theta/2), exp(1j * (phi + lam)) * cos(theta/2)]]
    """

    def __init__(self, index, theta, phi, lam):
        """Initializes a one qubit unitary gate"""

        self.arr = np.array([[np.cos(theta/2), -np.exp(1j * lam) * np.sin(theta/2)],
                             [np.exp(1j * phi) * np.sin(theta/2), np.exp(1j * (phi + lam)) * np.cos(theta/2)]]
                            , dtype=complex)
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.index = index

    def to_sting_notation(self):
        return f"UOne({self.index}, {self.theta}, {self.phi}, {self.lam})"

    def to_xyx_gates(self):
        pass

    def to_xzx_gates(self):
        pass

    def to_yxy_gates(self):
        pass

    def to_yzy_gates(self):
        pass

    def to_zxz_gates(self):
        pass

    def to_zyz_gates(self):
        pass


class TwoQubitUnitary(Gate):
    """A two qubit unitary gate

    """