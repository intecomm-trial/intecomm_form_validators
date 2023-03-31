from django_mock_queries.query import MockModel


class SubjectScreeningMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "SubjectScreening"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_screening.subjectscreening"

    def __str__(self):
        return str(self.screening_identifier)


class PatientGroupMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "PatientGroup"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_screening.patientgroup"
        self.user_created = "frisco"
        self.user_modified = "frisco"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self) -> str:
        return "absolute_url"

    def get_changelist_url(self, search_term=None) -> str:
        return "changelist_url"

    def refresh_from_db(self):
        pass


class PatientLogMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "PatientLog"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_screening.patientlog"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self) -> str:
        return "absolute_url"

    def get_changelist_url(self, search_term=None) -> str:
        return "changelist_url"


class ConditionsMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "Conditions"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_list.condition"


class SocialHarmsMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "SocialHarms"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_subject.socialharms"


class VitalsMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "Vitals"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_subject.vitals"


class AppointmentMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "Appointment"
        super().__init__(*args, **kwargs)
        self.visit_schedule_name = "visit_schedule"
        self._meta.label_lower = "edc_appointment.appointment"


class SubjectVisitMockModel(MockModel):
    def __init__(self, appointment, *args, **kwargs):
        kwargs["mock_name"] = "SubjectVisit"
        super().__init__(*args, **kwargs)
        self.appointment = appointment
        self.visit_schedule_name = appointment.visit_schedule_name
        self.schedule_name = appointment.schedule_name
        self.report_datetime = appointment.appt_datetime
        self._meta.label_lower = "intecomm_subject.subjectvisit"


class DmInitialReviewMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "DmInitialReview"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_subject.dminitialreview"


class HivInitialReviewMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "HivInitialReview"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_subject.hivinitialreview"


class HtnInitialReviewMockModel(MockModel):
    def __init__(self, *args, **kwargs):
        kwargs["mock_name"] = "HtnInitialReview"
        super().__init__(*args, **kwargs)
        self._meta.label_lower = "intecomm_subject.htninitialreview"
