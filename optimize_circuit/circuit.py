from gates import *
from hardware import QuantumHardware


class QuantumCircuit:
    """A quantum circuit defined on either one or two qubits

    A circuit is composed from three one qubit gates: X(p_1), Y(p_2), Z(p_3),
    where p_1, p_2 and p_3 are parameters, and one two qubit gate: CNOT.
    """

    def __init__(self, hardware: QuantumHardware):
        """Initializes a quantum circuit. If qubit_number > 2 raises
        not implemented error.

        :param hardware: QuantumHardware
        """

        self.qubit_number = hardware.qubit_number
        self.qubit_indexes = hardware.qubit_indexes
        self.gates = []

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
                if (index_1 not in self.qubit_indexes) or \
                        (index_1 not in self.qubit_indexes):
                    raise ValueError(f"The qubits with given indexes = ({index_1}, {index_2}) "
                                     f"are (is) not defined for the given QuantumHardware")
                self.add(CX(index_1, index_2))
            else:
                index = gate_str[2]
                if index not in self.qubit_indexes:
                    raise ValueError(f"The qubit with given index = {index} "
                                     f"is not defined for the given QuantumHardware")
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

    def __str__(self):
        """Uses string representation of the circuit: e.g. 'X(1, 90), Z(1, 180), CX(0,1)'"""
        return ", ".join([gate.to_sting_notation() for gate in self.gates])
