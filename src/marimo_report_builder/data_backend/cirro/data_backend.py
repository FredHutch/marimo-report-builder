from cirro import DataPortal
from marimo_report_builder.data_backend import DataBackend


class CirroDataBackend(DataBackend):
    """
    Set up the portal (cirro.DataPortal) object as follows (make sure to fill out "domain.cirro.bio"):

    ---
    from cirro import DataPortalLogin
    ---
    get_client, set_client = mo.state(None)
    ---
    if get_client() is None:
        with mo.status.spinner("Authenticating"):
            # Use device code authorization to log in to Cirro
            cirro_login = DataPortalLogin(base_url="domain.cirro.bio")
            cirro_login_ui = mo.md(cirro_login.auth_message_markdown)
    else:
        cirro_login = None
        cirro_login_ui = None

    mo.stop(cirro_login is None)
    cirro_login_ui
    ---
    # Once the user logs in, set the client state
    set_client(cirro_login.await_completion())
    ---
    # Set up a data backend helper using that Cirro client object
    mo.stop(get_client() is None)
    data_backend = CirroDataBackend(get_client())
    """

    portal: DataPortal

    def __init__(
        self,
        portal: DataPortal
    ):
        self.portal = portal
