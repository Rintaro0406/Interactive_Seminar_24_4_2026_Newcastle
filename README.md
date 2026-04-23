# AstroObs Seminar — Interactive data visualisation for teaching and outreach

This repository contains materials for the AstroObs interactive seminar (April 2026). It includes Jupyter notebooks and a Streamlit app, "Mundus ex Machina", for visualising cosmological quantities for teaching and public outreach.

## Contents
- **Streamlit app — "Mundus ex Machina"**: an interactive educational tool for exploring cosmological models and the large-scale structure of the Universe. Sections include:
  - Basics (Hubble parameter, cosmological distances, etc.)
  - Cosmic Microwave Background (including polarization)
  - Galaxy clustering
  - Weak gravitational lensing
- **Notebooks**:
  - Interactive plotting and animation examples (matplotlib, Plotly, Bokeh) using the matter power spectrum
  - Introduction to Streamlit (Can you modify hier, Devang?)
  - Example analysis using Gaussian processes

## How to run

1. Clone the repository (replace <repository-url> with this repo's URL):

    ```bash
    git clone <repository-url>
    cd interactive_seminar_24_4_2026
    ```

2. Create and activate a Python environment (Conda recommended):

    ```bash
    conda create -n interactive_seminar_env python=3.9 -y
    conda activate interactive_seminar_env
    ```

   Alternatively, use `python -m venv .venv` and `source .venv/bin/activate`.

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Install `classy` (Python wrapper for CLASS) if needed:

    ```bash
    pip install classy
    ```

5. If you need the CLASS Fortran code (used by `classy`), clone and build it:

    ```bash
    git clone https://github.com/lesgourg/class_public.git
    cd class_public
    make
    cd ..
    ```

6. Run the Streamlit app:

    ```bash
    cd mundus_ex_machina
    streamlit run mundus_ex_machina.py
    ```

7. Open the app in your browser at the URL shown by Streamlit (typically http://localhost:8501).

## Notes
- The repository was prepared for teaching and demonstration; some notebooks include developer notes you can adapt.
- If you run into missing dependencies or build issues for CLASS, consult the CLASS and classy documentation:
  - https://github.com/lesgourg/class_public
  - https://github.com/lesgourg/class_public/tree/master/CLASS

If you'd like, I can also:
- update any notebook headers/metadata for clarity
- add a minimal `requirements.txt` snippet or environment YAML
- run a quick local test (if you want me to start the app here)
