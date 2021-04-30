from gates import *
from hardware import HardwareConfiguration


class QuantumCircuit:
    """A quantum circuit defined on either one or two qubits

    A circuit is composed from three one qubit gates:
    X(index, p_1), Y(index, p_2), Z(index, p_3), where p_1, p_2 and p_3
    are parameters, and one two qubit gate: CNOT.
    """

    def __init__(self, hardware: HardwareConfiguration):
        """Initializes a quantum circuit. If qubit_number > 2 raises
        not implemented error.

        :param hardware: QuantumHardware
        """

        self.hardware = hardware
        self.gates = []

    def add(self, gate: Gate):
        """Adds a gate represented by an instance of Gate class
        :param gate: Gate object
        """
        self.gates.append(gate)

    def add_from_string(self, gates_in_string):
        """Adds gates from the string

        :param gates_in_string: str, e.g. "X(1, 90), Z(1, 180), CX(0,1)"
        """

        for gate_str in gates_in_string.split("), "):
            if gate_str[0:2] == "CX":
                index_1 = int(gate_str[3])
                index_2 = int(gate_str[-1])
                self.hardware.validate_qubit_index(index_1)
                self.hardware.validate_qubit_index(index_2)
                self.add(CX(index_1, index_2))
            else:
                index = gate_str[2]
                self.hardware.validate_qubit_index(index)
                theta = np.deg2rad(float(gate_str.split()[-1]))
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

    def get_cx_number(self):
        """Calculates the number of CX gates on the fly"""
        return sum([1 for gate in self.gates if isinstance(gate, CX)] + [0])

    def get_x_number(self):
        """Calculates the number of X gates on the fly"""
        return sum([1 for gate in self.gates if isinstance(gate, X)] + [0])

    def get_y_number(self):
        """Calculates the number of Y gates on the fly"""
        return sum([1 for gate in self.gates if isinstance(gate, Y)] + [0])

    def get_z_number(self):
        """Calculates the number of Z gates on the fly"""
        return sum([1 for gate in self.gates if isinstance(gate, Z)] + [0])

    def __str__(self):
        """Uses string representation of the circuit: e.g. 'X(1, 90), Z(1, 180), CX(0,1)'"""
        return ", ".join([gate.to_sting_notation() for gate in self.gates])

    def __len__(self):
        """Return number of gates in the circuit."""
        return len(self.gates)
