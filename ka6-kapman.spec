#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kapman
Summary:	Kapman
Name:		ka6-%{kaname}
Version:	24.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	83c84a673c9325d4653ef9c82e4dde29
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kapman is a clone of the well known game Pac-Man.

You must run through the maze to eat all pills without being captured
by a ghost. By eating an energizer, Kapman gets the ability to eat
ghosts for a few seconds. When a stage is cleared of pills and
energizer the player is taken to the next stage with slightly
increased game speed.

%description -l pl.UTF-8
Kapman jest klonem dobrze znanej gry Pac-Man.

Musisz przemieszczać się przez labirynt, połykać pigułki i unikać duchów.
Zjadając energetyka, Kapman otrzymuje moc zjadania duchów, która trwa
kilka sekund. Gdy plansza zostanie wyczyszczona z pigułek i energetyka,
gracz jest przenoszony na następny poziom z nieco przyspieszoną rozgrywką.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapman
%{_desktopdir}/org.kde.kapman.desktop
%{_iconsdir}/hicolor/128x128/apps/kapman.png
%{_iconsdir}/hicolor/16x16/apps/kapman.png
%{_iconsdir}/hicolor/22x22/apps/kapman.png
%{_iconsdir}/hicolor/32x32/apps/kapman.png
%{_iconsdir}/hicolor/48x48/apps/kapman.png
%{_iconsdir}/hicolor/64x64/apps/kapman.png
%{_datadir}/kapman
%{_datadir}/metainfo/org.kde.kapman.appdata.xml
%{_datadir}/sounds/kapman
