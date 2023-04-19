from dateutil.relativedelta import relativedelta
from edc_constants.constants import YES
from edc_crf.crf_form_validator_mixins import CrfFormValidatorMixin
from edc_dx_review.constants import DRUGS, INSULIN
from edc_dx_review.medical_date import DxDate, MedicalDateError, RxDate
from edc_dx_review.utils import raise_if_clinical_review_does_not_exist
from edc_form_validators import INVALID_ERROR
from edc_form_validators.form_validator import FormValidator
from edc_glucose.form_validators import GlucoseFormValidatorMixin


class DmInitialReviewFormValidator(
    GlucoseFormValidatorMixin,
    CrfFormValidatorMixin,
    FormValidator,
):
    fasting_fld = "glucose_fasting"

    def clean(self):
        raise_if_clinical_review_does_not_exist(self.cleaned_data.get("subject_visit"))

        try:
            dx_date = DxDate(self.cleaned_data)
        except MedicalDateError as e:
            self.raise_validation_error(e.message_dict, e.code)

        self.m2m_other_specify(m2m_field="managed_by", field_other="managed_by_other")

        selections = self.get_m2m_selected("managed_by")
        on_medications = {DRUGS, INSULIN}.intersection(set(selections))
        if on_medications and not (
            self.cleaned_data.get("rx_init_date") or self.cleaned_data.get("rx_init_ago")
        ):
            self.raise_validation_error(
                {"rx_init_date": "This field is required (or the below)."},
                INVALID_ERROR,
            )
        self.not_required_if_true(not on_medications, "rx_init_date")
        self.not_required_if_true(not on_medications, "rx_init_ago")

        try:
            RxDate(self.cleaned_data, reference_date=dx_date)
        except MedicalDateError as e:
            self.raise_validation_error(e.message_dict, e.code)

        self.required_if(YES, field="glucose_performed", field_required="glucose_date")

        self.validate_glucose_test()

        self.validate_test_date_within_6m(date_fld="glucose_date")

    def validate_test_date_within_6m(self: FormValidator, date_fld: str):
        if self.cleaned_data.get(date_fld) and self.cleaned_data.get("report_datetime"):
            try:
                dt = self.cleaned_data.get(date_fld).date()
            except AttributeError:
                dt = self.cleaned_data.get(date_fld)
            report_datetime = self.cleaned_data.get("report_datetime").date()
            rdelta = relativedelta(report_datetime, dt)
            months = rdelta.months + (12 * rdelta.years)
            if months >= 6 or months < 0:
                if months < 0:
                    msg = "Invalid. Cannot be a future date."
                else:
                    msg = f"Invalid. Must be within the last 6 months. Got {abs(months)}m ago."
                self.raise_validation_error(
                    {date_fld: msg},
                    INVALID_ERROR,
                )
