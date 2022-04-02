import asyncio
from time import sleep
from loguru import logger


def sync_foo():
    logger.info("Startng sync foo")
    sleep(1)
    logger.info("Finishing sync foo")


def sync_bar():
    logger.info("Startng sync bar")
    sleep(1)
    logger.info("Finishing sync bar")


async def foo():
    logger.info("Startng async foo")
    await asyncio.sleep(1)
    logger.info("Finishing async foo")


async def bar():
    logger.info("Startng async bar")
    await asyncio.sleep(1)
    logger.info("Finishing async bar")


def run_sync():
    sync_foo()
    sync_bar()


async def run_async():
    await foo()
    await bar()


async def main_async():
    logger.info("Starting main async")
    # await run_async()
    # await asyncio.gather(foo(), bar())

    await run_many_async_funcs(10)

    logger.info("Finishing main async")


async def some_async_func(number: int):
    logger.info("Start some func #{}", number)
    await asyncio.sleep(1)
    if number % 3 == 0:
        await asyncio.sleep(number / 10)
    logger.info("Finish some func #{}", number)


async def run_many_async_funcs(count: int):
    coros = [
        some_async_func(i)
        for i in range(count)
    ]
    logger.info("Prepare {} coros", count)
    # await asyncio.gather(*coros)  # simple version
    tasks = [asyncio.create_task(coro) for coro in coros]
    logger.info("start awaiting {} tasks", count)
    await asyncio.wait(tasks)
    logger.info("finished running {} roros", count)

def main():
    logger.info("Starting main")
    run_sync()


if __name__ == "__main__":
    asyncio.run(main_async())