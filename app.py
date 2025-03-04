from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Maxwell's Equations Calculator
def maxwells_equations(E, B, rho, J):
    div_E = rho / 8.854e-12  # ε0
    div_B = 0
    curl_E = -B
    curl_B = 1.2566e-6 * J + 8.854e-12 * E  # μ0
    
    return {
        "Gauss's Law for Electricity": div_E,
        "Gauss's Law for Magnetism": div_B,
        "Faraday's Law of Induction": curl_E,
        "Ampère's Law with Maxwell's addition": curl_B,
    }

# Quantum Field Calculators
def quark_mass_energy(mass):
    return mass * (3e8)**2  # E = mc²

def gluon_strength(alpha_s, distance):
    return alpha_s / distance  # Strong force potential

def lepton_oscillation_probability(theta, L, E):
    return (np.sin(2*theta))**2 * (np.sin(1.27 * L/E))**2  # Neutrino oscillation

def boson_mass(wavelength):
    return (6.626e-34) / (wavelength * 3e8)  # λ = h/(mc)

def higgs_coupling(mass, vev):
    return mass / (vev * np.sqrt(2))  # Yukawa coupling approximation

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/maxwell", methods=["GET", "POST"])
def maxwell():
    results = None
    if request.method == "POST":
        try:
            E = float(request.form.get("E"))
            B = float(request.form.get("B"))
            rho = float(request.form.get("rho"))
            J = float(request.form.get("J"))
            results = maxwells_equations(E, B, rho, J)
        except ValueError:
            results = "Invalid input. Please enter numeric values."
    return render_template("maxwell.html", results=results)

@app.route("/quantum/quark", methods=["GET", "POST"])
def quark_calculator():
    result = None
    if request.method == "POST":
        try:
            mass = float(request.form.get("mass"))
            result = f"Energy equivalent: {quark_mass_energy(mass):.2e} J"
        except ValueError:
            result = "Invalid input. Please enter a numeric value."
    return render_template("quantum/quark.html", result=result)

@app.route("/quantum/gluon", methods=["GET", "POST"])
def gluon_calculator():
    result = None
    if request.method == "POST":
        try:
            alpha_s = float(request.form.get("alpha_s"))
            distance = float(request.form.get("distance"))
            result = f"Strong force potential: {gluon_strength(alpha_s, distance):.2e} GeV/fm"
        except ValueError:
            result = "Invalid input. Please enter numeric values."
    return render_template("quantum/gluon.html", result=result)

@app.route("/quantum/lepton", methods=["GET", "POST"])
def lepton_calculator():
    result = None
    if request.method == "POST":
        try:
            theta = float(request.form.get("theta"))
            L = float(request.form.get("L"))
            E = float(request.form.get("E"))
            prob = lepton_oscillation_probability(theta, L, E)
            result = f"Oscillation probability: {prob:.2%}"
        except ValueError:
            result = "Invalid input. Please enter numeric values."
    return render_template("quantum/lepton.html", result=result)

@app.route("/quantum/boson", methods=["GET", "POST"])
def boson_calculator():
    result = None
    if request.method == "POST":
        try:
            wavelength = float(request.form.get("wavelength"))
            result = f"Boson mass: {boson_mass(wavelength):.2e} kg"
        except ValueError:
            result = "Invalid input. Please enter a numeric value."
    return render_template("quantum/boson.html", result=result)

@app.route("/quantum/higgs", methods=["GET", "POST"])
def higgs_calculator():
    result = None
    if request.method == "POST":
        try:
            mass = float(request.form.get("mass"))
            vev = float(request.form.get("vev"))
            result = f"Yukawa coupling: {higgs_coupling(mass, vev):.4f}"
        except ValueError:
            result = "Invalid input. Please enter numeric values."
    return render_template("quantum/higgs.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)