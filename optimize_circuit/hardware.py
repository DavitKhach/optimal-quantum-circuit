class QuantumHardware:

    def __init__(self, qubit_number, basis_gates=None):
        """Initializes a quantum Hardware with basis gates"""

        if basis_gates is None:
            basis_gates = {'X', 'Y', 'Z', 'CNOT'}
        self.qubit_number = qubit_number
        self.qubit_indexes = list(range(qubit_number))
        self.basis_gates = basis_gates

        self.length_x = 10  # ns
        self.length_y = 10  # ns
        self.length_z = 10  # ns
        self.length_cx = 100  # ns

    @property
    def length_x(self):
        """The length of the X gate in ns"""
        return self._length_x

    @property
    def length_y(self):
        """The length of the Y gate in ns"""
        return self._length_x

    @property
    def length_z(self):
        """The length of the Z gate in ns"""
        return self._length_x

    @property
    def length_cx(self):
        """The length of the Z gate in ns"""
        return self._length_cx

    @property
    def basis_gates(self):
        """The basis gates of the Hardware"""
        return self._basis_gates

    @length_x.setter
    def length_x(self, length):
        """Changes the length of the X gate"""
        if not isinstance(length, int):
            raise TypeError("The length of a gate must be an integer")
        if length <= 0:
            raise ValueError("the length of a gate can not be negative")
        self._length_x = length

    @length_y.setter
    def length_y(self, length):
        """Changes the length of the Y gate"""
        if not isinstance(length, int):
            raise TypeError("The length of a gate must be an integer")
        if length <= 0:
            raise ValueError("the length of a gate can not be negative")
        self._length_y = length

    @length_z.setter
    def length_z(self, length):
        """Changes the length of the Z gate"""
        if not isinstance(length, int):
            raise TypeError("The length of a gate must be an integer")
        if length <= 0:
            raise ValueError("the length of a gate can not be negative")
        self._length_z = length

    @length_cx.setter
    def length_cx(self, value):
        """Changes the length of the CX gate"""
        self._length_cx = value

    @basis_gates.setter
    def basis_gates(self, new_basis_gates):
        """Changes the set of the basis gates"""
        if not (new_basis_gates == {'X', 'Y', 'Z', 'CNOT'} or
                new_basis_gates == {'X', 'Y', 'CNOT'} or
                new_basis_gates == {'X', 'Z', 'CNOT'} or
                new_basis_gates == {'Y', 'Z', 'CNOT'}):
            raise ValueError("The basis gates should be either {'X', 'Y', 'Z', 'CNOT'}"
                             "or 'X', 'Y', 'CNOT'} or {'X', 'Z', 'CNOT'} "
                             "or {'Y', 'Z', 'CNOT'}. It was given: ", new_basis_gates)
        self._basis_gates = new_basis_gates


