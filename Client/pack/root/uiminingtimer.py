import ui
import wndMgr
import app
import player

WIDTH = 115
HEIGHT = 40

class MiningTimerWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.SetSize(WIDTH, HEIGHT)
		self.UI = {}

		self.time = 0
		self.timeType = player.MINING_TIMER_SUBHEADER_GC_RESET

		self.__LoadWindow()

	def __LoadWindow(self):
		screenHeight = wndMgr.GetScreenHeight()
		screenWidth = wndMgr.GetScreenWidth()

		self.SetPosition(
			(screenWidth / 2 - WIDTH / 2),
			(screenHeight / 2 - (screenHeight / 4))
		)

		self.UI["thinBoard"] = ui.ThinBoard()
		self.UI["thinBoard"].SetParent(self)
		self.UI["thinBoard"].SetSize(WIDTH, HEIGHT)
		self.UI["thinBoard"].SetPosition(0, 0)
		self.UI["thinBoard"].Show()

		self.UI["timer"] = ui.TextLine()
		self.UI["timer"].SetParent(self.UI["thinBoard"])
		self.UI["timer"].SetPosition(45, 5)
		self.UI["timer"].SetText("00:00")
		self.UI["timer"].SetPackedFontColor(ui.GenerateColor(255, 190, 0))
		self.UI["timer"].SetFontName("Tahoma:28")
		self.UI["timer"].Show()

		self.UI["ImageBox"] = ui.ImageBox()
		self.UI["ImageBox"].SetParent(self.UI["thinBoard"])
		self.UI["ImageBox"].SetPosition(10, 6)
		self.UI["ImageBox"].Show()

		self.SetTop()

	def GetMiningTimer(self, timeType, time):
		if timeType == player.MINING_TIMER_SUBHEADER_GC_RESET:
			self.Close()
			return

		self.time = app.GetGlobalTimeStamp() + int(time)
		self.timeType = int(timeType)
		self.Show()

	def Close(self):
		self.Hide()
		self.time = 0
		self.timeType = player.MINING_TIMER_SUBHEADER_GC_RESET

	def OnUpdate(self):
		if self.timeType == player.MINING_TIMER_SUBHEADER_GC_RESET:
			return

		showTime = int(self.time - app.GetGlobalTimeStamp())

		if showTime <= 0 and self.timeType != player.MINING_TIMER_SUBHEADER_GC_WAITING:
			self.Close()
			return

		if showTime < 0:
			showTime = 0
		minutes = showTime // 60
		seconds = showTime % 60
		time_str = "%02d:%02d" % (minutes, seconds)
		self.UI["timer"].SetText(time_str)

		if self.timeType == player.MINING_TIMER_SUBHEADER_GC_WAITING:
			self.UI["timer"].SetPackedFontColor(ui.GenerateColor(255, 255, 255))
			self.UI["ImageBox"].LoadImage("d:/ymir work/ui/game/timer/waiting.tga")
		elif self.timeType == player.MINING_TIMER_SUBHEADER_GC_GET:
			self.UI["timer"].SetPackedFontColor(ui.GenerateColor(255, 190, 0))
			self.UI["ImageBox"].LoadImage("d:/ymir work/ui/game/timer/get.tga")

		self.Show()
