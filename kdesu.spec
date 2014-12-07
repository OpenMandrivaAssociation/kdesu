%define major 5
%define libname %mklibname KF5KDESu %{major}
%define devname %mklibname KF5KDESu -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdesu
Version: 5.4.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 library for obtaining superuser privileges
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Pty)
BuildRequires: cmake(KF5I18n)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 library for obtaining superuser privileges

%package -n %{libname}
Summary: KDE Frameworks 5 library for obtaining superuser privileges
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 library for obtaining superuser privileges

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Desu library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Desu library

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang kdesud5

%files -f kdesud5.lang
%{_libdir}/libexec/kf5/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/*
