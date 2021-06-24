from apscheduler.schedulers.blocking import BlockingScheduler
# https://blog.csdn.net/weixin_39726347/article/details/88586860
def main():
	sched = BlockingScheduler()
	sched.add_job(roll, trigger='interval', hours=2)
	sched.start()


def roll():
	for i in range(1, 20):
		print(f'rotate{i}deg')

main()


if temp >= 35:
	stop()
else:
	start()