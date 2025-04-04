from Bio.SeqUtils import MeltingTemp as mt
from nupack import Model

def calculate_nn_tm(sequence: str, salt_conc: float = 0.05) -> float:
    """Calculate Tm using Nearest-Neighbor thermodynamics."""
    return mt.Tm_NN(
        sequence,
        nn_table=mt.DNA_NN1,
        salt_correction_method=mt.SALT_CORRECTION_OWCZARZY,
        Na=salt_conc * 1000  # Convert M to mM
    )

def predict_secondary_structure(sequence: str) -> dict:
    """Predict secondary structures using NUPACK."""
    model = Model(material='dna')
    analysis = Model(strands=[sequence]).analyze()
    return {
        'hairpin': analysis.hairpins[0].energy if analysis.hairpins else 0,
        'dimer': analysis.dimers[0].energy if analysis.dimers else 0
    }