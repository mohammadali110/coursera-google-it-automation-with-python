
# Usage of various keyword examples

# Example 1: keyword = assert
import math as myAlias
print(myAlias.cos(myAlias.pi))

a = 4
# uncomment below line to execute. 
# Be mindful it will stop execution of rest of the code is assertion fails

# assert a > 5, "The value of a is too small"


# Example 2: keyword=await
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())