from optimize_circuit.circuit import QuantumCircuit
from optimize_circuit.hardware.hardware_configuration \
    import HardwareConfiguration

xyz_hardware = HardwareConfiguration(1, basis_gates={'X', 'Y', 'Z', 'CX'})
xz_hardware = HardwareConfiguration(1, basis_gates={'X', 'Z', 'CX'})
yz_hardware = HardwareConfiguration(1, basis_gates={'Y', 'Z', 'CX'})


def test_parsing():
    circuit1 = QuantumCircuit(xyz_hardware)

    gates_string = "X(0, 180.0), Y(0, 67.0), X(0, 5.0), Y(0, 55.0)"

    circuit1.add_from_string(gates_string)
    assert str(circuit1) == gates_string

    circuit2 = QuantumCircuit(yz_hardware)
    circuit2.add_from_string(gates_string)

    assert str(circuit2) == "Z(0, 90), Y(0, 180.0), Z(0, -90), " \
                            "Y(0, 67.0), Z(0, 90), Y(0, 5.0), " \
                            "Z(0, -90), Y(0, 55.0)"

    circuit3 = QuantumCircuit(xz_hardware)
    circuit3.add_from_string(gates_string)
    assert str(circuit3) == "X(0, 180.0), Z(0, -90), X(0, 67.0), " \
                            "Z(0, 90), X(0, 5.0), Z(0, -90), " \
                            "X(0, 55.0), Z(0, 90)"
