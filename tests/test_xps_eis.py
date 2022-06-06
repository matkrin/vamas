import pytest

from vamas import Vamas
from .test_vamas import TESTFILE_XPS_EIS


@pytest.fixture
def xps_eis():
    return Vamas(TESTFILE_XPS_EIS)


def test_xps_eis_header(xps_eis: Vamas):
    header = xps_eis.header
    assert header.comment == "Experiment Type: XPS"
    assert header.experiment_mode == "NORM"
    assert header.scan_mode == "REGULAR"
    assert header.num_spectral_regions == 4
    assert header.num_blocks == 4
    assert header.experiment_mode == "NORM"


def test_xps_eis_blocks(xps_eis: Vamas):
    blocks = xps_eis.blocks
    for b in blocks:
        assert b.year == 2021
        assert b.analysis_source_characteristic_energy == 1486.7
        assert b.analysis_source_strength == 400.0
        assert b.analyzer_mode == "FAT"
        assert b.analyzer_work_function_or_acceptance_energy == 4.5
        assert b.analysis_width_x == 1200
        assert b.analysis_width_y == 1200
        assert b.charge_detected_particle == -1
        assert b.x_label == "kinetic energy"
        assert b.x_units == "eV"
        assert b.num_corresponding_variables == 1


def test_xps_eis_first_block(xps_eis: Vamas):
    b = xps_eis.blocks[0]
    assert b.analyzer_pass_energy_or_retard_ratio_or_mass_res == 50
    assert b.x_start == 1506.7
    assert b.x_step == -0.1
    assert b.signal_collection_time == 0.2
    assert b.num_scans_to_compile_block == 5
    assert b.signal_time_correction == 7e-8
    assert b.num_y_values == 8201


def test_xps_eis_last_block(xps_eis: Vamas):
    b = xps_eis.blocks[3]
    assert b.analyzer_pass_energy_or_retard_ratio_or_mass_res == 20
    assert b.x_start == 1246.7
    assert b.x_step == -0.05
    assert b.signal_collection_time == 0.2
    assert b.num_scans_to_compile_block == 10
    assert b.signal_time_correction == 7e-8
    assert b.num_y_values == 541


def test_xps_eis_header_corresponding_variables(xps_eis: Vamas):
    for block in xps_eis.blocks:
        corr_vars = block.corresponding_variables
        if corr_vars is not None:
            assert len(corr_vars) == block.num_corresponding_variables
            assert corr_vars[0].label == "count rate"
            assert corr_vars[0].unit == "c/s"


def test_xps_eis_first_block_corresponding_variables(xps_eis: Vamas):
    corr_vars = xps_eis.blocks[0].corresponding_variables
    if corr_vars is not None:
        assert corr_vars[0].y_min == 2141
        assert corr_vars[0].y_max == 84683
        assert len(corr_vars[0].y_values) == xps_eis.blocks[0].num_y_values


def test_xps_eis_last_block_corresponding_variables(xps_eis: Vamas):
    corr_vars = xps_eis.blocks[3].corresponding_variables
    if corr_vars is not None:
        assert corr_vars[0].y_min == 7813
        assert corr_vars[0].y_max == 12216
        assert len(corr_vars[0].y_values) == xps_eis.blocks[3].num_y_values
