import asyncio
# for multiple corotine 

async def fetch_data(delay, id):
    print(f"Fething data with delay of {delay} seconds for ID: {id}...")
    await asyncio.sleep(delay)
    if id==2:
        raise ValueError(f"An error occurred while fetching data for ID : {id}")
    print(f"Data fetched after {delay} seconds for ID: {id}!")
    return f"Data from {delay} seconds delay for ID: {id}"

# define main corotine that runs corotine 
async def main():
    print("Start of main corotine:")
    corotine1 = asyncio.create_task(fetch_data(2,1))
    corotine2 = asyncio.create_task(fetch_data(3,2))
    corotine3 = asyncio.create_task(fetch_data(4,3))

    print("corotine created, Now running......")

    # run corotine and wait for its completion
    result1 = await corotine1
    print("Corotine completed completed with result1  :",result1)
    result2 = await corotine2
    print("Corotine completed completed with result2  :",result2)
    result3 = await corotine3
    print("Corotine completed completed with result3  :",result3)

asyncio.run(main())
