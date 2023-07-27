# Toggle if to enable/disable compiling documentations.
#  0 = no
#  1 = yes
%define build_doc 0

Name:           antimicrox
Version:        3.3.4
Release:        1
Summary:        Graphical program used to map keyboard keys and mouse controls to a game-pad
License:        GPL-3.0
Group:          Hardware/Joystick
URL:            https://github.com/AntiMicroX/antimicroX
Source0:        https://github.com/AntiMicroX/antimicrox/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires: appstream-util
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xtst)

%if %build_doc
BuildRequires: doxygen
%endif

Requires:       systemd

%description
AntiMicroX is a graphical program used to map gamepad keys to keyboard, mouse, scripts and macros. 
You can use this program to control any desktop application with a gamepad on Linux. 
It can be also used for generating SDL2 configuration (useful for mapping atypical gamepads to generic ones like xbox360).
We support X.org and Wayland.
It allows mapping of gamepads/joystick buttons to:
-keyboard buttons
-mouse buttons and moves
-scripts and executables
-macros consisting of elements mentioned above

This application is continuation of project called AntiMicro, which was later abandoned and revived by Jagoda Górska (juliagoda).

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake  \
        -DAPPDATA=OFF \
        -DCMAKE_BUILD_TYPE=Release

%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt


%files -f %{name}.lang
%license LICENSE
%doc CHANGELOG.md README.md ProfileTips.md
%exclude %{_datadir}/%{name}/CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/antimicrox/LICENSE_SDL_GameControllerDB
%{_datadir}/antimicrox/gamecontrollerdb.txt
%{_datadir}/antimicrox/translations/antimicrox.qm
%{_datadir}/applications/io.github.antimicrox.%{name}.desktop
#{_datadir}/metainfo/io.github.antimicrox.%{name}.appdata.xml
%{_datadir}/mime/packages/io.github.antimicrox.%{name}.xml
%{_iconsdir}/*/*/apps/*
%{_mandir}/man1/antimicrox.1.*
%{_prefix}/lib/udev/rules.d/60-antimicrox-uinput.rules
