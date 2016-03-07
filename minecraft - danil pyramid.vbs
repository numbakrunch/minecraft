SlowDown = 100
Set MinecraftShell = WScript.CreateObject("WScript.Shell")
Do Until Success = True
    Success = MinecraftShell.AppActivate("Minecraft 1.8.7")
    rem Success = MinecraftShell.AppActivate("Notepad")
Loop

Wscript.Sleep 1000

MinecraftShell.SendKeys "{ESC}"
For Parameter1 = 0 To 40
    make = MakeBlock(Parameter1,Parameter1,Parameter1,"stained_glass",Parameter1)
Next
For Parameter1 = 0 To 39
    make = MakeBlock(Parameter1+1,Parameter1,Parameter1+1,"air",0)
Next

Function MakeBlock(x, y, z, block, blocktype)
    blocktype2 = ((blocktype * 3) Mod 11)
    If blocktype2 >= 0 Then
        blocktype2 = blocktype2 + 1
    End If
    If blocktype2 >= 7 Then
        blocktype2 = blocktype2 + 1
    End If
    If blocktype2 >= 8 Then
        blocktype2 = blocktype2 + 1
    End If
    If blocktype2 >= 12 Then
        blocktype2 = blocktype2 + 1
    End If
    If blocktype2 >= 15 Then
        blocktype2 = blocktype2 + 1
    End If
    Command = "/fill ~"+CStr(x+1)+" ~"+CStr(y)+" ~"+CStr(z+1)+" ~"+CStr(81-x)+" ~"+CStr(y)+" ~"+CStr(81-z)+" "+block+" "+CStr(blocktype2 Mod 16)
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
