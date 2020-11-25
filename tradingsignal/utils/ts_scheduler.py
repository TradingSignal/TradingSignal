import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import UnknownTimeZoneError, utc
from tradingsignal.utils import ts_logging

# Don't use this directly. Use scheduler() instead.
_scheduler = None


async def scheduler() -> AsyncIOScheduler:
    """Return apscheduler instance."""
    global _scheduler
    if _scheduler:
        return _scheduler

    try:
        _scheduler = AsyncIOScheduler(event_loop=asyncio.get_event_loop())
    except UnknownTimeZoneError:
        ts_logging.raise_warning(
            "apscheduler could not find a timezone configuration and added to default to utc."
        )
        _scheduler = AsyncIOScheduler(
            event_loop=asyncio.get_event_loop(), timezone=utc
        )

    _scheduler.start()
    return _scheduler
