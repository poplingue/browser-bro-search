import asyncio
import random


def times_up(time, max, percentage):
    if time == max * percentage:
        return True


async def activity(user, timer):
    random_stop = random.randrange(0, 10) / 10

    for t in range(0, timer):

        if times_up(t, timer, random_stop):
            print('Activity is done with {} at {}'.format(user, t))
            return random_stop

        # suspend function and allow other functions to run
        await asyncio.sleep(0.01)


async def spending_time(user, timer):
    print('Start activity with {} with {} minutes'.format(user, timer))

    random_stop = await activity(user, timer)

    return random_stop


async def main():
    # launch functions in parallel
    monday = loop.create_task(spending_time('Alfred', 1000))
    tuesday = loop.create_task(spending_time('John', 10000))

    await asyncio.wait([
        monday,
        tuesday
    ])

    return monday, tuesday

if __name__ == '__main__':

    try:

        # use asyncio module
        loop = asyncio.get_event_loop()
        l1, l2 = loop.run_until_complete(main())

        print('random_stop {}'.format(l1.result()))
        print('random_stop {}'.format(l2.result()))

    except Exception as e:

        print('Error {}'.format(e))

    finally:

        loop.close()

# https://www.youtube.com/watch?v=tSLDcRkgTsY
