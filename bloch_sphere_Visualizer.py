import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import plotly.graph_objects as go

# Function to check if the input state is valid
def is_valid_state(state):
    return np.isclose(np.sum(np.abs(state) ** 2), 1)

# Normalize the state if it's not valid
def normalize_state(state):
    norm = np.sqrt(np.sum(np.abs(state) ** 2))
    return [amp / norm for amp in state]

# Function to create a 3D Bloch sphere
def plot_bloch_sphere(state):
    fig = go.Figure()

    # Create the Bloch sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    fig.add_trace(go.Surface(x=x, y=y, z=z, opacity=0.3, colorscale='Viridis'))

    # Add the state vector
    theta = 2 * np.arccos(np.abs(state[0]))
    phi = np.angle(state[1])

    x_state = np.sin(theta) * np.cos(phi)
    y_state = np.sin(theta) * np.sin(phi)
    z_state = np.cos(theta)

    fig.add_trace(go.Scatter3d(x=[x_state], y=[y_state], z=[z_state], mode='markers', marker=dict(size=10, color='red')))

    # Update layout
    fig.update_layout(scene=dict(
        xaxis=dict(nticks=4, range=[-1, 1]),
        yaxis=dict(nticks=4, range=[-1, 1]),
        zaxis=dict(nticks=4, range=[-1, 1]),
        aspectmode='cube'),
        title="Bloch Sphere")

    return fig

# Main function to explore quantum states and visualize them
def bloch_sphere_explorer(real_part_0, imag_part_0, real_part_1, imag_part_1):
    # Form the complex state vector
    state = [complex(real_part_0, imag_part_0), complex(real_part_1, imag_part_1)]

    # Check if it's valid, and normalize if needed
    if not is_valid_state(state):
        st.warning("The input state is invalid. Normalizing the state...")
        state = normalize_state(state)
        st.write(f"Normalized state: {state}")

    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1)

    # Initialize the qubit to the user-defined state
    qc.initialize(state, 0)

    # Get the simulator backend
    sim = Aer.get_backend('statevector_simulator')

    # Transpile the quantum circuit for the simulator
    qc = transpile(qc, sim)

    # Execute the circuit and get the statevector
    result = sim.run(qc).result()
    statevector = result.get_statevector()

    # Plot the Bloch sphere as an image
    fig_image = plot_bloch_multivector(statevector)
    st.pyplot(fig_image)

    # Plot the Bloch sphere in 3D
    fig_3d = plot_bloch_sphere(statevector)
    st.plotly_chart(fig_3d)

# Streamlit interface
st.title("Bloch Sphere Explorer")

# User input for the quantum state
st.header("Enter Quantum State Amplitudes")
real_part_0 = st.number_input("Real part of |0⟩:", value=1.0, format="%.2f")
imag_part_0 = st.number_input("Imaginary part of |0⟩:", value=0.0, format="%.2f")
real_part_1 = st.number_input("Real part of |1⟩:", value=0.0, format="%.2f")
imag_part_1 = st.number_input("Imaginary part of |1⟩:", value=0.0, format="%.2f")

if st.button("Visualize Bloch Sphere"):
    bloch_sphere_explorer(real_part_0, imag_part_0, real_part_1, imag_part_1)
