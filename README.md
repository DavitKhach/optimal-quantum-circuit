# Optimal quantum circuit

An open-source package for optimizing circuits. 
Currently, the implementation is limited to the one qubit circuit case.

In order to use the package firstly download the package from GitHub.
For further configurations we recommend to install [Anaconda](https://www.anaconda.com/products/individual)
and create a separate `conda` environment for the package:

```bash
conda create -n ENV_NAME python=3
```

Activate your new environment.

```bash
conda activate ENV_NAME
```

Install required libraries:

```bash
pip install -r requirements.txt
```

For development/contribution proposes one can use `pytests` to check the test coverage:

```bash
pytest --cov optimize_circuit
```

Example of a code:

```bash
hardware = HardwareConfiguration(1, basis_gates={'X', 'Y', 'Z', 'CX'})
circuit = QuantumCircuit(hardware)
circuit.add_from_string("X(0, 75.0), Y(0, 67.0), X(0, 85.0), Y(0, 55.0), X(0, 55.0), Y(0, 67.0), X(0, 96.0)")
circuit.optimize()
print(circuit)
```

The output of the circuit will be either `"Z(0, angle_1), X(0, angle_2), Z(0, angle_3)"` or
`"Z(0, angle_1), Y(0, angle_2), Z(0, angle_3)"` depending on which sequence of universal gate 
sequence (`ZYZ` or `ZXZ`) will be smaller by duration. By using the default durations for the 
gates the output will be:

```bash
Z(0, 151.89983851222325), Y(0, 31.28762615922378), Z(0, -156.57543302957887)
```

There are four other universal rotational gate sequences (`XYX`, `XZX`, `YZY` and `YXY`)
that are implemented here. 

In the above example the `ZYZ` gate sequence was implemented. Let's 
define such an HardwareConfiguration that `ZXZ` will be preferable:

```bash
hardware = HardwareConfiguration(1, basis_gates={'X', 'Y', 'Z', 'CX'})
circuit = QuantumCircuit(hardware)
hardware.length_y = 30
circuit.add_from_string("X(0, 75.0), Y(0, 67.0), X(0, 85.0), Y(0, 55.0), X(0, 55.0), Y(0, 67.0), X(0, 96.0)")
circuit.optimize()
print(circuit)
```

The output will be:

```bash
Z(0, 150.32904218542836), X(0, 31.28762615922378), Z(0, -155.00463670278398)
```

When the length of the circuit is less than 3 the `optimize` method 
implements micro optimization by considering basic circuit identities.
