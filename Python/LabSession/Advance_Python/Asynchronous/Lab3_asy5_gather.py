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
    result = await asyncio.gather(      
        fetch_data(3,1),
        fetch_data(5,2),
        fetch_data(3,3)
    )
    print("corotine created, Now running......")

    for i,res in enumerate(result):
        print(f"Corotine {i+1} complete with result: {res}")

asyncio.run(main())
