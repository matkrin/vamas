from typing import List

from .vamas_header import VamasHeader
from .vamas_block import VamasBlock


class Vamas:
    def __init__(self, file: str):
        self.header, self.blocks = read_vamas(file)


def read_vamas(file: str) -> tuple[VamasHeader, List[VamasBlock]]:
    with open(file) as f:
        h = VamasHeader()
        h.format_identifier = next(f).strip()
        h.institution_identifier = next(f).strip()
        h.instrument_model_identifier = next(f).strip()
        h.operator_identifier = next(f).strip()
        h.experiment_identifier = next(f).strip()

        h.num_lines_comments = int(next(f))
        comments = []
        for _ in range(h.num_lines_comments):
            comments.append(next(f).strip())
        h.comments = "\n".join(comments)

        h.experiment_mode = next(f).strip()
        h.scan_mode = next(f).strip()

        if any(x in h.experiment_mode for x in ["MAP", "MAPD", "NORM", "SDP"]):
            h.num_spectral_regions = int(next(f).strip())

        if any(x in h.experiment_mode for x in ["MAP", "MAPD"]):
            h.num_analysis_positions = int(next(f))
            h.num_discrete_x_coords_in_full_map = int(next(f))
            h.num_discrete_y_coords_in_full_map = int(next(f))

        h.num_experiment_variables = int(next(f))
        h.experiment_variables = []
        for _ in range(h.num_experiment_variables):
            h.experiment_variables.append(
                {"label": next(f).strip(), "unit": next(f).strip()}
            )

        h.num_entries_inclusion_exclusion = int(next(f))
        h.block_params_includes = [
            h.num_entries_inclusion_exclusion <= 0 for _ in range(40)
        ]
        for _ in range(abs(h.num_entries_inclusion_exclusion)):
            h.block_params_includes[int(next(f)) + 1] = (
                h.num_entries_inclusion_exclusion > 0
            )

        h.num_manually_entered_items_in_block = int(next(f))

        h.num_future_upgrade_experiment_entries = int(next(f))
        h.future_upgrade_experiment_entries = []
        for _ in range(h.num_future_upgrade_experiment_entries):
            h.future_upgrade_experiment_entries.append(
                {"label": next(f).strip(), "unit": next(f).strip()}
            )

        if h.num_future_upgrade_experiment_entries != 0:
            print("unsupported future upgrade experiment entries")

        h.num_future_upgrade_block_entries = int(next(f))
        if h.num_future_upgrade_block_entries != 0:
            print("unsupported future block entries")

        h.num_blocks = int(next(f))

        # End of header
        blocks = []
        for _ in range(h.num_blocks):
            includes = (
                [True for _ in range(40)]
                if len(blocks) == 0
                else h.block_params_includes
            )
            b = VamasBlock()
            fb = VamasBlock()

            b.block_identifier = next(f).strip()
            b.sample_identifier = next(f).strip()

            b.year = int(next(f)) if includes[0] else fb.year
            b.month = int(next(f)) if includes[1] else fb.month
            b.day = int(next(f)) if includes[2] else fb.day
            b.hour = int(next(f)) if includes[3] else fb.hour
            b.minute = int(next(f)) if includes[4] else fb.minute
            b.second = int(next(f)) if includes[5] else fb.second

            b.num_advance_gmt = (
                int(next(f)) if includes[6] else fb.num_advance_gmt
            )

            if includes[7]:
                b.num_block_comments = int(next(f))
                block_comments = []
                for _ in range(b.num_block_comments):
                    block_comments.append(next(f).strip())

                b.block_comment = "\n".join(block_comments)
            else:
                b.num_block_comments = fb.num_block_comments
                b.block_comment = fb.block_comment

            b.technique = next(f).strip() if includes[8] else fb.technique

            if any(x in h.experiment_mode for x in ["MAP", "MAPD"]):
                b.x_coord = int(next(f)) if includes[9] else fb.x_coord
                b.y_coord = int(next(f)) if includes[9] else fb.y_coord

            if includes[10]:
                b.values_exp_var = []
                for _ in range(len(h.experiment_variables)):
                    b.values_exp_var.append(next(f))
            else:
                b.values_exp_var = fb.values_exp_var

            b.analysis_source_label = (
                next(f).strip() if includes[11] else fb.analysis_source_label
            )

            if any(
                x in h.experiment_mode
                for x in ["MAPDP", "MAPSVDP", "SDP", "SDPSV"]
            ) or any(
                x in b.technique
                for x in [
                    "SNMS energy spec",
                    "FABMS",
                    "FABMS energy spec",
                    "ISS",
                    "SIMS",
                    "SIMS energy spec",
                    "SNMS",
                ]
            ):
                b.sputtering_z = (
                    int(next(f)) if includes[12] else fb.sputtering_z
                )
                b.sputtering_num_particles = (
                    float(next(f))
                    if includes[12]
                    else fb.sputtering_num_particles
                )
                b.sputtering_charge = (
                    float(next(f).strip())
                    if includes[12]
                    else fb.sputtering_charge
                )

            b.analysis_source_char_energy = (
                float(next(f))
                if includes[13]
                else fb.analysis_source_char_energy
            )
            b.analysis_source_strength = (
                float(next(f)) if includes[14] else fb.analysis_source_strength
            )
            b.analysis_source_beam_width_x = (
                float(next(f))
                if includes[15]
                else fb.analysis_source_beam_width_x
            )
            b.analysis_source_beam_width_y = (
                float(next(f))
                if includes[15]
                else fb.analysis_source_beam_width_y
            )

            if any(
                x in h.experiment_mode
                for x in ["MAP", "MAPDP", "MAPSV", "MAPSVDP", "SEM"]
            ):
                b.field_view_x = (
                    float(next(f)) if includes[16] else fb.field_view_x
                )
                b.field_view_y = (
                    float(next(f)) if includes[16] else fb.field_view_y
                )

            # includes 16 or 17 ???
            if any(
                x in h.experiment_mode for x in ["MAPSV", "MAPSVDP", "SEM"]
            ):
                b.first_linescan_start_x = (
                    float(next(f))
                    if includes[17]
                    else fb.first_linescan_start_x
                )
                b.first_linescan_start_y = (
                    float(next(f))
                    if includes[17]
                    else fb.first_linescan_start_y
                )
                b.first_linescan_finish_x = (
                    float(next(f))
                    if includes[17]
                    else fb.first_linescan_finish_x
                )
                b.first_linescan_finish_y = (
                    float(next(f))
                    if includes[17]
                    else fb.first_linescan_finish_y
                )
                b.last_linescan_start_x = (
                    float(next(f))
                    if includes[17]
                    else fb.last_linescan_start_x
                )
                b.last_linescan_start_y = (
                    float(next(f))
                    if includes[17]
                    else fb.last_linescan_start_y
                )

            b.analysis_source_polar_incidence_angle = (
                float(next(f))
                if includes[18]
                else fb.analysis_source_polar_incidence_angle
            )
            b.analysis_source_azimuth = (
                float(next(f)) if includes[19] else fb.analysis_source_azimuth
            )
            b.analyzer_mode = (
                next(f).strip() if includes[20] else fb.analyzer_mode
            )

            b.analyzer_pass_energy_retard_ratio_mass_res = (
                float(next(f))
                if includes[21]
                else fb.analyzer_pass_energy_retard_ratio_mass_res
            )

            if b.technique == "AES diff":
                b.differential_width = (
                    next(f) if includes[22] else fb.differential_width
                )

            b.magnification_analyzer_transfer_lens = (
                float(next(f))
                if includes[23]
                else fb.magnification_analyzer_transfer_lens
            )
            b.analyzer_work_function_or_acceptance_energy = (
                float(next(f))
                if includes[24]
                else fb.analyzer_work_function_or_acceptance_energy
            )

            b.target_bias = float(next(f)) if includes[25] else fb.target_bias

            b.analysis_width_x = (
                float(next(f)) if includes[26] else fb.analysis_width_x
            )
            b.analysis_width_y = (
                float(next(f)) if includes[26] else fb.analysis_width_y
            )

            b.analyzer_axis_take_off_polar_angle = (
                float(next(f))
                if includes[27]
                else fb.analyzer_axis_take_off_polar_angle
            )
            b.analyzer_axis_take_off_azimuth = (
                float(next(f))
                if includes[27]
                else fb.analyzer_axis_take_off_azimuth
            )

            b.species_label = (
                next(f).strip() if includes[28] else fb.species_label
            )

            b.transition_or_charge_state_label = (
                next(f).strip()
                if includes[29]
                else fb.transition_or_charge_state_label
            )
            b.charge_detected_particle = (
                float(next(f)) if includes[29] else fb.charge_detected_particle
            )

            if h.scan_mode != "REGULAR":
                print("Only REGULAR scans supported")

            b.x_label = next(f).strip() if includes[30] else fb.x_label
            b.x_units = next(f).strip() if includes[30] else fb.x_units

            # 30 or 31
            b.x_start = float(next(f)) if includes[31] else fb.x_start
            b.x_step = float(next(f)) if includes[31] else fb.x_step

            if includes[31]:
                b.num_corresponding_variables = int(next(f))
                b.corresponding_variables = []
                for _ in range(b.num_corresponding_variables):
                    b.corresponding_variables.append(
                        {
                            "label": next(f).strip(),
                            "unit": next(f).strip(),
                            "array": [],
                        }
                    )

            else:
                b.num_corresponding_variables = fb.num_corresponding_variables
                b.corresponding_variables = fb.corresponding_variables.copy()

            b.signal_mode = next(f).strip() if includes[32] else fb.signal_mode

            b.signal_collection_time = (
                float(next(f)) if includes[33] else fb.signal_collection_time
            )

            b.num_scans_to_compile_block = (
                int(next(f)) if includes[34] else fb.num_scans_to_compile_block
            )

            b.signal_time_correction = (
                float(next(f)) if includes[35] else fb.signal_time_correction
            )

            if any(
                x in h.experiment_mode
                for x in ["MAPDP", "MAPSVDP", "SDP", "SDPSV"]
            ) and any(
                x in b.technique
                for x in ["AES diff", "AES dir", "EDX", "ELS", "UPS", "XRF"]
            ):
                b.sputtering_source_energy = (
                    float(next(f))
                    if includes[36]
                    else fb.sputtering_source_energy
                )
                b.sputtering_source_beam_current = (
                    float(next(f))
                    if includes[36]
                    else fb.sputtering_source_beam_current
                )
                b.sputtering_source_width_x = (
                    float(next(f))
                    if includes[36]
                    else fb.sputtering_source_width_x
                )
                b.sputtering_source_width_y = (
                    float(next(f))
                    if includes[36]
                    else fb.sputtering_source_width_y
                )
                b.sputtering_source_polar_angle_incidence = (
                    float(next(f))
                    if includes[36]
                    else fb.sputtering_source_polar_angle_incidence
                )
                b.sputtering_source_azimuth = (
                    float(next(f))
                    if includes[36]
                    else fb.sputtering_source_azimuth
                )
                b.sputtering_mode = (
                    next(f).strip() if includes[36] else fb.sputtering_mode
                )

            b.sample_normal_polar_angle_tilt = (
                float(next(f))
                if includes[37]
                else fb.sample_normal_polar_angle_tilt
            )

            b.sample_normal_tilt_azimuth = (
                float(next(f))
                if includes[37]
                else fb.sample_normal_tilt_azimuth
            )

            b.sample_rotation_angle = (
                float(next(f)) if includes[38] else fb.sample_rotation_angle
            )

            if includes[39]:
                b.num_additional_numerical_params = int(next(f))
                b.additional_numerical_params = []
                for _ in range(b.num_additional_numerical_params):
                    b.additional_numerical_params.append(
                        {
                            "label": next(f).strip(),
                            "unit": next(f).strip(),
                            "value": next(f),
                        }
                    )
            else:
                b.num_additional_numerical_params = (
                    fb.num_additional_numerical_params
                )
                b.additional_numerical_params = fb.additional_numerical_params

            b.num_y_values = int(next(f))
            for corres_var in b.corresponding_variables:
                corres_var["y_min"] = float(next(f))
                corres_var["y_max"] = float(next(f))

            for _ in range(
                int(b.num_y_values / len(b.corresponding_variables))
            ):
                for corres_var in b.corresponding_variables:
                    corres_var["array"].append(float(next(f)))

            blocks.append(b)
            fb = blocks[0]

        return h, blocks
