class Build:
    def __init__(self, id, state, email, device_id, blob_file, gpg, url, uuid):
        self.id = id
        self.state = state
        self.email = email
        self.device_id = device_id
        self.blob_file = blob_file
        self.gpg = gpg
        self.url = url
        self.uuid = uuid

    @property
    def device_chosen_or_beyond(self):
        return self.state in [0, 10, 20, 30, 40, 50, 60, 70, 80]

    @property
    def blob_file_uploaded_or_beyond_and_needs_rom(self):
        return self.blob_file_uploaded_or_beyond and self.device.needs_rom_dump

    @property
    def blob_file_uploaded_or_beyond(self):
        return self.state in [20, 30, 40, 50, 60, 70, 80]

    @property
    def configured_or_beyond(self):
        return self.state in [40, 50, 60, 70, 80]
