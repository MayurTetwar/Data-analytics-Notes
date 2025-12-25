import asyncio

async def fetch_data(delay):
    print(f"Fething data with delay of {delay} seconds...")
    await asyncio.sleep(delay)
    print(f"Data fetched after {delay} seconds!")
    return f"Data from {delay} seconds delay"

# define main corotine that runs corotine 
async def main():
    print("Start of main coroutine:")
    corotine = fetch_data(5)
    print("coroutine created, Now running......")

    # run corotine and wait for its completion
    result = await corotine
    print("coroutine completed completed with result:",result)

asyncio.run(main())