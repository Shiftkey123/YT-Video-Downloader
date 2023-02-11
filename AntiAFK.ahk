MsgBox, Welcome to my Anti-AFK script. This will ensure you never get kicked for being afk. This may not work on some games due to anticheat. Click "OK" to continue.
MsgBox, 4,, Click "OK" to start AntiAFK Script. F8 Starts and Pauses the script. F7 fully closes the script.
IfMsgBox, No
	return
Pause on
Loop
{
	Send, {w down}
	Sleep, 250
	Send, {w up}
	Send, {a down}
	Sleep, 250
	Send, {a up}
	Send, {s down}
	Sleep, 250
	Send, {s up}
	Send, {d down}
	Sleep, 250
	Send, {d up}
	Sleep, 500
}
F7::ExitApp
F8::
Pause
