SlowDown = 50
Set MinecraftShell = WScript.CreateObject("WScript.Shell")
Do Until Success = True
    Success = MinecraftShell.AppActivate("Minecraft 1.8.7")
    rem Success = MinecraftShell.AppActivate("Notepad")
Loop

Wscript.Sleep 1000

MinecraftShell.SendKeys "{ESC}"
For Parameter1 = 1 To 20
    make = MakeBlock(Parameter1,Parameter1,Parameter1,"wool",Parameter1)
Next

Function MakeBlock(x, y, z, block, blocktype)
    Command = "/fill ~"+CStr(x)+" ~"+CStr(y)+" ~"+CStr(z)+" ~"+CStr(x)+" ~"+CStr(y)+" ~"+CStr(z)+" "+block+" "+CStr(blocktype Mod 16)
    rem and = "/fill ~1 ~1 ~1 ~20 ~20 ~20 stone 7 hollow"
    For KeyStroke=1 To Len(Command)
        Wscript.Sleep SlowDown
        If Mid(Command,KeyStroke,1) <> "~" Then
            MinecraftShell.SendKeys Mid(Command,KeyStroke,1)
        Else
            MinecraftShell.SendKeys "{~}"
        End If
    Next
    Wscript.Sleep SlowDown
    MinecraftShell.SendKeys "{ENTER}"
    MakeBlock=x
End Function

Wscript.Sleep SlowDown
MinecraftShell.SendKeys "{ESC}"
