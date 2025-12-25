import asyncio

async def main():
    print("Hello, World!")
    asyncio.sleep(2)
    print("Goodbye, World!")

print('#### Type of the main():',type(main()))  # coroutine object
# main() returns a ruotine object, which is then run by asyncio.run()

# run the main coroutine
print("### Running coroutine")
asyncio.run(main())