import math

from modules.lightning_modules.ed.individual import (
    EDExclusive,
    MedReconExclusive,
    PYXISExclusive,
    VitalSignExclusive,
)
from modules.lightning_modules.ed_cxr.freeze_encoder_partial_warm_start_optimiser import (
    FreezeEncoderPartialWarmStartOptimiser,
)
from modules.lightning_modules.ed_cxr.report_gen_rev_f import MIMICIVEDCXRReportGen
from modules.transformers.cxrmate_ed.records import EDCXRSubjectRecords


class NoPrompt(MIMICIVEDCXRReportGen):

    def __init__(self, database_path, **kwargs):
        records = EDCXRSubjectRecords(database_path=database_path, time_delta_map=lambda x: 1 / math.sqrt(x + 1))

        records.ed_module_tables = {}
        records.mimic_cxr_tables = {k: records.mimic_cxr_tables[k] for k in ['mimic_cxr_sectioned']}
        records.mimic_cxr_tables['mimic_cxr_sectioned'].text_columns = []

        super().__init__(records=records, add_time_deltas=False, **kwargs)


class NoPromptEDExclusive(EDExclusive):

    def __init__(self, database_path, **kwargs):

        records = EDCXRSubjectRecords(database_path=database_path, time_delta_map=lambda x: 1 / math.sqrt(x + 1))
        records.ed_module_tables = {}
        records.mimic_cxr_tables = {k: records.mimic_cxr_tables[k] for k in ['mimic_cxr_sectioned']}
        records.mimic_cxr_tables['mimic_cxr_sectioned'].text_columns = []
        super().__init__(records=records, add_time_deltas=False, **kwargs)


class NoPromptMedReconExclusive(MedReconExclusive):

    def __init__(self, database_path, **kwargs):

        records = EDCXRSubjectRecords(database_path=database_path, time_delta_map=lambda x: 1 / math.sqrt(x + 1))
        records.ed_module_tables = {}
        records.mimic_cxr_tables = {k: records.mimic_cxr_tables[k] for k in ['mimic_cxr_sectioned']}
        records.mimic_cxr_tables['mimic_cxr_sectioned'].text_columns = []
        super().__init__(records=records, add_time_deltas=False, **kwargs)


class NoPromptVitalSignExclusive(VitalSignExclusive):

    def __init__(self, database_path, **kwargs):

        records = EDCXRSubjectRecords(database_path=database_path, time_delta_map=lambda x: 1 / math.sqrt(x + 1))
        records.ed_module_tables = {}
        records.mimic_cxr_tables = {k: records.mimic_cxr_tables[k] for k in ['mimic_cxr_sectioned']}
        records.mimic_cxr_tables['mimic_cxr_sectioned'].text_columns = []
        super().__init__(records=records, add_time_deltas=False, **kwargs)


class NoPromptPYXISExclusive(PYXISExclusive):

    def __init__(self, database_path, **kwargs):

        records = EDCXRSubjectRecords(database_path=database_path, time_delta_map=lambda x: 1 / math.sqrt(x + 1))
        records.ed_module_tables = {}
        records.mimic_cxr_tables = {k: records.mimic_cxr_tables[k] for k in ['mimic_cxr_sectioned']}
        records.mimic_cxr_tables['mimic_cxr_sectioned'].text_columns = []
        super().__init__(records=records, add_time_deltas=False, **kwargs)
        
        
    
class NoPrompFreezeEncoderPartialWarmStartOptimiser(FreezeEncoderPartialWarmStartOptimiser):

    def __init__(self, database_path, **kwargs):

        records = EDCXRSubjectRecords(database_path=database_path, time_delta_map=lambda x: 1 / math.sqrt(x + 1))
        records.ed_module_tables = {}
        records.mimic_cxr_tables = {k: records.mimic_cxr_tables[k] for k in ['mimic_cxr_sectioned']}
        records.mimic_cxr_tables['mimic_cxr_sectioned'].text_columns = []
        
        super().__init__(records=records, add_time_deltas=False, **kwargs)
 