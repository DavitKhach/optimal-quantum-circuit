from gates import *


def u_to_zxz_gates(u_one_gate: OneQubitUnitary):
    """Transforms OneQubitUnitary into ZXZ gate sequence

    :param u_one_gate: OneQubitUnitary
    :return: list of equivalent gates in form
            [Z(index, alpha_1), X(index, alpha_2), Z(index, alpha_3)]
    """
    gates = []

    if u_one_gate.lam != 0:
        gates.append(Z(u_one_gate.index, u_one_gate.lam - (np.pi / 2)))
    if u_one_gate.theta != 0:
        gates.append(Y(u_one_gate.index, u_one_gate.theta))
    if u_one_gate.phi != 0:
        gates.append(Z(u_one_gate.index, u_one_gate.phi + (np.pi / 2)))

    return gates


def u_to_zyz_gates(u_one_gate: OneQubitUnitary):
    """Transforms OneQubitUnitary into ZYZ gate sequence

    :param u_one_gate: OneQubitUnitary
    :return: list of equivalent gates in form
            [Z(index, alpha_1), Y(index, alpha_2), Z(index, alpha_3)]
    """
    gates = []

    if u_one_gate.lam != 0:
        gates.append(Z(u_one_gate.index, u_one_gate.lam))
    if u_one_gate.theta != 0:
        gates.append(Y(u_one_gate.index, u_one_gate.theta))
    if u_one_gate.phi != 0:
        gates.append(Z(u_one_gate.index, u_one_gate.phi))

    return gates


def u_to_xyx_gates(u_one_gate: OneQubitUnitary):
    pass


def u_to_xzx_gates(u_one_gate: OneQubitUnitary):
    pass


def u_to_yxy_gates(u_one_gate: OneQubitUnitary):
    pass


def u_to_yzy_gates(u_one_gate: OneQubitUnitary):
    pass