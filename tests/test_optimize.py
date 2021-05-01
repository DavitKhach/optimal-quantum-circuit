import pytest
from optimize_circuit.circuit import QuantumCircuit
from optimize_circuit.hardware.hardware_configuration import HardwareConfiguration

xyz_hardware = HardwareConfiguration(1, basis_gates={'X', 'Y', 'Z', 'CX'})
xz_hardware = HardwareConfiguration(1, basis_gates={'X', 'Z', 'CX'})
yz_hardware = HardwareConfiguration(1, basis_gates={'Y', 'Z', 'CX'})


def test_optimize():
    circuit = QuantumCircuit(xyz_hardware)

    gates_string = "X(0, 180.0), Y(0, 67.0), X(0, 5.0), Y(0, 55.0)"

    circuit.add_from_string(gates_string)
    circuit.optimize()
    assert len(circuit) <= 3

    circuit_xxx = QuantumCircuit(xyz_hardware)
    circuit_xxx.add_from_string("X(0, 90), X(0, 90), X(0, 180)")
    circuit_xxx.optimize()
    assert str(circuit_xxx) == "[]"

    circuit_yyy = QuantumCircuit(xyz_hardware)
    circuit_yyy.add_from_string("Y(0, 90), Y(0, 90), Y(0, 180)")
    circuit_yyy.optimize()
    assert str(circuit_yyy) == "[]"

    circuit_yxy = QuantumCircuit(xyz_hardware)
    circuit_yxy.add_from_string("Y(0, 180), X(0, 86.0), Y(0, 180)")
    circuit_yxy.optimize()
    assert str(circuit_yxy) == "X(0, -86.0)"

    circuit_9018090 = QuantumCircuit(xyz_hardware)
    circuit_9018090.add_from_string("Z(0, 90), X(0, 180), Z(0, 90)")
    circuit_9018090.optimize()
    assert str(circuit_9018090) == "X(0, 180.0)"
