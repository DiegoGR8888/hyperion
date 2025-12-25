class OxygenModel:
    def __init__(
        self,
        O2_init=100.0,
        consumption_rate=0.3,
        activity_factor=1.0,
        critical_threshold=30.0
    ):
        self.O2 = O2_init
        self.consumption_rate = consumption_rate
        self.activity_factor = activity_factor
        self.critical_threshold = critical_threshold
        self.time = 0

    def step(self, dt=1.0):
        consumption = self.consumption_rate * self.activity_factor * dt
        self.O2 -= consumption
        self.time += dt

    def run(self, max_time=600):
        history = []

        while self.O2 > 0 and self.time < max_time:
            history.append((self.time, self.O2))
            self.step()

            if self.O2 <= self.critical_threshold:
                break

        return history
