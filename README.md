# ThermoHybrid-Tm-Predictor# ThermoHybrid: Hybrid Thermodynamic-ML for Oligo Tm Prediction  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alrawab/ThermoHybrid-Tm-Predictor/blob/main/notebooks/Demo.ipynb)  

**Novelty**: First model to correct NN thermodynamics with *secondary structure penalties* via SHAP-guided ML.  

## Quick Start  
```python
pip install -r requirements.txt
from oligobench import predict_tm
predict_tm("GCGGCGCGGTTTTGCGGCGCGG", salt_conc=0.05)  # → 72.3°C (+ structure penalty)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alrawab/ThermoHybrid-Tm-Predictor/blob/main/notebooks/ThermoHybrid_Demo.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alrawab/ThermoHybrid-Tm-Predictor/blob/main/notebooks/ThermoHybrid_Demo.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)