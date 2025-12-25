import asyncio

shared_resourse = 0

lock=asyncio.Lock()

async def modify_shared_resoures(id):
    global shared_resourse
    async with lock:
        print("#"*40)
        print(f"{id}: resource before modification: {shared_resourse}")
        shared_resourse+=1
        await asyncio.sleep(3)
        print(f"{id}: resoures after modification: {shared_resourse}")

async def main():
    await asyncio.gather(*(modify_shared_resoures(i+1) for i in range(4)))

asyncio.run(main())