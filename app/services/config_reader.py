import json
import os
from app.models import Vendor, Device, Option

class ConfigReader:
    def run(self):
        files = self.load_config_files()
        for file in files:
            with open(file, 'r') as f:
                json_data = json.load(f)

            vendor, created = Vendor.objects.get_or_create(name=json_data.get('vendor'))
            device, created = Device.objects.get_or_create(codename=json_data.get('codename'))
            self.update_device(device, vendor, json_data)

            device.options.update(state=10)

            for option_key, option_value in json_data.get('options').items():
                option, created = Option.objects.get_or_create(device=device, label=option_key)
                if isinstance(option_value, list):
                    option.update(data_type='enum', default=None, possible_values=','.join(option_value), state=0)
                else:
                    option.update(data_type='bool', default=option_value, possible_values=None, state=0)

    def update_device(self, device, vendor, json_data):
        device.update(
            vendor=vendor,
            name=json_data.get('device'),
            commit=json_data.get('commit'),
            needs_rom_dump=json_data.get('blobs') == 'yes'
        )

    def load_config_files(self):
        import glob
        config_files = glob.glob("config/devices/**/*")
        return config_files