SlowDown = 100
Set MinecraftShell = WScript.CreateObject("WScript.Shell")
Do Until Success = True
    Success = MinecraftShell.AppActivate("Minecraft 1.8.7")
    rem Success = MinecraftShell.AppActivate("Notepad")
Loop

Wscript.Sleep 1000

MinecraftShell.SendKeys "{ESC}"
For Parameter1 = 0 To 25
    make = MakeBlock(Parameter1,Parameter1,Parameter1,"stained_hardened_clay",Parameter1)
Next
For Parameter1 = 0 To 23
    make = MakeBlock(Parameter1+2,Parameter1,Parameter1+2,"air",0)
Next

Function MakeBlock(x, y, z, block, blocktype)
    Command = "/fill ~"+CStr(x+x+1)+" ~"+CStr(y+y)+" ~"+CStr(z+z+1)+" ~"+CStr(101-x-x)+" ~"+CStr(y+y)+" ~"+CStr(101-z-z)+" "+block+" "+CStr(blocktype Mod 16)
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
    Wscript.Sleep 500
    MakeBlock=x
End Function

Wscript.Sleep SlowDown
MinecraftShell.SendKeys "{ESC}"
