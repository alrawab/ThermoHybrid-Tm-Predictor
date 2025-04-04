import pytest
from oligobench.core.thermodynamics import calculate_nn_tm

def test_nn_tm_calculation():
    """Verify NN model returns plausible Tm values."""
    assert 50 < calculate_nn_tm("ATGCATGC") < 70

def test_high_gc_tm():
    """GC-rich sequences should have higher Tm."""
    assert calculate_nn_tm("GCGCGCGC") > calculate_nn_tm("ATATATAT")