
class DOT_Maintenance():
    def __init__(self,levels,units,failure_mode,maintenance) -> None:
        self.levels = levels
        self.units = units
        self.failure_mode = failure_mode
        self.maintenance = maintenance

class DOTComponents():
    def __init__(self,sr_no,systems,units,components,replacement_due,failure_mode) -> None:
        self.sr_no = sr_no
        self.systems = systems
        self.units = units
        self.components = components
        self.replacement_due = replacement_due
        self.failure_mode = failure_mode

class DOT_Systems():
    def __init__(self,sr_no,systems,components,replacement_due,failure_mode) -> None:
        self.sr_no = sr_no
        self.systems = systems
        self.components = components
        self.replacement_due = replacement_due
        self.failure_mode = failure_mode

class MaintenanceDataEntry:
    def __init__(self,system,task_detail,completion_date,responsible_user,additional_note):
        self.system=system
        self.task_detail=task_detail
        self.completion_date=completion_date
        self.responsible_user=responsible_user
        self.additional_note=additional_note

    def __str__(self):
        return f"  System: {self.system}\n" \
               f"  Task Detail: {self.task_detail}\n" \
               f"  Completion Date: {self.completion_date}\n" \
               f"  Responsible User: {self.responsible_user}\n" \
               f"  Additional Note: {self.additional_note}"
