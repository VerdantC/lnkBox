; #NoTrayIcon
#SingleInstance force
#Persistent
; 移除默认的标准菜单项
Menu, Tray, NoStandard 
Menu, Tray, Add, Exit, ExitScript


; global appPath := "conf\\test5.exe"
test_name := "main"
global appPath := "conf\" . test_name . ".exe"

!e::
SetStoreCapsLockMode, Off
; 1,判定当前窗口
; WinGetClass, currentClass, A
; if (currentClass = "CabinetWClass" ) {
    ;     DirPath := GetActiveExplorerPath()
    ;     RunApp(DirPath)
    ;     return
    ; } 
    
    
    ; 2 剪贴板
    ; DirPath := GetSelectedFilePath()
    
    ; if InStr(FileExist(DirPath), "D") {
    ;     RunApp(DirPath)
    ;     return
    ; }
;2

    ; IfWinExist, ahk_exe test5.exe
    IfWinExist, ahk_exe %test_name%.exe
    {
        WinClose
        return
    }
    
    RunApp2()

SetStoreCapsLockMode, On
return
; ######################################################################################
RunApp(DirPath)
{
    Run, %appPath% "%DirPath%"
}

RunApp2()
{
    Run, %appPath% 
}

ExitScript:
    ExitApp ; 退出脚本

    ; 获取当前选中的文件路径
    GetActiveExplorerPath()
    {
        explorerHwnd := WinActive("ahk_class CabinetWClass")
        if (explorerHwnd)
        {
            for window in ComObjCreate("Shell.Application").Windows
            {
                if (window.hwnd==explorerHwnd)
                {
                    return window.Document.Folder.Self.Path
                }
            }
        }
    }
GetSelectedFilePath() {
    ; 保存剪贴板当前内容
    ClipSaved := ClipboardAll
    Clipboard := "" ; 清空剪贴板

    ; 发送复制快捷键 (Ctrl+C)
    Send, ^c
    ClipWait, 0.005 ; 等待剪贴板有内容

    ; 获取剪贴板内容
    FilePath := Clipboard

    ; 还原剪贴板内容
    Clipboard := ClipSaved
    ClipSaved = ; 清空保存的内容

    ; 返回文件路径
    return FilePath
}



