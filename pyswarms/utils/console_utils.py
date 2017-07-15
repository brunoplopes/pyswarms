def cli_print(msg, v, t):
	"""Helper function to print console output

	Inputs:
		- msg: message as string
		- v: verbosity setting by user
		- t: threshold. If v > t, then msg prints.
	"""
	if v >= t:
		print(msg)
	else:
		pass