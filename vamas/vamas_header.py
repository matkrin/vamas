from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ExperimentVariable:
    """

    The number of occurrences of *ExperimentVariable* is specified by the value
    of *number of experimental variables* in *VamasHeader*.

    Attributes:
        label (str):
        unit (str):
            ( c/s | d | degree | eV | K | micro C | micro m | m/s | n | nA
            | ps | s | u | V )
            These values are abbreviations for the units listed below:

            +---------+-------------------------------------------------------+
            | c/s     | counts per second                                     |
            +---------+-------------------------------------------------------+
            | d       | dimensionless - just a number, eg. counts per channel |
            +---------+-------------------------------------------------------+
            | degree  | angle in degrees                                      |
            +---------+-------------------------------------------------------+
            | eV      | electron volts                                        |
            +---------+-------------------------------------------------------+
            | K       | Kelvin                                                |
            +---------+-------------------------------------------------------+
            | micro C | microcoulombs                                         |
            +---------+-------------------------------------------------------+
            | micro m | micrometres                                           |
            +---------+-------------------------------------------------------+
            | m/s     | metres per second                                     |
            +---------+-------------------------------------------------------+
            | n       | not defined here - may be given in a label            |
            +---------+-------------------------------------------------------+
            | nA      | nanoamps                                              |
            +---------+-------------------------------------------------------+
            | ps      | picoseconds                                           |
            +---------+-------------------------------------------------------+
            | s       | seconds                                               |
            +---------+-------------------------------------------------------+
            | u       | unified atomic mass units                             |
            +---------+-------------------------------------------------------+
            | V       | volts                                                 |
            +---------+-------------------------------------------------------+

    """

    label: str
    unit: str


@dataclass
class FutureUpgradeExperimentEntry:
    """

    The number of occurrences of *FutureUpgradeExperimentEntry* is given by
    the value of *number of future upgrade experiment entries* in
    *VamesHeader*.
    It is defined as a text line so that any integer, real number or text line
    inserted here by a future upgrade of the format can be read as a text line
    then discarded.

    Attributes:
        label (str):
        unit (str):

    """

    label: str
    unit: str


@dataclass
class VamasHeader:
    """
    Attributes:
        format_identifier (str): Format identifier
            'VAMAS Surface Chemical Analysis Standard Data Transfer Format 1988
            May 4'

        institution_identifier (str): Institution identifier

        instrument_model_identifier (str): Instrumental Model Identifier

        operator_identifier (str): Operator Identifier

        experiment_identifier (str): Experiment Identifier

        num_lines_comment (int): Number of lines in comment

        comment (str): Concatenated comment lines
            The comment may include details of the last calibration
            of the instrument

        experiment_mode (str): Experiment mode \n
            ( MAP | MAPDP | MAPSV | MAPSVDP | NORM | SDP | SDPSV | SEM )
            The contents of each block in the experiment are indicated by the
            values of experiment mode as follows:

            - MAP
                A spectrum which refers to a specified point in a
                regular two-dimensional spatial array.
            - MAPDP
                A spectrum which refers to a specified point in a regular
                two-dimensional spatial array and to a specified layer in a
                depth profile.
            - MAPSV
                A complete set of single values of a fixed number of
                variables for every point in a regular two-dimensional spatial
                array. Note that an x linescan consists of a map with the value
                of number of analysis positions equal to the value of number of
                discrete x coordinates available in full map, that is, the
                number of discrete y coordinates is unity; in a y linescan the
                roles of x and y are reversed.
            - MAPSVDP
                A complete set of single values of a fixed number of
                variables for every point in a regular two-dimensional array
                for one layer in a depth profile. Successive blocks refer to
                successive layers in the depth profile.
            - NORM
                Either independent data or data which refers to a
                specified set of single values of one or more experimental
                variables; the data may be spectral or non-spectral.
            - SDP
                A spectrum which refers to a specified layer in a depth
                profile.
            - SDPSV
                A complete set of single values of a fixed number of
                variables for every layer in a depth profile.
            - SEM
                An electron emission intensity for every point in a
                regular two-dimensional spatial array.

        scan_mode (str): Scan Mode
            ( 'REGULAR' | 'IRREGULAR' | 'MAPPING )
            If the value of :attr:`~VamasHeader.experiment_mode` is **MAPSV**,
            **MAPSVDP** or **SEM** then the value of
            :attr:`~VamasHeader.scan_mode` must be **MAPPING**, otherwise if
            the data is in the form of an abscissa start, an abscissa increment
            and a number of complete sets of values of one or more experimental
            variables then the value of :attr:`~VamasHeader.scan_mode` is
            **REGULAR**, otherwise the value of :attr:`~VamasHeader.scan_mode`
            is **IRREGULAR**.

        num_spectral_regions (int): Number of spectral regions
            Normally only one technique is used in an experiment but there may
            be more. The value of *number of spectral regions* is the sum for
            all techniques of the numbers of spectral regions in each
            technique.
            *Number of spectral regions* is inserted if and only if the value
            of *experiment mode* is **MAP**, **MAPDP**, **NORM** or **SDP**.
            (optional-sequence)

        num_analysis_positions (int): Number of analysis positions.
            Inserted if and only if the value of experiment mode is either
            **MAP** or **MAPDP**.
            (optional-sequence)

        num_discrete_x_coords_in_full_map (int): Number of discrete x
            coordinates available in full map.
            Inserted if and only if the value of *experiment mode* is either
            **MAP** or **MAPDP**.
            (optional-sequence)

        num_discrete_y_coords_in_full_map (int): number of discrete y
            coordinates available in full map.
            Inserted if and only if the value of *experiment mode* is either
            **MAP** or **MAPDP**.
            (optional-sequence)

        num_experiment_variables (int): Number of experimental variables
            An experimental variable is a parameter which may be varied from
            block to block through the experiment but which remains constant
            within each block.

        experiment_variables (ExperimentVariable):
            (optional-sequence)

        num_entries_inclusion_exclusion (int): Parameter inclusion or exclusion
            prefix number

        block_params_includes (list of bool):

        num_manually_entered_items_in_block (int): Prefix number of manually
            entered item
            The number of occurrences of *prefix number of manually entered
            item* is specified by the value of *number of manually entered
            items in block* above. If this is greater than zero then the values
            of successive occurrences of *prefix number of manually entered
            item* should be in ascending order. Any of the items preceded by
            prefix numbers in comment brackets in the syntax-rule defining
            *block* which need to be evaluated by the operator and manually
            entered from the keyboard should be included in this list. If an
            item is to be expressed as a real number and the operator is unable
            to supply a value then the computer should enter the value 1E37.
            (repeated-sequence)

        num_future_upgrade_experiment_entries (int): Number of future upgrade
            experiment entries


        future_upgrade_experiment_entries
            (list of FutureUpgradeExperimentEntry):
            List of future upgrade experiment entries.
            The number of occurrences of *future upgrade experiment entry* is
            given by the value of *number of future upgrade experiment entries*
            above. It is defined as a text line so that any integer,
            real number or text line inserted here by a future upgrade of the
            format can be read as a text line then discarded.
            (repeated-sequence)

        num_future_upgrade_block_entries (int):
            *Number of future upgrade experiment entries and number of future
            upgrade block entries* are included in case the format is upgraded
            in the future to include more non-optional, non-repeating
            parameters. The numbers of these new parameters will be entered
            here so that old programs can skip the new parameters in new data,
            and new programs will not try to read the new parameters in old
            data. For the present both of them would be set to zero.

        num_blocks (int): Number of blocks.

    """

    format_identifier: Optional[str] = None
    institution_identifier: Optional[str] = None
    instrument_model_identifier: Optional[str] = None
    operator_identifier: Optional[str] = None
    experiment_identifier: Optional[str] = None
    num_lines_comment: Optional[int] = None
    comment: Optional[str] = None
    experiment_mode: Optional[str] = None
    scan_mode: Optional[str] = None
    num_spectral_regions: Optional[int] = None
    num_analysis_positions: Optional[int] = None
    num_discrete_x_coords_in_full_map: Optional[int] = None
    num_discrete_y_coords_in_full_map: Optional[int] = None
    num_experiment_variables: Optional[int] = None
    experiment_variables: Optional[List[ExperimentVariable]] = None
    num_entries_inclusion_exclusion: Optional[int] = None
    block_params_includes: Optional[List[bool]] = None
    num_manually_entered_items_in_block: Optional[int] = None
    num_future_upgrade_experiment_entries: Optional[int] = None
    future_upgrade_experiment_entries: Optional[
        List[FutureUpgradeExperimentEntry]
    ] = None
    num_future_upgrade_block_entries: Optional[int] = None
    num_blocks: Optional[int] = None
