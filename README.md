Bloch Sphere Explorer

Overview of the Project Bloch Sphere Explorer: This interactive view would serve to visualize quantum states on the Bloch Sphere. The user provides as input the real and imaginary parts of a quantum state, and it normalizes the input if necessary and produces both a 2D and 3D visualization for the corresponding state on the Bloch Sphere.
The simulation of the Quantum States is done by Qiskit, while Matplotlib was used to visualize the 2D Bloch Sphere. Plotly is used for building plots in an interactive 3D visualization, while Streamlit is for the web interface.

Features:-
- User-configurable amplitudes of quantum states around |0⟩ and |1⟩.
-Normalizes the input quantum state if the input probabilities do not sum to 1.
Bloch Sphere: plots the quantum state on the Bloch Sphere as a 2D image.
Bloch Sphere An interactive 3D representation of the Bloch Sphere.
Tech Stack
These include:
- Qiskit: Quantum circuit simulation.
- Qiskit Aer: Quantum state vector simulation backend.
- NumPy: to operate with complex numbers and to normalise states.
- Matplotlib: To visualize in 2D Bloch Sphere.
- Plotly: Makes 3D interactive visualization.
- Streamlit: For developing an intuitive web-based interface.

Install Dependencies
cmd:- pip install -r requirements.txt

Run the Application
streamlit run Bloch_Sphere.py

Example

Input real part: 1.0, imaginary part: 0.0 for |0⟩
Input real part: 1.0, imaginary part: 0.0 for |1⟩
Output will be a Bloch Sphere with the quantum state normalized to:
State |0⟩ amplitude: (0.707+0j)
State |1⟩ amplitude: (0.707+0j)
The state is visualized both as a 2D Bloch Sphere image and an interactive 3D object.

Contact

For any issues, questions, or feature requests, please contact the project maintainer:

Name: Raghav
LinkedIn:- https://www.linkedin.com/in/raghav-luthra-/
email:- raghavluthra555@gmail.com


