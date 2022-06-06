import pytest

from vamas import Vamas
from .test_vamas import TESTFILE_AES_STAIB


@pytest.fixture
def aes_staib():
    return Vamas(TESTFILE_AES_STAIB)


def test_aes_staib_header(aes_staib: Vamas):
    header = aes_staib.header
    assert header.institution_identifier == "Not Specified"
    assert header.instrument_model_identifier == "Staib SuperCMA"
    assert header.num_lines_comment == 1
    assert header.comment == "WinSpectro DAQ"
    assert header.experiment_mode == "NORM"
    assert header.scan_mode == "REGULAR"
    assert header.num_spectral_regions == 1
    assert header.num_blocks == 1


def test_aes_staib_blocks(aes_staib: Vamas):
    assert len(aes_staib.blocks) == 1
    block = aes_staib.blocks[0]
    assert block.block_identifier == "1st block id"
    assert block.sample_identifier == "1st sample id"

    assert block.year == 2022
    assert block.month == 5
    assert block.day == 26
    assert block.hour == 15
    assert block.minute == 0
    assert block.second == 46

    assert block.technique == "AES diff"
    assert block.analyzer_mode == "FAT"
    assert block.charge_detected_particle == -1
    assert block.x_label == "Kinetic Energy"
    assert block.x_units == "eV"
    assert block.x_start == 19.989319
    assert block.x_step == 1.983673
    assert block.num_corresponding_variables == 1
    assert block.signal_collection_time == 0.503
    assert block.num_additional_numerical_params == 4
    assert block.num_y_values == 1100


def test_aes_staib_corr_vars(aes_staib: Vamas):
    corr_vars = aes_staib.blocks[0].corresponding_variables
    if corr_vars is not None:
        assert (
            len(corr_vars) == aes_staib.blocks[0].num_corresponding_variables
        )
        assert corr_vars[0].label == "Intensity"
        assert corr_vars[0].unit == "d"
        assert corr_vars[0].y_min == -3423633
        assert corr_vars[0].y_max == 99886
        assert len(corr_vars[0].y_values) == aes_staib.blocks[0].num_y_values


def test_aes_staib_additional_numberical_params(aes_staib: Vamas):
    add_num_params = aes_staib.blocks[0].additional_numerical_params
    if add_num_params is not None:
        assert (
            len(add_num_params)
            == aes_staib.blocks[0].num_additional_numerical_params
        )
        assert add_num_params[0].label == "BKSrettime"
        assert add_num_params[1].label == "BKSsamples"
        assert add_num_params[2].label == "BKSresomode"
        assert add_num_params[3].label == "BKSresol"

        assert add_num_params[0].value == 5000
        assert add_num_params[1].value == 20120
        assert add_num_params[2].value == 1
        assert add_num_params[3].value == 1.0

        for param in add_num_params:
            assert param.unit == "n"
