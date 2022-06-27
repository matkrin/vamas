from dataclasses import dataclass
from typing import Optional, List


@dataclass
class LinescanCoordinates:
    """

    Inserted if and only if the value of experiment mode is **MAPSV**,
    **MAPSVDP** or **SEM**.
    They are required for specifying the size and shape of the map and for
    relating the order in the scan sequence to the position on the sample.
    In the coordinate system to be used, x-values start at unity at the
    left-hand side of the frame and increase towards the right-hand side,
    and y-values start at unity at the top of the frame and increase towards
    the bottom of the frame, as shown below.

    +----------------+
    | 1, 1      N, 1 |
    |                |
    |                |
    |                |
    | 1, M      N, M |
    +----------------+

    Attributes:
        first_linescan_start_x (int):
        first_linescan_start_y (int):
        first_linescan_finish_x (int):
        first_linescan_finish_y (int):
        last_linescan_finish_x (int):
        last_linescan_finish_y (int):
    """
    first_linescan_start_x: int
    first_linescan_start_y: int
    first_linescan_finish_x: int
    first_linescan_finish_y: int
    last_linescan_finish_x: int
    last_linescan_finish_y: int


@dataclass
class SputteringSource:
    """

    For a sputtering source used in addition to the analysis source, as in
    depth profiling, in AES diff, AES dir, EDX, ELS, UPS, XPS or XRF.
    Inserted if and only if both (1) the value of technique is **AES diff**,
    **AES dir**, **EDX**, **ELS**, **UPS**, **XPS** or **XRF**, and (2) the
    value of *experiment mode* is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**.
    (37)


    Attributes:
        energy (float): Energy in electron volts
        beam_current (float): Current in nanoamps or equivalent for neutrals
        width_x (float): x-width in micrometres at the sample in the plane
            perpendicular to the sputtering source beam
        width_y (float): y-width in micrometres at the sample in the plane
            perpendicular to the sputtering source beam
        polar_incidence_angle (float): degrees from upward z-direction,
            defined by the sample stage
        azimuth (float): degrees clockwise from the y-direction towards the
            operator, defined by the sample stage
        mode (str): 
            The value of sputtering mode is either 'continuous', when
            sputtering continues while spectral data is being recorded, or
            'cyclic', when sputtering is suspended while spectral data is being
            recorded.
    """
    energy: float
    beam_current: float
    width_x: float
    width_y: float
    polar_incidence_angle: float
    azimuth: float
    mode: str


@dataclass
class CorrespondingVariable:
    """
    The number of Occurrences of the above pair of entries is specified by the value of number of
    corresponding variables above. The order in which the pairs of entries appear is the same as the order in
    which the corresponding values of corresponding variable label are given above

    Attributes:
        label (str):
        unit (str):
        y_values (List[float]):
            The number of occurrences of ordinate value is specified by the
            value of *number of ordinate values* above. If the value of *number
            of corresponding variables* is greater than unity then the data is
            sent in the form of successive complete sets, each set consisting
            of an ordinate value for each of the corresponding variables
            arranged in the same order as that in which each value of
            corresponding variable label is given above.
            The minus-sign followed by the empty-sequence indicates that there
            must be at least one ordinate value.
        y_min (float):
            The number of occurrences of entries is specified by the value of
            *number of corresponding variables* above. The order in which the
            entries appear is the same as the order in which the *corresponding
            values of *corresponding variable label* are given.
        y_max (float):
            The number of occurrences of entries is specified by the value of
            *number of corresponding variables* above. The order in which the
            entries appear is the same as the order in which the *corresponding
            values of *corresponding variable label* are given.
    """
    label: str
    unit: str
    y_values: List[float]
    y_min: Optional[float] = None
    y_max: Optional[float] = None


@dataclass
class AdditionalNumericalParam:
    """

    The number of occurrences of AdditionalNumericlaParam is specified by the
    value of *number of additional numerical parameters*

    Attributes:
        label (str): 
        unit (str):
        value (str): 
    """
    label: str
    unit: str
    value: float


@dataclass
class VamasBlock:
    """
    Attributes:
        block_identifier (str):
        sample_identifier (str):

        year (int): Gregorian calendar year, for example, '1987' (01)
        month (int): (02)
        day (int): (03)
        hour (int): 24-hour clock (04)
        minute (int): (05)
        second (int): 
            If the value of any of the above six items is not known the value
            -1 should be entered as a dummy value.
            (06)

        num_hours_advance_gmt (float): Number of hours in advance of Greenwich
            Mean Time
            (07)

        num_lines_block_comment (int): (08)
        block_comment (str): Concatenated comment lines
            (The number of occurrences of comment line is specified by the
            value of number of lines in block comment above.)
            (08)

        technique (str):
            ( AES diff | AES dir | EDX | ELS | FABMS | FABMS energy spec |
            ISS | SIMS | SIMS energy spec | SNMS | SNMS energy spec | UPS |
            XPS | XRF )
            (09)

        x_coord (int):
            The ordinal number, starting with unity, of the point in the array
            along the analysis source deflection system x-axis
            Only inserted if and only if the value of experiment mode is either
            **MAP** or **MAPDI**.
            (10)

        y_coord (int):
            The ordinal number, starting with unity, of the point in the array
            along the analysis source deflection system y-axis.
            Only inserted if and only if the value of experiment mode is either
            **MAP** or **MAPDI**.
            (10)

        values_exp_var (list): Value of experimental variable
            *Value of experimental variable* may be, for example, total time in
            seconds, total etch time in seconds, temperature in Kelvin, energy
            in electron volts or mass in unified atomic mass units.
            The number of occurrences of *value of experimental variable* is
            specified by the value of *number of experimental variables* above,
            and the order in which the values are given is the same as the
            order in which experimental variable label and experimental
            variable units are declared above.
            (11)


        analysis_source_label (str):
            (12)

        sputtering_z (int): sputtering ion or atom atomic number
            Inserted if and only if either (1) the value of *experiment mode*
            is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**, or (2) the value
            of *technique* is **FABMS**, **FABMS energy spec**, **ISS**,
            **SIMS**, **SIMS energy spec**, **SNMS** or **SNMS energy spec**
            (13)
            (13)

        sputtering_num_particles (float): number of atoms in sputtering ion or
            atom particle
            Inserted if and only if either (1) the value of *experiment mode*
            is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**, or (2) the value
            of *technique* is **FABMS**, **FABMS energy spec**, **ISS**,
            **SIMS**, **SIMS energy spec**, **SNMS** or **SNMS energy spec**
            (13)
            (13)

        sputtering_charge (float): sputtering ion or atom charge sign and
            number
            Inserted if and only if either (1) the value of *experiment mode*
            is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**, or (2) the value
            of *technique* is **FABMS**, **FABMS energy spec**, **ISS**,
            **SIMS**, **SIMS energy spec**, **SNMS** or **SNMS energy spec**
            (13)

        analysis_source_characteristic_energy (float): energy in electron volts
            (14)

        analysis_source_strength (float):
            power in watts for XPS and XRF, beam current in nanoamps for AES,
            EDX, ISS, SIMS and SNMS; beam equivalent for FABMS
            (15)

        analysis_source_beam_width_x (float):
            width in micrometres at the sample in the plane perpendicular to
            the source beam
            (16)

        analysis_source_beam_width_y (float):
            width in micrometres at the sample in the plane perpendicular to
            the source beam
            (16)

        field_view_x (float):
            micrometres
            Inserted if and only if the value of experiment mode is **MAP**,
            **MAPDP**, **MAPSV**, **MAPSVDP** or **SEM**
            (17)

        field_view_y (float):
            micrometres
            Inserted if and only if the value of experiment mode is **MAP**,
            **MAPDP**, **MAPSV**, **MAPSVDP** or **SEM**
            (17)

        linescan_coordinates (LinescanCoordinates):
            (18)

        analysis_source_polar_incidence_angle (float):
            Degrees from upward zdirection, defined by the sample stage
            (19)

        analysis_source_azimuth (float):
            Degrees clockwise from the y-direction towards the operator,
            defined by the sample stage
            (20)

        analyzer_mode (str):
            ( FAT | FRR | constant delta m | constant m / delta m )
            (21)

        analyzer_pass_energy_or_retard_ratio_or_mass_res (float):
            Energy in electron volts, mass in amu
            (22)

        differential_width (float):
            Electron volts peak-to-peak for sinusoidal modulation or computer
            differentiation.
            Inserted if and only if the value of technique is **AES diff**.
            (23)

        magnification_analyzer_transfer_lens (float):
            (24)

        analyzer_work_function_or_acceptance_energy (float):
            Positive value for work function in electron volts for AES, ELS,
            ISS, UPS and XPS. The acceptance energy of an ion is the energy
            filter pass energy of the mass spectrometer for FABMS, SIMS and
            SNMS.
            (25)

        target_bias (float):
            In volts, including the sign
            (26)

        analysis_width_x (float):
            The analysis width x is the gated signal width of the source in the
            x-direction in the plane perpendicular to the beam for FABMS,
            FABMS energy spec, ISS, SIMS, SIMS energy spec, SNMS and
            SNMS energy spec, the analyser slit length divided by the
            magnification of the analyser transfer lens to that slit for AES
            diff, AES dir, ELS, UPS and XPS, and is the source width in the
            x-direction for both EDX and XRF.
            *Analysis width x* is in micrometres.
            (27)
        
        analysis_width_y (float):
            The analysis width y is the gated signal width of the source in the
            y-direction in the plane perpendicular to the beam for FABMS,
            FABMS energy spec, ISS, SIMS, SIMS energy spec, SNMS and
            SNMS energy spec, the analyser slit length divided by the
            magnification of the analyser transfer lens to that slit for AES
            diff, AES dir, ELS, UPS and XPS, and is the source width in the
            y-direction for both EDX and XRF.
            *Analysis width y* is in micrometres.
            (27)

        analyzer_axis_take_off_polar_angle (float):
            Degrees from upward z-direction, defined by the sample stage
            (28)

        analyzer_axis_take_off_azimuth (float):
            Degrees clockwise from the y-direction towards the operator,
            defined by the sample stage
            (28)

        species_label (str)
            Elemental symbol or molecular formula
            (29)

        transition_or_charge_state_label (str):
            For example, 'KLL' for AES, '1s' for XPS, '-1' for SIMS.
            (30)

        charge_detected_particle (int):
            For example, -1 for AES and XPS, +1 for positive SIMS.
            (30)


        x_label (str):
            Inserted if and only if the value of scan mode is **REGULAR**
            (31)
        x_units (str):
            TODO: table page 12
            Inserted if and only if the value of scan mode is **REGULAR**
            (31)
        x_start (float):
            Inserted if and only if the value of scan mode is **REGULAR**
            (31)
        x_step (float):
            Inserted if and only if the value of scan mode is **REGULAR**
            (31)

        num_corresponding_variables (int):
            If the data is in the form of sets of corresponding values of two
            or more variables then *number of corresponlding variables* is
            equal to the number of variables, otherwise it is equal to unity.
            (32)

        corresponding_variables (List[CorrespondingVariable]):
            (32)

        signal_mode (str):
            ( analogue | pulse counting )
            Analogue signals, while recorded digitally, may be of either sign
            and have a gain which may be noted in the block comment.
            Pulse counting signals are integers with values equal to or greater
            than zero.
            (33)

        signal_collection_time (float):
            Time in seconds per scan for each channel or array-point, except
            for both EDX and XRF where it is the total spectrum collection time
            (34)

        num_scans_to_compile_block (int):
            (35)

        signal_time_correction (float):
            This is the system dead time, except for EDX and XRF where it is
            the livetime-corrected acquisition time. In the case of a dead
            time, a positive value indicates that the count rate should be
            corrected by dividing by (1 - measured rate x dead time) whereas a 
            negative value indicates a correction by multiplying
            by (exp(true count rate x dead time)).
            *Signal time correction* is in seconds.
            (36)

        sputtering_source (SputteringSource):
            (37)

        sample_normal_polar_angle_tilt (float):
            Degrees from upward z-direction, defined by the sample stage
            (38)

        sample_normal_tilt_azimuth (float):
            Degrees clockwise from the y-direction towards the operator,
            defined by the sample stage
            (38)

        sample_rotation_angle (float):
            Degrees clockwise rotation about the sample normal. If this is
            referenced to a particular direction on the sample this direction
            would be specified in a comment line at item number 8.
            (39)

        num_additional_numerical_params (int):
            (40)
        additional_numerical_params (List[AdditionalNumericalParam]):
            (40)

        num_y_values (int):
            The value of number of ordinate values is equal to product of the
            value of number of corresponding variables and the number of sets
            of corresponding variables to be transferred.
            (40)

    """
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
