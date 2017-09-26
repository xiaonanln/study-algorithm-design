
class ExpectError(Exception):
	pass


def expect(expr):
	if not expr:
		raise ExpectError()
