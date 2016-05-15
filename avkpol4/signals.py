from django.dispatch import Signal,receiver


signal = Signal(providing_args=["datetime"])