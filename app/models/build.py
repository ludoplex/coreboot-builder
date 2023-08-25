from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import select, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BuildState(Enum):
    NEW_BUILD = 0
    DEVICE_CHOSEN = 10
    BLOB_FILE_UPLOADED = 20
    OPTIONS_CONFIGURED = 30
    CONFIGURED = 40
    PENDING = 50
    STARTED = 60
    SUCCEEDED = 70
    FAILED = 80

class Build(Base):
    __tablename__ = 'builds'

    id = Column(Integer, primary_key=True)
    state = Column(Enum(BuildState), nullable=False)
    email = Column(String, nullable=False)
    device_id = Column(Integer, ForeignKey('devices.id'))
    blob_file = Column(String)
    gpg = Column(String)
    url = Column(String)
    uuid = Column(String)

    device = relationship("Device", back_populates="builds")
    configurations = relationship("Configuration", back_populates="build")

    def __init__(self, **kwargs):
        super(Build, self).__init__(**kwargs)
        if not self.uuid:
            self.uuid = str(uuid.uuid4())

    @property
    def device_chosen_or_beyond(self):
        return self.state in [BuildState.DEVICE_CHOSEN, BuildState.BLOB_FILE_UPLOADED, BuildState.OPTIONS_CONFIGURED, BuildState.CONFIGURED, BuildState.PENDING, BuildState.STARTED, BuildState.SUCCEEDED, BuildState.FAILED]

    @property
    def blob_file_uploaded_or_beyond_and_needs_rom(self):
        return self.blob_file_uploaded_or_beyond and self.device.needs_rom_dump

    @property
    def blob_file_uploaded_or_beyond(self):
        return self.state in [BuildState.BLOB_FILE_UPLOADED, BuildState.OPTIONS_CONFIGURED, BuildState.CONFIGURED, BuildState.PENDING, BuildState.STARTED, BuildState.SUCCEEDED, BuildState.FAILED]

    @property
    def configured_or_beyond(self):
        return self.state in [BuildState.CONFIGURED, BuildState.PENDING, BuildState.STARTED, BuildState.SUCCEEDED, BuildState.FAILED]
