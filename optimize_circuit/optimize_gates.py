from optimize_circuit.transformations import u_to_zxz_gates, u_to_zyz_gates
from optimize_circuit.gates import OneQubitUnitary, X, Y, Z
import numpy as np


def optimize_one_qubit_circuit(gate_list, hardware):
    """Optimizes one qubit gate_list

    :param hardware: HardwareConfiguration
    :param gate_list: list of Gate objects (X, Y, Z)
    :return: optimized gate_list
    """
    index = gate_list[0].qubit_index
    resulting_unitary = np.identity(2, dtype=complex)

    for gate in gate_list:
        resulting_unitary = np.matmul(resulting_unitary, gate.arr)

    global_phase = np.angle(resulting_unitary[0, 0])

    resulting_unitary = np.exp(-1j * global_phase) * resulting_unitary
    if resulting_unitary[0, 0].imag > 1e-5:
        raise ArithmeticError(
            "resulting_unitary[0, 0].imag must be 0 "
            f"at this point, but it is equal to "
            f"{resulting_unitary[0, 0].imag }"
        )
    theta_rad = np.arccos(np.abs(resulting_unitary[0, 0]))
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
            hardware.duration_of_one_qubit_gates(gates_zyz):
        return gates_zxz
    else:
        return gates_zyz


def micro_optimize_one_qubit_circuit(gate_list):
    """Does mini optimization on circuit with
    less than 3 gates
    """
    if len(gate_list) == 1:
        if int(gate_list[0].theta) % 360 == 0:
            return []
        else:
            return gate_list
    if len(gate_list) == 2:
        return optimize_two_gate(gate_list)
    if len(gate_list) == 3:
        return optimize_three_gate(gate_list)


def optimize_three_gate(gate_list):
    """Optimizes three gate circuit

    :param gate_list: list of gates
    :return: optimized gate_list
    """
    optimized_first_two_gates = optimize_two_gate(gate_list[0:2])
    optimized_last_two_gates = optimize_two_gate(gate_list[1:])

    if len(optimized_first_two_gates) <= 1:
        gate_list = optimized_first_two_gates + gate_list[2:]
        return optimize_two_gate(gate_list)
    if len(optimized_last_two_gates) <= 1:
        gate_list = gate_list[0:1] + optimized_last_two_gates
        return optimize_two_gate(gate_list)

    return optimize_with_three_gate_identities(gate_list)


def optimize_two_gate(gate_list):
    """Optimizes two gate circuit

    :param gate_list: list of Gates
    :return: optimized gate_list
    """
    if isinstance(gate_list[0], X) and isinstance(gate_list[1], X):
        theta = gate_list[0].theta + gate_list[1].theta
        if int(theta) % 360 == 0:
            return []
        else:
            return [X(0, theta)]
    if isinstance(gate_list[0], Y) and isinstance(gate_list[1], Y):
        theta = gate_list[0].theta + gate_list[1].theta
        if int(theta) % 360 == 0:
            return []
        else:
            return [Y(0, theta)]
    if isinstance(gate_list[0], Z) and isinstance(gate_list[1], Z):
        theta = gate_list[0].theta + gate_list[1].theta
        if int(theta) % 360 == 0:
            return []
        else:
            return [Z(0, theta)]

    return gate_list


def optimize_with_three_gate_identities(gate_list):
    """Optimize with three gates identities

    :param gate_list: list of gates
    :return: optimized gate_list
    """
    # XYX = -Y, XZX = -Z when X.theta ==180
    if isinstance(gate_list[0], X) and isinstance(gate_list[2], X) and \
            int(gate_list[0].theta) == 180 and int(gate_list[2].theta) == 180:
        if isinstance(gate_list[1], Y):
            return [Y(gate_list[1].qubit_index, -gate_list[1].theta)]
        if isinstance(gate_list[1], Z):
            return [Z(gate_list[1].qubit_index, -gate_list[1].theta)]

    # YXY = -X, YZY = -Z when Y.theta ==180
    if isinstance(gate_list[0], Y) and isinstance(gate_list[2], Y) and \
            int(gate_list[0].theta) == 180 and int(gate_list[2].theta) == 180:
        if isinstance(gate_list[1], X):
            return [X(gate_list[1].qubit_index, -gate_list[1].theta)]
        if isinstance(gate_list[1], Z):
            return [Z(gate_list[1].qubit_index, -gate_list[1].theta)]

    # ZXZ = -X, ZYZ = -Y when Z.theta ==180
    if isinstance(gate_list[0], Z) and isinstance(gate_list[2], Z) and \
            int(gate_list[0].theta) == 180 and int(gate_list[2].theta) == 180:
        if isinstance(gate_list[1], X):
            return [X(gate_list[1].qubit_index, -gate_list[1].theta)]
        if isinstance(gate_list[1], Y):
            return [Y(gate_list[1].qubit_index, -gate_list[1].theta)]

    # Pauli(90)Pauli'(180)Pauli(90) = Pauli'(180)
    if int(gate_list[0].theta) == 90 and int(gate_list[1].theta) == 180 \
            and int(gate_list[2].theta) == 90:
        return [gate_list[1]]

    return gate_list
