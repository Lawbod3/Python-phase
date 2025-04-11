from datetime import date
from datetime import timedelta
class menstrual_method:
    def __init__(self, period_days, flow_days, first_day_of_last_period ):
        self.period_days = period_days
        self.flow_days = flow_days
        self.first_day_of_last_period = first_day_of_last_period

    def get_period_day(self):
        set_date = date.fromisoformat(self.first_day_of_last_period)
        next_period_day = set_date + timedelta(days=self.period_days)
        return next_period_day.isoformat()

    def get_ovulation(self):
        set_date = date.fromisoformat(self.first_day_of_last_period)
        next_period_day = set_date + timedelta(days=self.period_days)
        if self.period_days > 33:
            ovulation = next_period_day + timedelta(days= 21)
        elif self.period_days > 28:
            ovulation = next_period_day + timedelta(days = 16)
        elif self.period_days > 24:
            ovulation = next_period_day + timedelta(days = 14)
        else:
            ovulation = next_period_day + timedelta(days = 9)
        return ovulation.isoformat()

    def get_fertility_period(self):
        set_date = date.fromisoformat(self.get_ovulation())
        next_fertility_day = set_date - timedelta(days=4)
        fertility_end = date.fromisoformat(self.get_ovulation())
        return next_fertility_day.isoformat() + " - " + fertility_end.isoformat()

    def get_flow_days(self):
        set_date = date.fromisoformat(self.get_period_day())
        end_date = set_date + timedelta(days= self.flow_days)
        return set_date.isoformat() + " - " + end_date.isoformat()

    def get_pre_ovulation(self):
        set_date = date.fromisoformat(self.get_period_day())
        input_date = date.fromisoformat(self.get_ovulation())
        end_date = input_date - timedelta(days = 1)
        return set_date.isoformat() + " - " + end_date.isoformat()

    def get_end_of_cycle(self):
        set_date = date.fromisoformat(self.get_period_day())
        input_date = set_date + timedelta(days = self.period_days - 1)
        return  input_date.isoformat()

    def get_post_ovulation(self):
        set_date = date.fromisoformat(self.get_ovulation())
        post_date = set_date + timedelta(days = 1)
        return  post_date.isoformat()+ " - " + self.get_end_of_cycle()

    def get_safe_day(self):
        set_date = date.fromisoformat(self.get_period_day())
        use_date = set_date + timedelta(days = self.flow_days + 1)
        return  set_date.isoformat() + " - " + use_date.isoformat()

    def get_post_ovulation_safe_day(self):
        set_date = date.fromisoformat(self.get_ovulation())
        start_date = set_date + timedelta(days =  1)
        return start_date.isoformat() + " - " + self.get_end_of_cycle()















