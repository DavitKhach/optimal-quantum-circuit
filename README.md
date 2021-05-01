# Optimal quantum circuit

An open-source project for optimizing circuits. 
Currently, the implementation is limited to the one-qubit circuit case.

## How to run


In order to use the project firstly clone the repository from GitHub.
For further configurations we recommend installing [Anaconda](https://www.anaconda.com/products/individual)
and creating a separate `conda` environment for the project:

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

## How to work with circuits

Example of circuit usage:

```python
from optimize_circuit.hardware_configuration import HardwareConfiguration
from optimize_circuit.circuit import QuantumCircuit

hardware = HardwareConfiguration(1, basis_gates={'X', 'Y', 'Z', 'CX'})
circuit = QuantumCircuit(hardware)
circuit.add_from_string("X(0, 75.0), Y(0, 67.0), X(0, 85.0), Y(0, 55.0), X(0, 55.0), Y(0, 67.0), X(0, 96.0)")
circuit.optimize()
print(circuit)
```

The output of the circuit will be either `"Z(0, angle_1), X(0, angle_2), Z(0, angle_3)"` or
`"Z(0, angle_1), Y(0, angle_2), Z(0, angle_3)"` depending on which sequence of gate 
sequence (`ZYZ` or `ZXZ`: for more info please have a look at [gate_identities](./docs/gate_identities.ipynb)
with Jupyter Notebook) will be smaller by duration. If we don't change the default durations 
for the gates (`10ns` for single qubit gates and `100ns` for `CX`) the output will be:

```bash
Z(0, 151.89983851222325), Y(0, 31.28762615922378), Z(0, -156.57543302957887)
```

There are four other rotational gate sequences (`XYX`, `XZX`, `YZY` and `YXY`)
that can be used, but are considered/implemented here yet. 

In the above example the `ZYZ` gate sequence was chosen for the decomposition. Now, let's 
define such an HardwareConfiguration that `ZXZ` will be preferable by changing default
durations:

```python
from optimize_circuit.hardware_configuration import HardwareConfiguration
from optimize_circuit.circuit import QuantumCircuit

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

When the length of the circuit is <= 3 the `optimize` method 
implements micro optimization by considering basic circuit identities.
