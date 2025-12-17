from cirro import DataPortal
from marimo_report_builder.data_backend import DataBackend


class CirroDataBackend(DataBackend):

    portal: DataPortal

    def __init__(
        self,
        portal: DataPortal
    ):
        self.portal = portal
