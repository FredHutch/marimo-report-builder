import marimo as mo
from functools import lru_cache
from cirro import DataPortal


@lru_cache
def list_projects(_portal: DataPortal):
    with mo.status.spinner("Listing projects"):
        return _portal.list_projects()


def list_datasets(_portal: DataPortal, project_id: str):
    with mo.status.spinner("Listing datasets"):
        ds_list = _portal.get_project_by_id(project_id).list_datasets()
    ds_list.sort(key=lambda ds: ds.created_at)
    return ds_list


@lru_cache
def list_files(_portal: DataPortal, project_id: str, dataset_id: str):
    with mo.status.spinner("Listing files"):
        return _portal.get_dataset(project_id, dataset_id).list_files()


@lru_cache
def read_csv(_portal: DataPortal, project_id: str, dataset_id: str, file_path: str, **kwargs):
    with mo.status.spinner("Reading CSV"):
        return (
            _portal
            .get_dataset(project_id, dataset_id)
            .get_file(file_path)
            .read_csv(**kwargs)
        )
