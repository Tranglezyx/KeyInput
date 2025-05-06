import asyncio

async def test():
    await asyncio.sleep(3)
    print("test ----")
    return "1"

async def main():
    num =  await test()
    print(f"main ---- {num}")

if __name__ == "__main__":
    asyncio.run(main())
    