def QueueTramsfering(Queue):
	Qlist = []
	while True:
		try:
			Qlist.append(Queue.get(timeout=1))
		except:
			break
	return Qlist