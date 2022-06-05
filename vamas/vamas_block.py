from dataclasses import dataclass
from typing import Optional, List
import numpy as np


@dataclass
class CorrespondingVariable:
    label: str
    unit: str
    array: List[float]
    y_min: Optional[float] = None
    y_max: Optional[float] = None


@dataclass
class AdditionalNumericalParam:
    label: str
    unit: str
    values: float


@dataclass
class VamasBlock:
    block_identifier: Optional[str] = None
    sample_identifier: Optional[str] = None

    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    second: Optional[int] = None
    num_advance_gmt: Optional[int] = None

    num_block_comments: Optional[int] = None
    block_comment: Optional[str] = None

    technique: Optional[str] = None

    x_coord: Optional[int] = None
    y_coord: Optional[int] = None

    values_exp_var: Optional[List] = None

    analysis_source_label: Optional[str] = None

    sputtering_z: Optional[int] = None
    sputtering_num_particles: Optional[float] = None
    sputtering_charge: Optional[float] = None

    analysis_source_char_energy: Optional[float] = None
    analysis_source_strength: Optional[float] = None
    analysis_source_beam_width_x: Optional[float] = None
    analysis_source_beam_width_y: Optional[float] = None

    field_view_x: Optional[float] = None
    field_view_y: Optional[float] = None

    first_linescan_start_x: Optional[float] = None
    first_linescan_start_y: Optional[float] = None
    first_linescan_finish_x: Optional[float] = None
    first_linescan_finish_y: Optional[float] = None
    last_linescan_start_x: Optional[float] = None
    last_linescan_start_y: Optional[float] = None

    analysis_source_polar_incidence_angle: Optional[float] = None
    analysis_source_azimuth: Optional[float] = None
    analyzer_mode: Optional[str] = None

    analyzer_pass_energy_retard_ratio_mass_res: Optional[float] = None
    differential_width: Optional[str] = None

    magnification_analyzer_transfer_lens: Optional[float] = None
    analyzer_work_function_or_acceptance_energy: Optional[float] = None

    target_bias: Optional[float] = None

    analysis_width_x: Optional[float] = None
    analysis_width_y: Optional[float] = None
    analyzer_axis_take_off_polar_angle: Optional[float] = None
    analyzer_axis_take_off_azimuth: Optional[float] = None

    species_label: Optional[str] = None
    transition_or_charge_state_label: Optional[str] = None

    charge_detected_particle: Optional[float] = None

    x_label: Optional[str] = None
    x_units: Optional[str] = None
    x_start: Optional[float] = None
    x_step: Optional[float] = None
    num_corresponding_variables: Optional[int] = None
    corresponding_variables: Optional[List[CorrespondingVariable]] = None

    signal_mode: Optional[str] = None
    signal_collection_time: Optional[float] = None
    num_scans_to_compile_block: Optional[int] = None
    signal_time_correction: Optional[float] = None

    sputtering_source_energy: Optional[float] = None
    sputtering_source_beam_current: Optional[float] = None
    sputtering_source_width_x: Optional[float] = None
    sputtering_source_width_y: Optional[float] = None
    sputtering_source_polar_angle_incidence: Optional[float] = None
    sputtering_source_azimuth: Optional[float] = None
    sputtering_mode: Optional[str] = None

    sample_normal_polar_angle_tilt: Optional[float] = None
    sample_normal_tilt_azimuth: Optional[float] = None
    sample_rotation_angle: Optional[float] = None

    num_additional_numerical_params: Optional[int] = None
    additional_numerical_params: Optional[
        List[AdditionalNumericalParam]
    ] = None

    num_y_values: Optional[int] = None

    @property
    def data_points(self):
        if (
            self.x_start
            and self.x_step
            and self.num_y_values
            and self.corresponding_variables
        ):
            start = self.x_start
            print(start)
            step = self.x_step
            print(step)
            end = start + self.num_y_values * step
            print(end)
            if step < 0:
                start, end = end, start
                step = -step
            return np.column_stack(
                (
                    np.arange(start, end, step),
                    np.asarray(self.corresponding_variables[0]["array"]),
                )
            )
        return
