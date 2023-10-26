"""Guess the driver kind"""

def GetDevice(index=0, dump=False):
	try:
		print("Probing LibUSB...", end=' ')
		from .LibusbDriver import LibusbDriver
		drv = LibusbDriver(index=index, dump=dump)
		drv.open()
		drv.close()
		print("ok")
		return drv
	except Exception as e:
		print(e)
		try:
			print("Probing Hantek...", end=' ')
			from .HTDriver import HTDriver
			drv = HTDriver(index=index, dump=dump)
			drv.open()
			drv.close()
			print("ok")
			return drv
		except Exception as e:
			print(e)
			return None

__all__ = ["GetDevice"]
