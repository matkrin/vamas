from dataclasses import dataclass
from typing import Optional, List


@dataclass
class VamasHeader:
    format_identifier: Optional[str] = None
    institution_identifier: Optional[str] = None
    instrument_model_identifier: Optional[str] = None
    operator_identifier: Optional[str] = None
    experiment_identifier: Optional[str] = None
    num_lines_comments: Optional[int] = None
    comments: Optional[str] = None
    experiment_mode: Optional[str] = None
    scan_mode: Optional[str] = None
    num_spectral_regions: Optional[int] = None
    num_analysis_positions: Optional[int] = None
    num_discrete_x_coords_in_full_map: Optional[int] = None
    num_discrete_y_coords_in_full_map: Optional[int] = None
    num_experiment_variables: Optional[int] = None
    experiment_variables: Optional[List[dict[str, str]]] = None
    num_entries_inclusion_exclusion: Optional[int] = None
    block_params_includes: Optional[List[bool]] = None
    num_manually_entered_items_in_block: Optional[int] = None
    num_future_upgrade_experiment_entries: Optional[int] = None
    future_upgrade_experiment_entries: Optional[List[dict[str, str]]] = None
    num_future_upgrade_block_entries: Optional[int] = None
    num_blocks: Optional[int] = None
