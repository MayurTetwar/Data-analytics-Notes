import asyncio

async def access_resoures(sepamore,resource_id):
    async with sepamore:
        print("#"*40)
        print(f"{id}: Accessing resources {resource_id}")
        await asyncio.sleep(2)
        print(f"{id}: Releasing resources {resource_id}")

async def main():
    semaphore = asyncio.Semaphore(2)    # allow 2 concurrent acesses
    await asyncio.gather(*(access_resoures(semaphore,i) for i in range(4)))

asyncio.run(main())