import time
import asyncio
import random


def times_up(time, max, percentage):

    if time == max*percentage:
        return True


async def activity(user, timer):

    random_stop = random.randrange(0, 10)/10

    for t in range(0, timer):

        if times_up(t, timer, random_stop):

            print('Activity is done with {} at {}'.format(user, t))
            return user

        # suspend function and allow other functions to run
        await asyncio.sleep(0.01)


async def spending_time(user, timer):

    print('Start activity with {} with {} minutes'.format(user, timer))

    await activity(user, timer)

    return None


async def main():

    # launch functions in parallel
    await asyncio.wait([
        spending_time('Mitch', 1000),
        spending_time('Lena', 100)
    ])


if __name__ == '__main__':

    try:

        # use asyncio module
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    except Exception as e:

        print('Error {}'.format(e))


    finally:
        loop.close()

# https://www.youtube.com/watch?v=tSLDcRkgTsY
