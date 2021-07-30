import asyncio

import ydb
import os


queries = [  # Tables description to create
    """
    CREATE table `series` (
        `series_id` Uint64,
        `title` Utf8,
        `series_info` Utf8,
        `release_date` Date,
        PRIMARY KEY (`series_id`)
    )
    """,
    """
    CREATE table `seasons` (
        `series_id` Uint64,
        `season_id` Uint64,
        `title` Utf8,
        `first_aired` Date,
        `last_aired` Date,
        PRIMARY KEY (`series_id`, `season_id`)
    )
    """,
    """
    CREATE table `episodes` (
        `series_id` Uint64,
        `season_id` Uint64,
        `episode_id` Uint64,
        `title` Utf8,
        `air_date` Date,
        PRIMARY KEY (`series_id`, `season_id`, `episode_id`)
    )
    """
]


async def create_table(session, query):
    """
    Helper function to acquire session, execute `create_table` and release it
    """
    await session.execute_scheme(query)


async def main():
    endpoint = os.getenv('YDB_ENDPOINT')
    database = os.getenv('YDB_DATABASE')
    driver = ydb.aio.Driver(
        endpoint=endpoint,
        database=database
    )
    pool = ydb.aio.SessionPool(
        driver,
        size=10  # Max number of available session
    )

    coros = [  # Generating coroutines to create tables concurrently
        pool.retry_operation(create_table, query)
        for query in queries
    ]
    await asyncio.gather(*coros)  # Run table creating concurrently

    await pool.stop()
    await driver.stop()
    directory = await driver.scheme_client.list_directory(database)  # Listing database to ensure that tables are created
    print("Items in database:")
    for child in directory.children:
        print(child.type, child.name)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
