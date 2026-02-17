"""Firebase bootstrap helpers."""

from __future__ import annotations

import firebase_admin
from firebase_admin import credentials

from .config import settings


_initialized = False


def init_firebase() -> bool:
    """Initialize Firebase admin if env config is available.

    Returns True if initialized, False when skipped.
    """

    global _initialized
    if _initialized:
        return True

    if not settings.firebase_project_id:
        return False

    options: dict[str, str] = {'projectId': settings.firebase_project_id}
    if settings.firebase_storage_bucket:
        options['storageBucket'] = settings.firebase_storage_bucket

    firebase_admin.initialize_app(credentials.ApplicationDefault(), options=options)
    _initialized = True
    return True
