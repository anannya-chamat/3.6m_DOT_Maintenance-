
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
