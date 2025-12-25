import asyncio
# for multiple corotine 

async def fetch_data(delay, id):
    print(f"Fething data with delay of {delay} seconds for ID: {id}...")
    await asyncio.sleep(delay)
    print(f"Data fetched after {delay} seconds for ID: {id}!")
    return f"Data from {delay} seconds delay for ID: {id}"

# define main corotine that runs corotine 
async def main():
    print("Start of main corotine:")
    corotine1 = fetch_data(3,1)
    corotine2 = fetch_data(3,2)
    print("corotine created, Now running......")

    # run corotine and wait for its completion
    result1 = await corotine1
    print("Corotine completed completed with result1  :",result1)
    result2 = await corotine2
    print("Corotine completed completed with result1  :",result2)

asyncio.run(main())
"""
👉 Asynchronous programming means:
    1. Doing multiple tasks without blocking the program
    2. While one task is waiting (like for time, network, I/O), another task can run
"""