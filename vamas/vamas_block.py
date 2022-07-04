from dataclasses import dataclass
from typing import Optional, List


@dataclass
class LinescanCoordinates:
    """Information about linescan coordinates in mapping experiments

    Inserted if and only if the value of
    :attr:`VamasHeader.experiment_mode
    <vamas.vamas_header.VamasHeader.experiment_mode>` is **MAPSV**,
    **MAPSVDP** or **SEM**.
    They are required for specifying the size and shape of the map and for
    relating the order in the scan sequence to the position on the sample.
    In the coordinate system to be used, x-values start at unity at the
    left-hand side of the frame and increase towards the right-hand side,
    and y-values start at unity at the top of the frame and increase towards
    the bottom of the frame, as shown below.
    **(18)**

    +------------------+
    | 1, 1        N, 1 |
    |                  |
    |                  |
    |                  |
    | 1, M        N, M |
    +------------------+

    Attributes:
        first_linescan_start_x (int): Start x-value of the first linescan.
        first_linescan_start_y (int): Start y-value of the first linescan.
        first_linescan_finish_x (int): End x-value of the first linescan.
        first_linescan_finish_y (int): End y-value of the first linescan.
        last_linescan_finish_x (int): End x-value of the last linescan.
        last_linescan_finish_y (int): End y-value of the last linescan.

    """

    first_linescan_start_x: int
    first_linescan_start_y: int
    first_linescan_finish_x: int
    first_linescan_finish_y: int
    last_linescan_finish_x: int
    last_linescan_finish_y: int


@dataclass
class SputteringSource:
    """Information about the sputtering source

    For a sputtering source used in addition to the analysis source, as in
    depth profiling.
    Inserted if and only if both (1) the value of :attr:`VamasBlock.technique`
    is **AES diff**, **AES dir**, **EDX**, **ELS**, **UPS**, **XPS** or
    **XRF**, and (2) the value of :attr:`VamasHeader.experiment_mode
    <vamas.vamas_header.VamasHeader.experiment_mode>` is **MAPDP**,
    **MAPSVDP**, **SDP** or **SDPSV**.
    **(37)**


    Attributes:
        energy (float): Energy of the sputtering source in electron volts.
        beam_current (float): Beam current of the sputtering source in nanoamps
            or equivalent for neutrals.
        width_x (float): X-width in micrometres at the sample in the plane
            perpendicular to the sputtering source beam.
        width_y (float): Y-width in micrometres at the sample in the plane
            perpendicular to the sputtering source beam.
        polar_incidence_angle (float): Polar incidence angle in degrees from
            upward z-direction, defined by the sample stage.
        azimuth (float): Azimuth angle in degrees clockwise from the
            y-direction towards the operator, defined by the sample stage
        mode (str): Mode of the sputtering source.
            The value is either 'continuous', when sputtering continues while
            spectral data is being recorded, or 'cyclic', when sputtering is
            suspended while spectral data is being recorded.

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
    """Information about the measured values

    The number of occurrences of :class:`CorrespondingVariable` is specified by
    the value of :attr:`VamasBlock.num_corresponding_variables`.
    The order in which the entries appear is the same as the order in
    which the corresponding values of :attr:`~CorrespondingVariable.label`
    are given.

    Attributes:
        label (str): Label of the corresponding variable.
        unit (str): Unit of the corresponding variable.
        y_values (List[float]): Measured y-values.
            The number of occurrences of ordinate values is specified by the
            value of :attr:`VamasBlock.num_y_values`. If this value is greater
            than unity then the data is sent in the form of successive
            complete sets, each set consisting of an ordinate y_value for each
            of the corresponding variables arranged in the same order as that
            in which each value of :attr:`~CorrespondingVariable.label` is
            given.
            The minus-sign followed by the empty-sequence indicates that there
            must be at least one y value.
        y_min (float): Minimal measured y-value.
            The number of occurrences of entries is specified by the value of
            :attr:`VamasBlock.num_corresponding_variables`. The order in which
            the entries appear is the same as the order in which the
            corresponding values of :attr:`~CorrespondingVariable.label`
            are given.
        y_max (float): Maximal measured y-value.
            The number of occurrences of entries is specified by the value of
            :attr:`VamasBlock.num_corresponding_variables`. The order in which
            the entries appear is the same as the order in which the
            corresponding values of :attr:`~CorrespondingVariable.label`
            are given.
    """

    label: str
    unit: str
    y_values: List[float]
    y_min: Optional[float] = None
    y_max: Optional[float] = None


@dataclass
class AdditionalNumericalParam:
    """Information about additional numerical parameters

    The number of occurrences of AdditionalNumericalParam is specified by the
    value of :attr:`VamasBlock.num_additional_numerical_params`.

    Attributes:
        label (str): Label of the additional numerical parameter.
        unit (str): Unit of the additional numerical parameter.
        value (str): Value of the additional numerical parameter.

    """

    label: str
    unit: str
    value: float


@dataclass
class VamasBlock:
    """Information about a measurement as part of an experiment

    VamasBlock contains the information about one part of the experiment, e.g.
    one spectral region or scan in XPS measurements or one image in an
    SEM experiment.

    Attributes:
        block_identifier (str): Identifier of the block.
        sample_identifier (str): Identifier of the sample.
        year (int): Year of the measurement.
            Gregorian calendar year, e.g., '1987'.
            If the value is not known, the value -1 should be entered as a
            dummy value.
        month (int): Month of the measurement.
            If the value is not known, the value -1 should be entered as a
            dummy value.
        day (int): Day of the measurement.
            If the value is not known, the value -1 should be entered as a
            dummy value.
        hour (int): Hour as part of the measurement time.
            In 24-hour clock format. If the value is not known, the value
            -1 should be entered as a dummy value.
        minute (int): Minute as part of the measurement time.
            If the value is not known, the value -1 should be entered as a
            dummy value.
        second (int): Second as part of the measurement time.
            If the value is not known, the value -1 should be entered as a
            dummy value.
        num_hours_advance_gmt (float): Number of hours in advance of Greenwich
            Mean Time.
        num_lines_block_comment (int): Number of lines of block comments.
        block_comment (str): Concatenated block comment lines.
            The number of occurrences of comment line is specified by the
            value of number of lines in block comment above.
        technique (str): Measurement Technique.
            One of the values 'AES diff' | 'AES dir' | 'EDX' | 'ELS' | 'FABMS'
            | 'FABMS energy spec' | 'ISS' | 'SIMS' | 'SIMS energy spec'
            | 'SNMS' | 'SNMS energy spec' | 'UPS' | 'XPS' | 'XRF'.
        x_coord (int): X-coordinate.
            The ordinal number, starting with unity, of the point in the array
            along the analysis source deflection system x-axis
            Only inserted if and only if the value of experiment mode is either
            **MAP** or **MAPDI**.
        y_coord (int): Y-coordinate.
            The ordinal number, starting with unity, of the point in the array
            along the analysis source deflection system y-axis.
            Only inserted if and only if the value of experiment mode is either
            **MAP** or **MAPDI**.
        values_exp_var (list): Values of experimental variables.
            May be, for example, total time in seconds, total etch time in
            seconds, temperature in Kelvin, energy in electron volts or mass
            in unified atomic mass units.
            The number of items in the list is specified by the value of
            :attr:`VamasBlock.num_experiment_variables
            <vamas.vamas_header.VamasHeader.num_experiment_variables>`,
            and the order in which the values are given is the same as the
            order in which :attr:`ExperimentVariable.label
            <vamas.vamas_header.ExperimentVariable.label>` and
            :attr:`ExperimentVariable.unit
            <vamas.vamas_header.ExperimentVariable.unit>` are declared.
        analysis_source_label (str): Label of the Analysis source.
        sputtering_z (int): Species of the sputtering ion or atom in atomic
            number.
            Inserted if and only if either (1) the value of *experiment mode*
            is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**, or (2) the value
            of *technique* is **FABMS**, **FABMS energy spec**, **ISS**,
            **SIMS**, **SIMS energy spec**, **SNMS** or **SNMS energy spec**.
        sputtering_num_particles (float): Number of particles in sputtering ion
            or atom particle.
            Inserted if and only if either (1) the value of *experiment mode*
            is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**, or (2) the value
            of *technique* is **FABMS**, **FABMS energy spec**, **ISS**,
            **SIMS**, **SIMS energy spec**, **SNMS** or **SNMS energy spec**.
        sputtering_charge (float): Charge sign and number of the sputtering
            ion or atom.
            Inserted if and only if either (1) the value of *experiment mode*
            is **MAPDP**, **MAPSVDP**, **SDP** or **SDPSV**, or (2) the value
            of *technique* is **FABMS**, **FABMS energy spec**, **ISS**,
            **SIMS**, **SIMS energy spec**, **SNMS** or **SNMS energy spec**.
        analysis_source_characteristic_energy (float): Characteristic energy
            of the analysis source in electron volts.
        analysis_source_strength (float): Strengh of the analysis source.
            Power of the analysis source in watts for XPS and XRF, beam current
            in nanoamps for AES, EDX, ISS, SIMS and SNMS; beam equivalent for
            FABMS.
        analysis_source_beam_width_x (float): Width of the beam in
            x-direction in micrometres at the sample in the plane perpendicular
            to the source beam.
        analysis_source_beam_width_y (float): Width of the beam in
            y-direction in micrometres at the sample in the plane perpendicular
            to the source beam.
        field_view_x (float): Field of view in x-direction in micrometres.
            Inserted if and only if the value of experiment mode is **MAP**,
            **MAPDP**, **MAPSV**, **MAPSVDP** or **SEM**.
        field_view_y (float) Field of view in y-direction in micrometres
            Inserted if and only if the value of experiment mode is **MAP**,
            **MAPDP**, **MAPSV**, **MAPSVDP** or **SEM**.
        linescan_coordinates (LinescanCoordinates): Linescan coordinates.
        analysis_source_polar_incidence_angle (float): Incidence angle of
            the analysis source.
            In degrees from upward z-direction, defined by the sample stage.
        analysis_source_azimuth (float): Azimuth angle of the analysis source.
            In degrees clockwise from the y-direction towards the operator,
            defined by the sample stage.
        analyzer_mode (str): Analyzer mode.
            The value is on of  'FAT' | 'FRR' | 'constant delta m'
            | 'constant m / delta m'.
        analyzer_pass_energy_or_retard_ratio_or_mass_res (float): Pass energy
            or retard ration or mass resolution of the analyser.
            The unit for energy is in electron volts, the one for mass in amu.
        differential_width (float): Differential width.
            Electron volts peak-to-peak for sinusoidal modulation or computer
            differentiation.
            Inserted if and only if the value of technique is **AES diff**.
        magnification_analyzer_transfer_lens (float): Magnification of the
            analyzer transfer lens.
        analyzer_work_function_or_acceptance_energy (float): Work function or
            acceptance angle of the analyzer.
            Positive value for work function in electron volts for AES, ELS,
            ISS, UPS and XPS. The acceptance energy of an ion is the energy
            filter pass energy of the mass spectrometer for FABMS, SIMS and
            SNMS.
        target_bias (float): Bias of the target.
            In volts, including the sign.
        analysis_width_x (float): Analysis width in x-direction.
            The analysis width x is the gated signal width of the source in the
            x-direction in the plane perpendicular to the beam for **FABMS**,
            **FABMS energy spec**, **ISS**, **SIMS**, **SIMS energy spec**,
            **SNMS** and **SNMS energy spec**, the analyser slit length divided
            by the magnification of the analyser transfer lens to that slit for
            **AES diff**, **AES dir**, **ELS**, **UPS** and **XPS**, and is the
            source width in the x-direction for both **EDX** and **XRF**.\n
            In micrometres.
        analysis_width_y (float): Analysis width in y-direction.
            The analysis width y is the gated signal width of the source in the
            y-direction in the plane perpendicular to the beam for **FABMS**,
            **FABMS energy spec**, **ISS**, **SIMS**, **SIMS energy spec**,
            **SNMS** and **SNMS energy spec**, the analyser slit length divided
            by the magnification of the analyser transfer lens to that slit for
            **AES diff**, **AES dir**, **ELS**, **UPS** and **yPS**, and is the
            source width in the y-direction for both **EDX** and **XRF**.\n
            In micrometres.
        analyzer_axis_take_off_polar_angle (float): Analyzer axis take off
            polar angle.
            Degrees from upward z-direction, defined by the sample stage.
        analyzer_axis_take_off_azimuth (float): Analyzer axis take off
            azimuth.
            Degrees clockwise from the y-direction towards the operator,
            defined by the sample stage.
        species_label (str): Label of the species.
            Elemental symbol or molecular formula.
        transition_or_charge_state_label (str): Label of the transition or
            charge state.
            For example, 'KLL' for **AES**, '1s' for **XPS**, '-1' for
            **SIMS**.
        charge_detected_particle (int): Charge of the detected particle.
            For example, -1 for **AES** and **XPS**, +1 for positive **SIMS**.
        x_label (str): Label of the x-values.
            Inserted if and only if the value of scan mode is **REGULAR**.
        x_units (str): Unit of the x-values.

            +------------+----------------------------------------------+
            | experiment | unit corresponding to technique              |
            |            |                                              |
            | mode       |                                              |
            |            +------------+------------+--------------------+
            |            | AES diff,  | FABMS,     | FABMS energy spec, |
            |            |            |            |                    |
            |            | AES dir,   | SIMS,      | SIMS energy spec,  |
            |            |            |            |                    |
            |            | EDX, ELSS, | SNMS,      | SNMS energy spec,  |
            |            |            |            |                    |
            |            | ISS, UPS   |            |                    |
            |            |            |            |                    |
            |            | XPS, XRF   |            |                    |
            +------------+------------+------------+--------------------+
            | MAP        | 'eV'       | 'u' or 's' | 'eV'               |
            |            |            |            |                    |
            | MAPDP      |            |            |                    |
            |            |            |            |                    |
            | NORM       |            |            |                    |
            |            |            |            |                    |
            | SDP        |            |            |                    |
            +------------+------------+------------+--------------------+
            | SDPSV      | 's'        | 's'        |                    |
            +------------+------------+------------+--------------------+

            Inserted if and only if the value of scan mode is **REGULAR**.

        x_start (float): Start value of the x-values.
            Inserted if and only if the value of scan mode is **REGULAR**.

        x_step (float): Step size between x-values.
            Inserted if and only if the value of scan mode is **REGULAR**.

        num_corresponding_variables (int): Number of corresponding variables.
            If the data is in the form of sets of corresponding values of two
            or more variables then
            :attr:`~VamasBlock.num_corresponding_variables` is equal to the
            number of variables, otherwise it is equal to unity.
        corresponding_variables (List[CorrespondingVariable]): Corresponding
            Variables.
        signal_mode (str): Signal mode.
            Is either 'analogue' | 'pulse counting'.
            Analogue signals, while recorded digitally, may be of either sign
            and have a gain which may be noted in the block comment.
            Pulse counting signals are integers with values equal to or greater
            than zero.
        signal_collection_time (float): Signal collection time.
            Time in seconds per scan for each channel or array-point, except
            for both **EDX** and **XRF** where it is the total spectrum
            collection time.
        num_scans_to_compile_block (int): Number of scan to compile block.
            This is the number of measurement recordings to get the data block,
            e.g. the number of sweeps for **XPS**.
        signal_time_correction (float): Time correction for the signal.
            This is the system dead time, except for **EDX** and **XRF** where
            it is the livetime-corrected acquisition time. In the case of a
            dead time, a positive value indicates that the count rate should be
            corrected by dividing by (1 - measured rate * dead time) whereas a
            negative value indicates a correction by multiplying
            by (exp(true count rate * dead time)). In seconds.
        sputtering_source (SputteringSource): Sputtering source.
        sample_normal_polar_angle_tilt (float): Sample normal polar angle of
            tilt.
            Degrees from upward z-direction, defined by the sample stage.
        sample_normal_tilt_azimuth (float): Sample normal tilt azimuth.
            Degrees clockwise from the y-direction towards the operator,
            defined by the sample stage.
        sample_rotation_angle (float): Sample rotation angle.
            Degrees clockwise rotation about the sample normal. If this is
            referenced to a particular direction on the sample this direction
            would be specified in a comment line at
            :attr:`~VamasBlock.block_comment`.
        num_additional_numerical_params (int): Number of additional numberical
            parameters.
        additional_numerical_params (List[AdditionalNumericalParam]):
            Additional numberical parameters.
        num_y_values (int): Number of y-values.
            The value of number of y-values (ordinate values) is equal to
            product of the value of
            :attr:`~VamasBlock.num_corresponding_variables` and
            the number of sets of :class:`CorrespondingVariable`s to be
            transferred.

    """

    block_identifier: str
    sample_identifier: str

    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    num_hours_advance_gmt: float

    num_lines_block_comment: int
    block_comment: str

    technique: str

    values_exp_var: List

    analysis_source_label: str

    analysis_source_characteristic_energy: float
    analysis_source_strength: float
    analysis_source_beam_width_x: float
    analysis_source_beam_width_y: float

    analysis_source_polar_incidence_angle: float
    analysis_source_azimuth: float

    analyzer_mode: str

    analyzer_pass_energy_or_retard_ratio_or_mass_res: float

    magnification_analyzer_transfer_lens: float
    analyzer_work_function_or_acceptance_energy: float

    target_bias: float

    analysis_width_x: float
    analysis_width_y: float
    analyzer_axis_take_off_polar_angle: float
    analyzer_axis_take_off_azimuth: float

    species_label: str
    transition_or_charge_state_label: str

    charge_detected_particle: int

    x_label: str
    x_units: str
    x_start: float
    x_step: float

    num_corresponding_variables: int
    corresponding_variables: List[CorrespondingVariable]

    signal_mode: str
    signal_collection_time: float
    num_scans_to_compile_block: int
    signal_time_correction: float

    sample_normal_polar_angle_tilt: float
    sample_normal_tilt_azimuth: float
    sample_rotation_angle: float

    num_additional_numerical_params: int
    additional_numerical_params: List[AdditionalNumericalParam]

    num_y_values: int

    # Optional
    x_coord: Optional[int] = None
    y_coord: Optional[int] = None
    sputtering_z: Optional[int] = None
    sputtering_num_particles: Optional[float] = None
    sputtering_charge: Optional[float] = None
    field_view_x: Optional[float] = None
    field_view_y: Optional[float] = None
    linescan_coordinates: Optional[LinescanCoordinates] = None
    differential_width: Optional[float] = None
    sputtering_source: Optional[SputteringSource] = None
