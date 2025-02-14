from core_data_modules.cleaners import somali, swahili, Codes
from core_data_modules.cleaners.cleaning_utils import CleaningUtils
from core_data_modules.traced_data import Metadata
from core_data_modules.traced_data.util.fold_traced_data import FoldStrategies

from configuration import code_imputation_functions
from configuration.code_schemes import CodeSchemes
from src.lib.configuration_objects import CodingConfiguration, CodingModes, CodingPlan


def clean_age_with_range_filter(text):
    """
    Cleans age from the given `text`, setting to NC if the cleaned age is not in the range 10 <= age < 100.
    """
    age = swahili.DemographicCleaner.clean_age(text)
    if type(age) == int and 10 <= age < 100:
        return str(age)
        # TODO: Once the cleaners are updated to not return Codes.NOT_CODED, this should be updated to still return
        #       NC in the case where age is an int but is out of range
    else:
        return Codes.NOT_CODED


def get_rqa_coding_plans(pipeline_name):
    return [
        CodingPlan(raw_field="rqa_s01_pilot_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01_pilot_run_id",
                   coda_filename="COVID19_s01e01.json",
                   icr_filename="s01_pilot.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01_PILOT,
                           coded_field="rqa_s01_pilot_coded",
                           analysis_file_key="rqa_s01_pilot_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01_PILOT, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19 s01e01"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),
        
        CodingPlan(raw_field="rqa_s01e01_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01e01_run_id",
                   coda_filename="COVID19_KE_Urban_s01e01.json",
                   icr_filename="s01e01.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E01,
                           coded_field="rqa_s01e01_coded",
                           analysis_file_key="rqa_s01e01_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E01, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19-KE-Urban s01e01"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e02_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01e02_run_id",
                   coda_filename="COVID19_KE_Urban_s01e02.json",
                   icr_filename="s01e02.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E02,
                           coded_field="rqa_s01e02_coded",
                           analysis_file_key="rqa_s01e02_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E02, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19-KE-Urban s01e02"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e03_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01e03_run_id",
                   coda_filename="COVID19_KE_Urban_s01e03.json",
                   icr_filename="s01e03.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E03,
                           coded_field="rqa_s01e03_coded",
                           analysis_file_key="rqa_s01e03_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E03, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19-KE-Urban s01e03"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e04_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01e04_run_id",
                   coda_filename="COVID19_KE_Urban_s01e04.json",
                   icr_filename="s01e04.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E04,
                           coded_field="rqa_s01e04_coded",
                           analysis_file_key="rqa_s01e04_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E04, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19-KE-Urban s01e04"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e05_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01e05_run_id",
                   coda_filename="COVID19_KE_Urban_s01e05.json",
                   icr_filename="s01e05.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E05,
                           coded_field="rqa_s01e05_coded",
                           analysis_file_key="rqa_s01e05_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E05, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19-KE-Urban s01e05"),
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="rqa_s01e06_raw",
                   time_field="sent_on",
                   run_id_field="rqa_s01e06_run_id",
                   coda_filename="COVID19_KE_Urban_s01e06.json",
                   icr_filename="s01e06.csv",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.MULTIPLE,
                           code_scheme=CodeSchemes.S01E06,
                           coded_field="rqa_s01e06_coded",
                           analysis_file_key="rqa_s01e06_",
                           fold_strategy=lambda x, y: FoldStrategies.list_of_labels(CodeSchemes.S01E06, x, y)
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("COVID19-KE-Urban s01e06"),
                   raw_field_fold_strategy=FoldStrategies.concatenate)
    ]


def fold_source(x, y):
    if x["CodeID"] == y["CodeID"]:
        return x
    else:
        return CleaningUtils.make_label_from_cleaner_code(
            CodeSchemes.SOURCE, CodeSchemes.SOURCE.get_code_with_match_value("both"), Metadata.get_call_location()
        ).to_dict()


def get_demog_coding_plans(pipeline_name):
    return [
        CodingPlan(raw_field="source_raw",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.SOURCE,
                           coded_field="source_coded",
                           analysis_file_key="source",
                           fold_strategy=fold_source
                       )
                   ],
                   raw_field_fold_strategy=FoldStrategies.concatenate),

        CodingPlan(raw_field="gender_raw",
                   time_field="gender_time",
                   coda_filename="COVID19_gender.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.GENDER,
                           cleaner=somali.DemographicCleaner.clean_gender,
                           coded_field="gender_coded",
                           analysis_file_key="gender",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("gender"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="age_raw",
                   time_field="age_time",
                   coda_filename="COVID19_age.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE,
                           cleaner=clean_age_with_range_filter,
                           coded_field="age_coded",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE_CATEGORY,
                           coded_field="age_category_coded",
                           analysis_file_key="age_category",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_age_category,
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("age"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(raw_field="location_raw",
                   time_field="location_time",
                   coda_filename="COVID19_location.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.KENYA_COUNTY,
                           coded_field="county_coded",
                           analysis_file_key="county",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.KENYA_CONSTITUENCY,
                           coded_field="constituency_coded",
                           analysis_file_key="constituency",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_kenya_location_codes,
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("location"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal)
    ]


def get_follow_up_coding_plans(pipeline_name):
    return []


def get_ws_correct_dataset_scheme(pipeline_name):
    return CodeSchemes.WS_CORRECT_DATASET
