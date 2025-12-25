from o2_model import OxygenModel

model = OxygenModel(
    O2_init=100.0,
    consumption_rate=0.25,
    activity_factor=1.2
)

history = model.run()

for t, o2 in history:
    print(f"Time: {t:4.0f}s | O2 level: {o2:6.2f}")
