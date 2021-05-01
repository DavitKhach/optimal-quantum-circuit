from transformations import u_to_zxz_gates, u_to_zyz_gates
from gates import OneQubitUnitary
import numpy as np


def optimize_one_qubit_circuit(gate_list, hardware):
    """Optimizes one qubit gate_list

    :param hardware: HardwareConfiguration
    :param gate_list: list of Gate objects (X, Y, Z)
    :return: optimized gate_list
    """

    if len(gate_list) == 0:
        return gate_list

    index = gate_list[0].qubit_index
    resulting_unitary = np.identity(2, dtype=complex)

    for gate in gate_list:
        resulting_unitary = np.matmul(resulting_unitary, gate.arr)

    global_phase = resulting_unitary[0, 0]

    resulting_unitary = np.exp(-1j * global_phase) * global_phase

    theta_rad = np.arccos(resulting_unitary[0, 0])
    phi_rad = np.angle(resulting_unitary[1, 0])
    lam_rad = np.angle(-resulting_unitary[0, 1])

    u_one_qubit_gate = OneQubitUnitary(
        index, np.rad2deg(theta_rad), np.rad2deg(phi_rad), np.rad2deg(lam_rad))

    return u_to_optimal_three_gates(u_one_qubit_gate, hardware)


def u_to_optimal_three_gates(u_one_gate, hardware):
    """ Finds the optimal gate sequence

    :param u_one_gate: OneQubitUnitary
    :param hardware: HardwareConfiguration
    :return: list of optimal gates
    """
    gates_zxz = u_to_zxz_gates(u_one_gate)
    gates_zyz = u_to_zyz_gates(u_one_gate)

    if "X" not in hardware.basis_gates:
        return gates_zyz
    if "Y" not in hardware.basis_gates:
        return gates_zxz

    if hardware.duration_of_one_qubit_gates(gates_zxz) < \
            hardware.duration_of_one_qubit_gates(gates_zxz):
        return gates_zxz
    else:
        return gates_zyz
