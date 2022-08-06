from typing import Union, List, Dict, TextIO
from pathlib import Path

from .vamas_header import (
    VamasHeader,
    ExperimentVariable,
    FutureUpgradeExperimentEntry,
)
from .vamas_block import (
    VamasBlock,
    SputteringSource,
    LinescanCoordinates,
    CorrespondingVariable,
    AdditionalNumericalParam,
)

from .errors import VmsIdentifierError, FileExtensionError


class Vamas:
    """Main class for handling a vamas file

    Parses the vamas file into the attributes header and blocks.

    Args:
        file (Union[str, Path]): vamas file to be parsed

    Attributes:
        header (VamasHeader):
        blocks (List[VamasBlock]):
    """

    def __init__(self, file: Union[str, Path]) -> None:
        if not str(file).endswith(".vms"):
            raise FileExtensionError

        with open(file) as f:
            self.header, self.blocks = _read_vamas(f)


def _read_vamas(f: TextIO) -> tuple[VamasHeader, List[VamasBlock]]:
    """Parses a vamas file

    Args:
        f (TextIO): file descripter for a vamas file


    Returns:
        Parsed vamas-file as tuple of :class:`~vamas.vamas_header.VamasHeader`
        a list of :class:`~vamas.vamas_block.VamasBlock`
    """

    h: Dict = {}
    h["format_identifier"] = next(f).strip()

    if (
        h["format_identifier"]
        != "VAMAS Surface Chemical Analysis Standard Data Transfer Format"
        " 1988 May 4"
    ):
        raise VmsIdentifierError

    h["institution_identifier"] = next(f).strip()
    h["instrument_model_identifier"] = next(f).strip()
    h["operator_identifier"] = next(f).strip()
    h["experiment_identifier"] = next(f).strip()

    h["num_lines_comment"] = int(next(f))
    comments = []
    for _ in range(h["num_lines_comment"]):
        comments.append(next(f).strip())
    h["comment"] = "\n".join(comments)

    h["experiment_mode"] = next(f).strip()
    h["scan_mode"] = next(f).strip()

    if h["experiment_mode"] in ["MAP", "MAPD", "NORM", "SDP"]:
        h["num_spectral_regions"] = int(next(f).strip())

    if h["experiment_mode"] in ["MAP", "MAPD"]:
        h["num_analysis_positions"] = int(next(f))
        h["num_discrete_x_coords_in_full_map"] = int(next(f))
        h["num_discrete_y_coords_in_full_map"] = int(next(f))

    h["num_experiment_variables"] = int(next(f))
    h["experiment_variables"] = []
    for _ in range(h["num_experiment_variables"]):
        h["experiment_variables"].append(
            # {"label": next(f).strip(), "unit": next(f).strip()}
            ExperimentVariable(next(f).strip(), next(f).strip())
        )

    h["num_entries_inclusion_exclusion"] = int(next(f))
    h["block_params_includes"] = [
        h["num_entries_inclusion_exclusion"] <= 0 for _ in range(40)
    ]
    for _ in range(abs(h["num_entries_inclusion_exclusion"])):
        h["block_params_includes"][int(next(f)) + 1] = (
            h["num_entries_inclusion_exclusion"] > 0
        )

    h["num_manually_entered_items_in_block"] = int(next(f))

    h["num_future_upgrade_experiment_entries"] = int(next(f))
    h["future_upgrade_experiment_entries"] = []
    for _ in range(h["num_future_upgrade_experiment_entries"]):
        h["future_upgrade_experiment_entries"].append(
            # {"label": next(f).strip(), "unit": next(f).strip()}
            FutureUpgradeExperimentEntry(next(f).strip(), next(f).strip())
        )

    if h["num_future_upgrade_experiment_entries"] != 0:
        print("unsupported future upgrade experiment entries")

    h["num_future_upgrade_block_entries"] = int(next(f))
    if h["num_future_upgrade_block_entries"] != 0:
        print("unsupported future block entries")

    h["num_blocks"] = int(next(f))

    # End of header
    blocks: List[Dict] = []
    for _ in range(h["num_blocks"]):
        include = (
            [True for _ in range(40)]
            if len(blocks) == 0
            else h["block_params_includes"]
        )
        # b = VamasBlock()
        # fb = VamasBlock()
        b: Dict = {}
        fb: Dict = {}

        b["block_identifier"] = next(f).strip()
        b["sample_identifier"] = next(f).strip()

        b["year"] = int(next(f)) if include[0] else fb["year"]
        b["month"] = int(next(f)) if include[1] else fb["month"]
        b["day"] = int(next(f)) if include[2] else fb["day"]
        b["hour"] = int(next(f)) if include[3] else fb["hour"]
        b["minute"] = int(next(f)) if include[4] else fb["minute"]
        b["second"] = int(next(f)) if include[5] else fb["second"]

        b["num_hours_advance_gmt"] = (
            float(next(f)) if include[6] else fb["num_hours_advance_gmt"]
        )

        if include[7]:
            b["num_lines_block_comment"] = int(next(f))
            block_comments = []
            for _ in range(b["num_lines_block_comment"]):
                block_comments.append(next(f).strip())

            b["block_comment"] = "\n".join(block_comments)
        else:
            b["num_lines_block_comment"] = fb["num_lines_block_comment"]
            b["block_comment"] = fb["block_comment"]

        b["technique"] = next(f).strip() if include[8] else fb["technique"]

        if h["experiment_mode"] in ["MAP", "MAPD"]:
            b["x_coord"] = int(next(f)) if include[9] else fb["x_coord"]
            b["y_coord"] = int(next(f)) if include[9] else fb["y_coord"]

        if include[10]:
            b["values_exp_var"] = []
            for _ in range(len(h["experiment_variables"])):
                b["values_exp_var"].append(next(f))
        else:
            b["values_exp_var"] = fb["values_exp_var"]

        b["analysis_source_label"] = (
            next(f).strip() if include[11] else fb["analysis_source_label"]
        )

        if h["experiment_mode"] in ["MAPDP", "MAPSVDP", "SDP", "SDPSV"] or b[
            "technique"
        ] in [
            "SNMS energy spec",
            "FABMS",
            "FABMS energy spec",
            "ISS",
            "SIMS",
            "SIMS energy spec",
            "SNMS",
        ]:
            b["sputtering_z"] = (
                int(next(f)) if include[12] else fb["sputtering_z"]
            )
            b["sputtering_num_particles"] = (
                float(next(f))
                if include[12]
                else fb["sputtering_num_particles"]
            )
            b["sputtering_charge"] = (
                float(next(f).strip())
                if include[12]
                else fb["sputtering_charge"]
            )

        b["analysis_source_characteristic_energy"] = (
            float(next(f))
            if include[13]
            else fb["analysis_source_characteristic_energy"]
        )
        b["analysis_source_strength"] = (
            float(next(f)) if include[14] else fb["analysis_source_strength"]
        )
        b["analysis_source_beam_width_x"] = (
            float(next(f))
            if include[15]
            else fb["analysis_source_beam_width_x"]
        )
        b["analysis_source_beam_width_y"] = (
            float(next(f))
            if include[15]
            else fb["analysis_source_beam_width_y"]
        )

        if h["experiment_mode"] in [
            "MAP",
            "MAPDP",
            "MAPSV",
            "MAPSVDP",
            "SEM",
        ]:
            b["field_view_x"] = (
                float(next(f)) if include[16] else fb["field_view_x"]
            )
            b["field_view_y"] = (
                float(next(f)) if include[16] else fb["field_view_y"]
            )

        if h["experiment_mode"] in ["MAPSV", "MAPSVDP", "SEM"]:
            if include[17]:
                b["linescan_coordinates"] = LinescanCoordinates(
                    first_linescan_start_x=int(next(f)),
                    first_linescan_start_y=int(next(f)),
                    first_linescan_finish_x=int(next(f)),
                    first_linescan_finish_y=int(next(f)),
                    last_linescan_finish_x=int(next(f)),
                    last_linescan_finish_y=int(next(f)),
                )
            else:
                b["linescan_coordinates"] = fb["linescan_coordinates"]

        b["analysis_source_polar_incidence_angle"] = (
            float(next(f))
            if include[18]
            else fb["analysis_source_polar_incidence_angle"]
        )
        b["analysis_source_azimuth"] = (
            float(next(f)) if include[19] else fb["analysis_source_azimuth"]
        )
        b["analyzer_mode"] = (
            next(f).strip() if include[20] else fb["analyzer_mode"]
        )

        b["analyzer_pass_energy_or_retard_ratio_or_mass_res"] = (
            float(next(f))
            if include[21]
            else fb["analyzer_pass_energy_or_retard_ratio_or_mass_res"]
        )

        if b["technique"] == "AES diff":
            b["differential_width"] = (
                float(next(f)) if include[22] else fb["differential_width"]
            )

        b["magnification_analyzer_transfer_lens"] = (
            float(next(f))
            if include[23]
            else fb["magnification_analyzer_transfer_lens"]
        )
        b["analyzer_work_function_or_acceptance_energy"] = (
            float(next(f))
            if include[24]
            else fb["analyzer_work_function_or_acceptance_energy"]
        )

        b["target_bias"] = float(next(f)) if include[25] else fb["target_bias"]

        b["analysis_width_x"] = (
            float(next(f)) if include[26] else fb["analysis_width_x"]
        )
        b["analysis_width_y"] = (
            float(next(f)) if include[26] else fb["analysis_width_y"]
        )

        b["analyzer_axis_take_off_polar_angle"] = (
            float(next(f))
            if include[27]
            else fb["analyzer_axis_take_off_polar_angle"]
        )
        b["analyzer_axis_take_off_azimuth"] = (
            float(next(f))
            if include[27]
            else fb["analyzer_axis_take_off_azimuth"]
        )

        b["species_label"] = (
            next(f).strip() if include[28] else fb["species_label"]
        )

        b["transition_or_charge_state_label"] = (
            next(f).strip()
            if include[29]
            else fb["transition_or_charge_state_label"]
        )
        b["charge_detected_particle"] = (
            int(next(f)) if include[29] else fb["charge_detected_particle"]
        )

        if h["scan_mode"] != "REGULAR":
            print("Only REGULAR scans supported")

        b["x_label"] = next(f).strip() if include[30] else fb["x_label"]
        b["x_units"] = next(f).strip() if include[30] else fb["x_units"]

        b["x_start"] = float(next(f)) if include[30] else fb["x_start"]
        b["x_step"] = float(next(f)) if include[30] else fb["x_step"]

        if include[31]:
            b["num_corresponding_variables"] = int(next(f))
            b["corresponding_variables"] = []
            for _ in range(b["num_corresponding_variables"]):
                b["corresponding_variables"].append(
                    CorrespondingVariable(
                        label=next(f).strip(),
                        unit=next(f).strip(),
                        y_values=[],
                    )
                )

        else:
            b["num_corresponding_variables"] = fb[
                "num_corresponding_variables"
            ]
            assert fb["corresponding_variables"] is not None
            b["corresponding_variables"] = fb["corresponding_variables"].copy()

        b["signal_mode"] = (
            next(f).strip() if include[32] else fb["signal_mode"]
        )

        b["signal_collection_time"] = (
            float(next(f)) if include[33] else fb["signal_collection_time"]
        )

        b["num_scans_to_compile_block"] = (
            int(next(f)) if include[34] else fb["num_scans_to_compile_block"]
        )

        b["signal_time_correction"] = (
            float(next(f)) if include[35] else fb["signal_time_correction"]
        )

        if h["experiment_mode"] in ["MAPDP", "MAPSVDP", "SDP", "SDPSV"] and b[
            "technique"
        ] in [
            "AES diff",
            "AES dir",
            "EDX",
            "ELS",
            "UPS",
            "XRF",
        ]:
            if include[36]:
                b["sputtering_source"] = SputteringSource(
                    energy=float(next(f)),
                    beam_current=float(next(f)),
                    width_x=float(next(f)),
                    width_y=float(next(f)),
                    polar_incidence_angle=float(next(f)),
                    azimuth=float(next(f)),
                    mode=next(f).strip(),
                )
            else:
                b["sputtering_source"] = fb["sputtering_source"]

        b["sample_normal_polar_angle_tilt"] = (
            float(next(f))
            if include[37]
            else fb["sample_normal_polar_angle_tilt"]
        )

        b["sample_normal_tilt_azimuth"] = (
            float(next(f)) if include[37] else fb["sample_normal_tilt_azimuth"]
        )

        b["sample_rotation_angle"] = (
            float(next(f)) if include[38] else fb["sample_rotation_angle"]
        )

        if include[39]:
            b["num_additional_numerical_params"] = int(next(f))
            b["additional_numerical_params"] = []
            for _ in range(b["num_additional_numerical_params"]):
                b["additional_numerical_params"].append(
                    AdditionalNumericalParam(
                        label=next(f).strip(),
                        unit=next(f).strip(),
                        value=float(next(f)),
                    )
                )
        else:
            b["num_additional_numerical_params"] = fb[
                "num_additional_numerical_params"
            ]
            b["additional_numerical_params"] = fb[
                "additional_numerical_params"
            ]

        b["num_y_values"] = int(next(f))
        for corres_var in b["corresponding_variables"]:
            corres_var.y_min = float(next(f))
            corres_var.y_max = float(next(f))

        for _ in range(
            int(b["num_y_values"] / len(b["corresponding_variables"]))
        ):
            for corres_var in b["corresponding_variables"]:
                corres_var.y_values.append(float(next(f)))

        blocks.append(b)
        fb = blocks[0]

    return VamasHeader(**h), [VamasBlock(**item) for item in blocks]
