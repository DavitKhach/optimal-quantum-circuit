from gates import *


class QuantumCircuit:
    """A quantum circuit defined on either one or two qubits

    A circuit is composed from three one qubit gates: X(p_1), Y(p_2), Z(p_3),
    where p_1, p_2 and p_3 are parameters, and one two qubit gate: CNOT.
    """

    def __init__(self, qubit_number):
        """Initializes a quantum circuit. If qubit_number > 2 raises
        not implemented error. In the initialization the default values for
        gate length are defined that can be changed with corresponding setter.

        :param qubit_number: 1 or 2
        """

        self.qubit_number = qubit_number
        self.length_x = 10  # ns
        self.length_y = 10  # ns
        self.length_z = 10  # ns
        self.length_cnot = 100  # ns
        self.hardware_basis_gates = {"X", "Y", "Z", "CNOT"}
        self.gates = []

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
    def hardware_basis_gates(self):
        """The basis gates of the Hardware"""
        return self._hardware_basis_gates

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

    @hardware_basis_gates.setter
    def hardware_basis_gates(self, basis_gates):
        """Changes the set of the basis gates"""
        if not (basis_gates == {'X', 'Y', 'Z', 'CNOT'} or
                basis_gates == {'X', 'Y', 'CNOT'} or
                basis_gates == {'X', 'Z', 'CNOT'} or
                basis_gates == {'Y', 'Z', 'CNOT'}):
            raise ValueError("The basis gates should be either {'X', 'Y', 'Z', 'CNOT'}"
                             "or 'X', 'Y', 'CNOT'} or {'X', 'Z', 'CNOT'} "
                             "or {'Y', 'Z', 'CNOT'}. It was given: ", basis_gates)
        self._hardware_basis_gates = basis_gates

    def add(self, gate: Gate):
        """Adds a gate represented by an instance of Gate class
        :param gate: str or an instance of X or Y or Z or CX classes
        """
        if isinstance(gate, str):
            self.gates.append(gate)

    def add_from_string(self, gates_in_string):
        """Adds gates from the string

        :param gates_in_string: str, e.g. "X(1, 90), Z(1, 180), CX(0,1)"
        """

        for gate_str in gates_in_string.split("), "):
            if gate_str[0:2] == "CX":
                index_1 = int(gate_str[3])
                index_2 = int(gate_str[-1])
                self.add(CX(index_1, index_2))
            else:
                index = gate_str[2]
                theta = float(gate_str.split()[-1])
                if gate_str[0] == "X":
                    self.add(X(index, theta))
                elif gate_str[0] == "Y":
                    self.add(Y(index, theta))
                elif gate_str[0] == "Z":
                    self.add(X(index, theta))
                else:
                    raise ValueError("The given string must be in the following form "
                                     "'{Gate}({qubit}, {Angle}), CX({qubitA}, {qubitB}), "
                                     "{Gate}({qubit}, {Angle}) ...' with exact spacing."
                                     f". The given string = {gates_in_string}")

    def __str__(self):
        """Uses string representation of the circuit: e.g. 'X(1, 90), Z(1, 180), CX(0,1)'"""
        return ", ".join([gate.to_sting_notation() for gate in self.gates])
