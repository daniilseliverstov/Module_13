import time
import asyncio


async def start_strongman(name, power):
    for ball in range(1, 6):
        print(f'Силач {name} начал соревнования.')
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Vasya', 3))
    task_2 = asyncio.create_task(start_strongman('Rafaele', 1))
    task_3 = asyncio.create_task(start_strongman('OnePunchMan', 10))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
