from optimize_circuit.gates import X, Y, Z, CX

DEFAULT_BASIS_GATES = frozenset({'X', 'Y', 'Z', 'CX'})
ACCEPTABLE_BASIS_GATES_LIST = {
    DEFAULT_BASIS_GATES,
    frozenset({'X', 'Z', 'CX'}),
    frozenset({'Y', 'Z', 'CX'})
}


class HardwareConfiguration:

    def __init__(self, qubit_number, basis_gates=DEFAULT_BASIS_GATES):
        """Initializes a quantum hardware configuration with basis gates"""

        if basis_gates not in ACCEPTABLE_BASIS_GATES_LIST:
            raise ValueError(f"The {basis_gates} are not one of "
                             f"the acceptable basis gates: "
                             f" {ACCEPTABLE_BASIS_GATES_LIST}")
        self._basis_gates = basis_gates
        self._qubit_number = qubit_number

        self.length_x = 10  # ns
        self.length_y = 10  # ns
        self.length_z = 10  # ns
        self.length_cx = 100  # ns

    def validate_qubit_index(self, qubit_index):
        """Validates if the qubit_index valid for the hardware

        :param qubit_index: int
        """
        if (not isinstance(qubit_index, int)) or \
                qubit_index >= self.qubit_number or qubit_index < 0:
            raise ValueError(f"'{qubit_index}' is not valid qubit index")

    def duration_of_one_qubit_gates(self, gate_list):
        """Calculates the duration for the given gate_list
        Defined for single qubit

        :param gate_list: list of Gates
        :return:
        """
        duration = 0
        for gate in gate_list:
            if isinstance(gate, X):
                duration += self.length_x
            elif isinstance(gate, Y):
                duration += self.length_y
            elif isinstance(gate, Z):
                duration += self.length_z
            elif isinstance(gate, CX):
                raise ValueError("CX gate cannot be presented in "
                                 "the list of the single qubit gates")

        return duration

    @property
    def length_x(self):
        """The length of the X gate in ns"""
        return self._length_x

    @property
    def length_y(self):
        """The length of the Y gate in ns"""
        return self._length_y

    @property
    def length_z(self):
        """The length of the Z gate in ns"""
        return self._length_z

    @property
    def length_cx(self):
        """The length of the Z gate in ns"""
        return self._length_cx

    @property
    def basis_gates(self):
        """The basis gates of the Hardware"""
        return self._basis_gates

    @property
    def qubit_number(self):
        """The number of the qubits in the hardware"""
        return self._qubit_number

    @length_x.setter
    def length_x(self, length):
        """Changes the length of the X gate"""
        if not isinstance(length, int):
            raise TypeError("The length of a gate must be an integer")
        if length <= 0:
            raise ValueError("The length of a gate can not be negative")
        self._length_x = length

    @length_y.setter
    def length_y(self, length):
        """Changes the length of the Y gate"""
        if not isinstance(length, int):
            raise TypeError("The length of a gate must be an integer")
        if length <= 0:
            raise ValueError("The length of a gate can not be negative")
        self._length_y = length

    @length_z.setter
    def length_z(self, length):
        """Changes the length of the Z gate"""
        if not isinstance(length, int):
            raise TypeError("The length of a gate must be an integer")
        if length <= 0:
            raise ValueError("The length of a gate can not be negative")
        self._length_z = length

    @length_cx.setter
    def length_cx(self, value):
        """Changes the length of the CX gate"""
        self._length_cx = value
