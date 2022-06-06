from dataclasses import dataclass
from typing import Optional, List


@dataclass
class LinescanCoordinates:
    first_linescan_start_x: int
    first_linescan_start_y: int
    first_linescan_finish_x: int
    first_linescan_finish_y: int
    last_linescan_finish_x: int
    last_linescan_finish_y: int


@dataclass
class SputteringSource:
    energy: float
    beam_current: float
    width_x: float
    width_y: float
    polar_incidence_angle: float
    azimuth: float
    mode: str


@dataclass
class CorrespondingVariable:
    label: str
    unit: str
    y_values: List[float]
    y_min: Optional[float] = None
    y_max: Optional[float] = None


@dataclass
class AdditionalNumericalParam:
    label: str
    unit: str
    value: float


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
    num_hours_advance_gmt: Optional[float] = None

    num_lines_block_comment: Optional[int] = None
    block_comment: Optional[str] = None

    technique: Optional[str] = None

    x_coord: Optional[int] = None
    y_coord: Optional[int] = None

    values_exp_var: Optional[List] = None

    analysis_source_label: Optional[str] = None

    sputtering_z: Optional[int] = None
    sputtering_num_particles: Optional[float] = None
    sputtering_charge: Optional[float] = None

    analysis_source_characteristic_energy: Optional[float] = None
    analysis_source_strength: Optional[float] = None
    analysis_source_beam_width_x: Optional[float] = None
    analysis_source_beam_width_y: Optional[float] = None

    field_view_x: Optional[float] = None
    field_view_y: Optional[float] = None

    linescan_coordinates: Optional[LinescanCoordinates] = None

    analysis_source_polar_incidence_angle: Optional[float] = None
    analysis_source_azimuth: Optional[float] = None

    analyzer_mode: Optional[str] = None

    analyzer_pass_energy_or_retard_ratio_or_mass_res: Optional[float] = None
    differential_width: Optional[float] = None

    magnification_analyzer_transfer_lens: Optional[float] = None
    analyzer_work_function_or_acceptance_energy: Optional[float] = None

    target_bias: Optional[float] = None

    analysis_width_x: Optional[float] = None
    analysis_width_y: Optional[float] = None
    analyzer_axis_take_off_polar_angle: Optional[float] = None
    analyzer_axis_take_off_azimuth: Optional[float] = None

    species_label: Optional[str] = None
    transition_or_charge_state_label: Optional[str] = None

    charge_detected_particle: Optional[int] = None

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

    sputtering_source: Optional[SputteringSource] = None

    sample_normal_polar_angle_tilt: Optional[float] = None
    sample_normal_tilt_azimuth: Optional[float] = None
    sample_rotation_angle: Optional[float] = None

    num_additional_numerical_params: Optional[int] = None
    additional_numerical_params: Optional[
        List[AdditionalNumericalParam]
    ] = None

    num_y_values: Optional[int] = None
