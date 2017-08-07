import wx
import sys

class Mywin(wx.Frame):
    def __init__(self):
        super(Mywin,self).__init__(None,-1,"tupian",size = (600,410))
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        filepick = wx.FilePickerCtrl(panel,-1,style = wx.FLP_DEFAULT_STYLE)
        filepick.Bind(wx.EVT_FILEPICKER_CHANGED,self.OnFileChanged)
        box.Add(filepick,0,wx.ALIGN_CENTER_HORIZONTAL)

        slider1 = wx.Slider(panel ,-1, 0, 0, 255, size = (256,32),style = wx.SL_AUTOTICKS|wx.SL_VALUE_LABEL)
        box.Add(slider1,0,wx.ALIGN_CENTER_HORIZONTAL)
        slider1.Bind(wx.EVT_SLIDER,self.OnSlider1)
        slider2 = wx.Slider(panel ,-1, 0, 0, 255, size = (256,32),style = wx.SL_AUTOTICKS|wx.SL_VALUE_LABEL)
        box.Add(slider2,0, wx.ALIGN_CENTER_HORIZONTAL)
        slider2.Bind(wx.EVT_SLIDER, self.OnSlider2)
        slider3 = wx.Slider(panel ,-1, 0, 0, 255, size = (256,32),style = wx.SL_AUTOTICKS|wx.SL_VALUE_LABEL)
        box.Add(slider3,0, wx.ALIGN_CENTER_HORIZONTAL)
        slider3.Bind(wx.EVT_SLIDER, self.OnSlider3)
        self.bmp = wx.StaticBitmap(panel,-1)
        box.Add(self.bmp,1,wx.ALIGN_CENTER_HORIZONTAL)

        panel.SetSizer(box)


    def OnFileChanged(self, event):
        self.img = wx.Image(event.GetEventObject().GetPath(),wx.BITMAP_TYPE_ANY)#.ConvertToBitmap()
        self.bmp.SetBitmap(self.img.ConvertToBitmap())
        self.sizew = self.img.GetWidth()
        self.sizeh = self.img.GetHeight()

    def OnSlider1(self,event):
        value= event.GetEventObject().GetValue()

        for w in range(self.sizew):
            for h in range(self.sizeh):
                self.img.SetRGB(w,h,value,self.img.GetGreen(w,h),self.img.GetBlue(w,h))
        self.bmp.SetBitmap(self.img.ConvertToBitmap())

    def OnSlider2(self, event):
        value = event.GetEventObject().GetValue()

        for w in range(self.sizew):
            for h in range(self.sizeh):
                self.img.SetRGB(w, h, self.img.GetRed(w,h), value, self.img.GetBlue(w, h))
        self.bmp.SetBitmap(self.img.ConvertToBitmap())

    def OnSlider3(self, event):
        value = event.GetEventObject().GetValue()

        for w in range(self.sizew):
            for h in range(self.sizeh):
                self.img.SetRGB(w, h, self.img.GetRed(w, h), self.img.GetGreen(w,h), value)
        self.bmp.SetBitmap(self.img.ConvertToBitmap())

if __name__ == "__main__":
    app = wx.App()
    frame = Mywin()
    frame.Show()
    app.MainLoop()
    sys.exit()