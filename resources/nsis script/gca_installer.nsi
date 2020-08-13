; gca_installer.nsi
;

;--------------------------------

; The name of the installer
Name "GCA Analysis Tool Installer"

; The file to write
OutFile "GCA Analysis Tool v4.10.exe"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

; Build Unicode installer
Unicode True

; The default installation directory
;InstallDir "$DESKTOP\GCA Analysis Tool"
InstallDir "$PROGRAMFILES\GCA Analysis Tool"

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\GCA_Analysis_Tool" "Install_Dir"

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles


;--------------------------------

; The stuff to install
Section "GCA Analysis Tool (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  File "..\..\dist\GCA Analysis Tool.exe"
  File "..\..\COPYING.rtf"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM "SOFTWARE\GCA_Analysis_Tool" "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\GCA_Analysis_Tool" "DisplayName" "GCA Analysis Tool"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\GCA_Analysis_Tool" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\GCA_Analysis_Tool" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\GCA_Analysis_Tool" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
SectionEnd

; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

  CreateDirectory "$SMPROGRAMS\GCA Analysis Tool"
  CreateShortcut "$SMPROGRAMS\GCA Analysis Tool\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortcut "$SMPROGRAMS\GCA Analysis Tool\GCA Analysis Tool.lnk" "$INSTDIR\GCA Analysis Tool.exe" "" "$INSTDIR\GCA Analysis Tool.exe" 0
  
SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\GCA_Analysis_Tool"
  DeleteRegKey HKLM "SOFTWARE\GCA_Analysis_Tool"

  ; Remove files and uninstaller
  Delete "$INSTDIR\GCA Analysis Tool.exe"
  Delete "$INSTDIR\COPYING.rtf"
  Delete "$INSTDIR\uninstall.exe"

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\GCA Analysis Tool\*.*"

  ; Remove directories used
  RMDir "$SMPROGRAMS\GCA Analysis Tool"
  RMDir "$INSTDIR"

SectionEnd